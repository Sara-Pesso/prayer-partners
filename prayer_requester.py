from mass_notifications import *
import tomllib
from pathlib import Path
import os
os.chdir(os.getcwd())

def check_for_prayer_requests():
    # Email account details
    with Path('config.toml').open("rb") as f:
        config_info = tomllib.load(f)
    USERNAME = config_info['email']['username']
    PASSWORD = config_info['email']['password']
    IMAP_SERVER = "imap.gmail.com"
    DIRECTORY = config_info['directory']['dir']

    # Run the search
    # The string to search for and the time to search for 
    SEARCH_STRING = "#prayer-request"
    NEW_MAILBOX =  'Prayer Requests'

    found_emails = search_email_for_prayer_requests(USERNAME, PASSWORD, IMAP_SERVER, SEARCH_STRING, NEW_MAILBOX)
    for request in found_emails:
        MESSAGE_SUBJECT = "Prayer Request: " + date.today().strftime("%Y-%m-%d")+ " " + request['Subject']
        MESSAGE_CONTENT = request['Body']
        send_mass_email(MESSAGE_SUBJECT, MESSAGE_CONTENT, USERNAME, PASSWORD, DIRECTORY)
        
check_for_prayer_requests()