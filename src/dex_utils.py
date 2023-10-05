DEX_API_BASE_URL = "https://api.getdex.com/api/rest"

import requests

def extract_dex_id_from_url(url):
    """
    Extracts and returns the Dex Contact ID from the provided URL.
    """
    return url.split("/")[-1]

def fetch_dex_contact_by_id(dex_contact_id, DEX_API_KEY):
    headers = {
        "Content-Type": "application/json",
        "x-hasura-dex-api-key": DEX_API_KEY
    }
    
    # Construct the full URL using the base URL
    url = f"{DEX_API_BASE_URL}/contacts/{dex_contact_id}"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error fetching contact from Dex with ID {dex_contact_id}. Status code: {response.status_code}")
        return None

    contact_data = response.json()
    
    # Check if the contact_data contains the expected fields
    if "contacts" in contact_data and len(contact_data["contacts"]) > 0:
        return contact_data["contacts"][0]
    else:
        return None


def update_spreadsheet(contact_name, dex_id, image_url):
    # print(f"Updating spreadsheet with details: {contact_name}, {dex_id}, {image_url}...")
    # Update the spreadsheet with the necessary details
    pass

def get_image_url_from_dex(dex_contact_id):
    """
    Fetches the contact details from Dex using the provided Dex Contact ID and returns the image URL.
    """
    dex_contact = fetch_dex_contact_by_id(dex_contact_id)
    return dex_contact.get("image_url")
