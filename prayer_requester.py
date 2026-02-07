from mass_notifications import *

def check_for_prayer_requests():
    # Email account details
    USERNAME = "pessognellisa20@gmail.com"
    PASSWORD = "axyf rity yzjb hcdo" # Use an App Password
    IMAP_SERVER = "imap.gmail.com"
    DIRECTORY = "E:\prayer-partners\directory.xlsx"

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