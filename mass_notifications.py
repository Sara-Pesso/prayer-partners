import imaplib
import email
from email.header import decode_header
from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta, timezone
from directory import *
import smtplib
import ssl
from email.message import EmailMessage
from email_distro import *
from imap_tools import MailBox

def search_email_for_prayer_requests(username, password, imap_server, search_string, new_mailbox):
    uids = []
    try:
        # Connect to the IMAP server
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(username, password)
        
        # Select the inbox
        mail.select("inbox")

        SEARCH_QUERY = f'(BODY "{search_string}")'
        status, messages = mail.search(None, SEARCH_QUERY)
        # status, messages = mail.search(None, '#prayer-request', f'newer_than:60m {search_string}')
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

                    # Move email to folder, out of inbox
                    result, data = mail.fetch(email_id, '(UID BODY[HEADER.FIELDS (SUBJECT)])')
                    uid = data[0][0].decode().split()[2] 
                    uids.append(uid)
                    

        mail.logout()

        # Move email to folder, out of inbox
        remove_prayer_request(username, password, imap_server, uids, new_mailbox)

        return emails_with_string

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def remove_prayer_request(username, password, imap_server, uids, new_mailbox):
    with MailBox(imap_server).login(username, password) as mailbox:
        for uid in uids:
            # MOVE all messages from current folder to folder2, *in bulk (implicit creation of uid list)
            mailbox.move(uid, new_mailbox)

            # DELETE all messages from current folder, *in bulk (explicit creation of uid list)
            mailbox.delete(uid)
    return []
