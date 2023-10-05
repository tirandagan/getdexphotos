[home](../README.md) > settings.md

# Setting Up the `getdexphotos` Program

This guide will walk you through the initial setup of the `getdexphotos` program, including the following steps:

1. Creating the `token.json` File for Google OAuth 2.0 Authentication.
2. Configuring OAuth 2.0 in Your Google Developer Console.
3. Obtaining an API Key for Dex and Storing It in `dex-api.txt`.

## Prerequisites

Before you begin, make sure you have the following:

- Python 3.x installed on your computer.
- Pip (Python package installer) installed.
- A Google account with access to Google Contacts.

## 1. Creating the `token.json` File for Google OAuth 2.0 Authentication

To access Google Contacts, the `getdexphotos` program uses OAuth 2.0 authentication. You need to create a `token.json` file to store your authentication credentials. Follow these steps:

### Step 1: Create a Project in the Google Developer Console

1. Go to the [Google Developer Console](https://console.developers.google.com/).
2. Click on the project dropdown and select "New Project."
3. Give your project a name and click "Create."

### Step 2: Enable the Google People API

1. In the left navigation pane, click on "APIs & Services" > "Library."
2. Search for "Google People API" and click on it.
3. Click the "Enable" button.

### Step 3: Create OAuth 2.0 Credentials

1. In the left navigation pane, click on "APIs & Services" > "Credentials."
2. Click the "Create Credentials" dropdown and select "OAuth client ID."
3. Select "Desktop app" as the application type.
4. Give your OAuth client a name.
5. Click "Create."

### Step 4: Download JSON Credentials

1. Click the "Download" button next to your newly created OAuth 2.0 client.
2. Save the JSON file as `credentials.json` in the same directory as your `getdexphotos` program.

## 2. Configuring OAuth 2.0 in Your Google Developer Console

To allow the `getdexphotos` program to access your Google Contacts, you'll need to configure the OAuth 2.0 consent screen in your Google Developer Console:

### Step 1: Configure OAuth Consent Screen

1. In the Google Developer Console, go to "APIs & Services" > "OAuth consent screen."
2. Select "External" for the user type and click "Create."
3. Fill in the required fields:
   - **App name**: Enter a name for your app.
   - **User support email**: Enter your email address.
   - **Developer contact information**: Enter your email address.
   - **Scopes for Google APIs**: Leave this blank.
   - **Authorized domains**: Leave this blank.
   - **Application Homepage link**: Leave this blank.
   - **Application Privacy Policy link**: Leave this blank.
   - **Application Terms of Service link**: Leave this blank.
4. Click "Save and Continue."
5. Add test users if necessary (skip if you don't need this).
6. Click "Save and Continue."
7. Review your settings and click "Back to Dashboard."

### Step 2: Get Your OAuth Client ID

1. In the Google Developer Console, go to "APIs & Services" > "Credentials."
2. Under "OAuth 2.0 Client IDs," locate your OAuth client ID and click on it.
3. Make note of the "Client ID" value; you'll need it later when running the `getdexphotos` program.

## 3. Obtaining an API Key for Dex and Storing It in `dex-api.txt`

The `getdexphotos` program requires an API key for Dex to access Dex API services. Follow these steps:

### Step 1: Obtain an API Key from Dex

1. Visit the [Dex Developer Portal](https://developer.getdex.com/).
2. Sign in or create an account.
3. Create a new Dex API project.
4. Generate an API key for your project.

### Step 2: Store the API Key in `dex-api.txt`

1. In the `getdexphotos` program directory, create a new file named `dex-api.txt`.
2. Open `dex-api.txt` and paste your Dex API key into the file.
3. Save and close the file.

## Program Setup Complete

With the `token.json` file, OAuth 2.0 configuration, and Dex API key in place, you've completed the initial setup of the `getdexphotos` program. You are now ready to run the program to retrieve and upload contact photos.

To run the program, open your command prompt or terminal, navigate to the `getdexphotos` program directory, and execute the program using the following command:

