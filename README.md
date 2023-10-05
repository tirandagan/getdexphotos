## Overview

If you are using [getdex.com](https://www.getdex.com) to manage your contact and have established one-way sync to your google contact, this program will upload all the contact photos sotred with dex into google contacts. 

One sample use case: you might use dex to consolidate all your contacts across LinkedIn, your phone contacts, facebook, etc. Dex does a great job with this but you will end up with a mess on your phone mixing the clean/consolidated Dex contacts with your master contacts on your phone.

If you are using google to store your contacts (and sync to your iphone for instance) then here is a process I follow to get a super clean set of contacts assuming you already used the Merge and Fix feature in Dex to get yourself to single instances of each contact (caution advised!!!):

1. **Backup your contacts**: from your phone to icloud, export them from Google contacts - do everything possible to save what you have in case you need to revert!

2. **Disconnect dex one-way sync**: we will next be deleting our contacts on google and phone so we dont want them to resync back before we are ready

3. **Delete all your contacts**: I then delete all my contacts from my phone and from google contacts, leaving dex contacts intact. Sign in to google contacts to confirm the contact list is empty

4. **Reconnect Dex one-way sync**: to your google account. This might take an hour or more. I had 6600 contacts and it took nearly 3 hours to complete the sync. At the end I had all my clean contacts back in google. HOWEVER - dex does not port over the contact photos that it retrieved from various social accounts. We will do this separately using our Python app here, leveraging the dex API calls.

## Uimplemented feature: 
It will also store information about the contacts and their photos in a spreadsheet.

## How It Works
To learn how this program works, see the [the app operation document](docs/app-operation.md). Here is a sample execution:

![sample execution](docs/getdexphotos-execution.mp4)

# Getting Started

To configure the app, follow the instructions in [settings.md](docs/settings.md)
