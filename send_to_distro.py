import imaplib
import email
from email.header import decode_header
from bs4 import BeautifulSoup
from datetime import datetime
import win32com.client

# Email account details
USERNAME = "pessognellisa20@gmail.com"
PASSWORD = "axyf rity yzjb hcdo" # Use an App Password
IMAP_SERVER = "imap.gmail.com"

# The string to search for and the time to search for 
SEARCH_STRING = "#prayer-request"
TARGET_DATETIME = datetime(2025, 1, 15, 10, 30, 0)
FILTER_TIME_STR = TARGET_DATETIME.strftime('%Y-%m-%d %H:%M')

def search_emails(username, password, imap_server, search_string):
    try:
        # Connect to the IMAP server
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(username, password)
        
        # Select the inbox
        mail.select("inbox")
    
        status, messages = mail.search(None, f'(BODY "{search_string}")')
        
        email_ids = messages[0].split()

        print(f"Found {len(email_ids)} emails in inbox. Filtering for '{search_string}'...")

        emails_with_string = []

        for email_id in email_ids:
            # Fetch the email data (RFC822 is the full message)
            status, msg_data = mail.fetch(email_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        subject = subject.decode()
                    
                    # Check body content
                    body = ""
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get_content_disposition())
                            try:
                                body = part.get_payload(decode=True).decode()
                            except:
                                pass
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                body = BeautifulSoup(body, "html.parser").get_text() 
                                break
                    else:
                        body = msg.get_payload(decode=True).decode()
                        body = BeautifulSoup(body, "html.parser").get_text()

                    # Check if the search string is in the subject or body
                    if search_string.lower() in subject.lower() or search_string.lower() in body.lower():
                        emails_with_string.append({"Subject": subject, "From": msg.get("From"), "Date": msg.get("Date"), "Body": body})
                        
        mail.logout()
        return emails_with_string

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Run the search
found_emails = search_emails(USERNAME, PASSWORD, IMAP_SERVER, SEARCH_STRING)
print(found_emails)
