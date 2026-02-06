import smtplib
import ssl
from email.message import EmailMessage

def compose_email(message_subject, message_content, username, password, recipient_email):
    # Create the EmailMessage object
    msg = EmailMessage()
    msg.set_content(message_content)
    msg['Subject'] = message_subject #"Prayer Reminder: " + date.today().strftime("%Y-%m-%d")
    msg['From'] = username
    msg['To'] = recipient_email #receiver email

    # Define the SMTP server and port (for Gmail with implicit TLS/SSL)
    smtp_server = "smtp.gmail.com"
    port = 465  # For SSL

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to the server and send the email
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(username, password)
            server.send_message(msg)
        print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print(f"Error: {e}")


# Email account details
from directory import *
USERNAME = "pessognellisa20@gmail.com"
PASSWORD = "axyf rity yzjb hcdo" # Use an App Password
def email_composer(message_content, message_subject, username, password, distro_xlsx):
    names, name_to_email, email_distro = get_directory(distro_xlsx) #"E:\prayer-partners\directory.xlsx"
    for email_address in email_distro:
        compose_email(message_subject, message_content, username, password, email_address)

if __name__ == "__main__":
    email_composer(message_content="TEST EMAIL", message_subject="TEST EMAIL", username=USERNAME, password=PASSWORD, distro_xlsx="E:\prayer-partners\directory.xlsx")