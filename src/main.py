import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tqdm import tqdm
from dex_utils import fetch_dex_contact_by_id, extract_dex_id_from_url, update_spreadsheet
from contact_manager import (
    fetch_google_contacts_and_dex_id,
    upload_image_to_google_contact,
    filter_contacts_with_missing_photos,
    download_and_store_image,
)
from google_credentials import setup_google_credentials

# Constants
CONTACT_PHOTO_FOLDER = 'contact photos'
SPREADSHEET_NAME = 'photo inventory.xls'

# Load Dex API key from file
with open("dex-api.txt", "r") as f:
    DEX_API_KEY = f.read().strip()

# Progress bar format
L_BAR = '{desc}: {percentage:3.0f}%|'
R_BAR = '| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, ' '{rate_fmt}{postfix}]'

def main():
    delete_all_missing = False  # Initialize the flag
    creds = setup_google_credentials()
    service = build('people', 'v1', credentials=creds)

    # Ask the user for their choice
    user_choice = input("Do you want to retrieve [A]ll photos or only [M]issing photos? (A/M): ").strip().lower()

    if user_choice == 'a':
        # Retrieve all photos
        contacts = fetch_google_contacts_and_dex_id(service)
    elif user_choice == 'm':
        # Retrieve missing photos (only upload if no existing photo)
        all_contacts = fetch_google_contacts_and_dex_id(service)
        contacts = filter_contacts_with_missing_photos(all_contacts, service)
    else:
        print("Invalid choice. Please select either [A] or [M].")
        return

    # Create a tqdm object with the total number of contacts
    progress = tqdm(total=len(contacts), dynamic_ncols=True, unit=" contacts", bar_format=None)

    for contact in contacts:
        try:
            # Extract the Dex URL from the contact's urls field
            dex_url = next((url['value'] for url in contact.get('urls', []) if "Dex Contact Details" in url.get('type', '')), None)
            
            # If no Dex URL is found, update the progress bar and continue
            if not dex_url:
                progress.update(1)  # Update the progress bar
                continue

            # Extract the Dex Contact ID from the Dex URL
            dex_contact_id = extract_dex_id_from_url(dex_url)
            display_name = contact['names'][0]['displayName']

            progress.set_description(display_name)
            progress.bar_format='{percentage:3.0f}%| {bar}{desc}' + R_BAR

            # Fetch the contact details from Dex using the Dex Contact ID
            dex_contact = fetch_dex_contact_by_id(dex_contact_id, DEX_API_KEY)
            
            # Check if dex_contact is None
            if dex_contact is None:
                if not delete_all_missing:
                    # Dex contact not found, ask the user what to do
                    user_input = input(f"{display_name} not found in Dex. Do you want to delete it from Google Contacts? (y/n/A for all): ").strip()
                    if user_input.lower() == 'y':
                        try:
                            # Delete the contact from Google Contacts
                            service.people().deleteContact(resourceName=contact['resourceName']).execute()
                            print(f"Deleted {display_name} from Google Contacts.")
                        except HttpError as e:
                            print(f"Error deleting {display_name} from Google Contacts: {e}")
                    elif user_input == 'A':
                        delete_all_missing = True  # Set the flag to delete all missing contacts

                if delete_all_missing:
                    try:
                        # Delete the contact from Google Contacts
                        service.people().deleteContact(resourceName=contact['resourceName']).execute()
                        print(f"Deleted {display_name} from Google Contacts.")
                    except HttpError as e:
                        print(f"Error deleting {display_name} from Google Contacts: {e}")
                    
                continue  # Skip to the next contact if not found

            # Extract the image URL
            image_url = dex_contact.get("image_url")
            
            # If image_url is blank or None, update the progress bar and continue
            if not image_url:
                progress.update(1)  # Update the progress bar
                continue

            # Download the image and store it
            image_path = download_and_store_image(image_url, display_name, CONTACT_PHOTO_FOLDER)

            # Upload the image to Google Contacts
            upload_image_to_google_contact(service, contact['resourceName'], image_path)
            
            # Add entry to spreadsheet
            update_spreadsheet(display_name, dex_contact_id, image_url)
            
            progress.update(1)  # Update the progress bar

        except KeyError:
            # Handle the KeyError (missing 'names' key) by printing an error message and continuing to the next contact
            print(f"KeyError: 'names' key is missing for a contact.")
            progress.update(1)  # Update the progress bar
            continue

    progress.close()  # Close the progress bar

if __name__ == "__main__":
    main()
