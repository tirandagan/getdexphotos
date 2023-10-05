import urllib.request
import base64
import time
from tqdm import tqdm
import os

LIMIT_CONTACTS = 0  # set to 0 for no limit on # of contacts (for testing)


def fetch_google_contacts_and_dex_id(service):
    all_connections = []
    page_token = None

    # Initialize a tqdm object with an unknown total (using total=None)
    progress = tqdm(total=None, dynamic_ncols=True, desc="Fetching contacts", unit=" contacts")

    while True:
        results = service.people().connections().list(
            resourceName='people/me',
            pageSize=100,
            personFields='names,emailAddresses,urls',
            pageToken=page_token
        ).execute()

        connections = results.get('connections', [])
        non_trashed_connections = [contact for contact in connections if not contact.get('trashed', False)]
        all_connections.extend(non_trashed_connections)

        # Update the progress bar with the number of contacts fetched in this iteration
        progress.update(len(connections))

        page_token = results.get('nextPageToken')
        if not page_token:
            break
        if (len(all_connections) > LIMIT_CONTACTS) and LIMIT_CONTACTS != 0:
            break

    # Filter out trashed contacts
    progress.close()
    return non_trashed_connections

def download_and_store_image(image_url, contact_name, CONTACT_PHOTO_FOLDER):
    #print(f"Downloading and storing image for {contact_name} from {image_url}...")
    print(f"  retrieving image for {contact_name}:", end='')

    # Make sure the directory exists
    if not os.path.exists(CONTACT_PHOTO_FOLDER):
        os.makedirs(CONTACT_PHOTO_FOLDER)
    
    # Generate the file path
    file_extension = os.path.splitext(image_url)[1]
    safe_name = ''.join(e for e in contact_name if e.isalnum())  # Removing any characters that might not be safe for a filename
    image_path = os.path.join(CONTACT_PHOTO_FOLDER, f"{safe_name}{file_extension}")
    
    # Download and save the image
    urllib.request.urlretrieve(image_url, image_path)
    
    return image_path

def upload_image_to_google_contact(service, resource_name, image_path, max_retries=3):
    # Uploads the image from the provided path to the specified Google Contact.
    # Retry a maximum of max_retries times in case of errors.

    for retry in range(max_retries):
        try:
            # Read the image data
            with open(image_path, "rb") as image_file:
                image_data = image_file.read()

            # Encode the image data in base64
            image_base64 = base64.b64encode(image_data).decode("utf-8")

            # Create the request body
            request_body = {
                "photoBytes": image_base64,
                "personFields": "photos"
            }

            # Update the contact's photo
            service.people().updateContactPhoto(
                resourceName=resource_name,
                body=request_body
            ).execute()

            print(f"Upload successful.")
            return  # Exit the function on successful upload

        except googleapiclient.errors.HttpError as e:
            print(f"Error: {e}")
            if retry < max_retries - 1:
                # Retry after a short delay (e.g., 5 seconds) if not the final retry
                print(f"Retrying after {retry + 1} seconds...")
                time.sleep(retry + 1)
                continue
            else:
                print(f"Max retries reached. Upload failed.")
                break

def filter_contacts_with_missing_photos(contacts, service):
    """
    Filters contacts to include only those with missing photos.
    """
    contacts_with_missing_photos = []

    for contact in contacts:
        # Check if the contact has an existing photo
        existing_photos = contact.get("photos", [])
        if not existing_photos:
            contacts_with_missing_photos.append(contact)

    return contacts_with_missing_photos