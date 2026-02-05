from select_prayer_buddies import *
import smtplib
import ssl
from email.message import EmailMessage
from datetime import date
from directory import *
import sys

# Email account details
USERNAME = "pessognellisa20@gmail.com"
PASSWORD = "axyf rity yzjb hcdo" # Use an App Password
IMAP_SERVER = "imap.gmail.com"

#send to email_distro
names, name_to_email, email_distro = get_directory("E:\prayer-partners\directory.xlsx")
for email_address in email_distro:
    # Create the EmailMessage object
    msg = EmailMessage()
    msg.set_content("")
    msg['Subject'] = "Prayer Reminder: " + date.today().strftime("%Y-%m-%d")
    msg['From'] = USERNAME
    msg['To'] = email_address #receiver email

    # Define the SMTP server and port (for Gmail with implicit TLS/SSL)
    smtp_server = "smtp.gmail.com"
    port = 465  # For SSL

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to the server and send the email
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)
        print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print(f"Error: {e}")