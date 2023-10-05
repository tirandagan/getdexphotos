[home](../README.md) > app-operation.md

## How It Works

1. **Authentication**: The program starts by authenticating with Google services using OAuth 2.0. This step ensures that the program can access the user's Google Contacts and perform necessary actions.

2. **User Input**: The user is prompted to choose whether they want to retrieve all photos or only missing photos.
   - If the user selects "A" (all photos), the program fetches all contacts.
   - If the user selects "M" (missing photos), the program fetches all contacts and then filters out contacts with existing photos.

3. **Fetching Google Contacts**:
   - The program uses the Google People API to retrieve the user's Google Contacts.
   - It does this in batches, fetching 100 contacts at a time.
   - The progress is displayed using a progress bar, showing the number of contacts fetched.

4. **Iterating Through Contacts**:
   - For each contact retrieved, the program checks if there is a "Dex Contact Details" URL associated with the contact. This URL typically points to additional information about the contact, including their profile photo.
   - If no Dex URL is found, the contact is skipped, and the program continues to the next contact.

5. **Fetching Dex Contact Details**:
   - If a Dex URL is found, the program extracts the Dex Contact ID from the URL.
   - It uses the Dex API to fetch additional details about the contact, including the image URL.
   - If the Dex API call is successful, it retrieves the contact's image URL.

6. **Downloading and Storing Images**:
   - If the image URL is available, the program downloads the image from the URL.
   - The image is saved in a local directory named "contact photos." If the directory doesn't exist, it's created.
   - The image file is named based on the contact's name, and any special characters are removed from the name to ensure it's a valid filename.

7. **Uploading Images to Google Contacts**:
   - After downloading the image, the program uploads it to Google Contacts for the respective contact.
   - If the upload is successful, it prints a success message.

8. **Updating the Spreadsheet**:
   - The program keeps track of contact information in a spreadsheet named "photo inventory.xls." However, the actual update to the spreadsheet is not implemented in the provided code. You would need to implement this part according to your requirements.

9. **Error Handling**:
   - The program includes error handling to deal with various issues, such as missing Dex URLs, missing image URLs, and transient errors during image uploads to Google Contacts.
   - It retries image uploads a specified number of times before giving up.

10. **Completion**:
    - After processing all contacts, the program finishes, and you can view the uploaded images in Google Contacts.

## Customization

- You can customize the program by adjusting the number of retries for image uploads, the folder where images are stored, and the spreadsheet update logic to suit your specific needs.

## Dependencies

The program relies on several Python libraries, including:

- `google-auth-oauthlib`: For authentication with Google services.
- `google-api-python-client`: For interacting with the Google People API.
- `requests`: For making HTTP requests to the Dex API.
- `tqdm`: For displaying progress bars.
- `base64`: For encoding and decoding image data.
- `urllib`: For downloading images.
- `os`: For file and directory operations.
- `time`: For handling retries and delays.
- `xlrd` and `xlwt`: For reading and writing Excel spreadsheets. (Note: These are not included in the provided code, and you would need to install them separately if you want to update the spreadsheet.)

## Notes

- The provided code does not include the actual spreadsheet update logic, so you would need to implement that part separately if needed.
- The program gracefully handles various errors and retries image uploads to deal with transient issues.

Please let me know if you have any specific questions or if there's anything else you'd like to know about the program!
