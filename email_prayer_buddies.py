# email_prayer_buddies.py
from select_prayer_buddies import *
import smtplib
import ssl
from email.message import EmailMessage
from datetime import date
import tomllib
from pathlib import Path
import os
os.chdir(os.getcwd())

def weekly_prayer_buddies():
    # Define email sender and receiver
    with Path('config.toml').open("rb") as f:
        config_info = tomllib.load(f)
    sender_email = config_info['email']['username']
    password = config_info['email']['password']
    file = config_info['directory']['dir']

    random_pairs, names, name_to_email= random_prayer_partners(file)
    for i, pair in enumerate(random_pairs, 1):
        # Create the email message string
        if len(pair) > 2:
            message = "Hello "+ " ".join([name_to_email[pair[j]][1]+", and " if j == len(pair)-2 else name_to_email[pair[j]][1]+","  for j in range(0,len(pair))])
        else:
            message = "Hello "+ " ".join([name_to_email[pair[j]][1]+" and " if j == len(pair)-2 else name_to_email[pair[j]][1]+","  for j in range(0,len(pair))])
        
        for partner in pair:
            # Create the EmailMessage object
            msg = EmailMessage()
            msg.set_content(message+"\n"+"Congratulations! You have been selected as prayer buddies for the week of "+ date.today().strftime("%Y-%m-%d") +"!")
            msg['Subject'] = date.today().strftime("%Y-%m-%d")  + ": This week's prayer buddies!"
            msg['From'] = sender_email
            msg['To'] = name_to_email[partner][2] #receiver email

            # Define the SMTP server and port (for Gmail with implicit TLS/SSL)
            smtp_server = "smtp.gmail.com"
            port = 465  # For SSL

            # Create a secure SSL context
            context = ssl.create_default_context()

            # Try to log in to the server and send the email
            try:
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.send_message(msg)
                print("Email sent successfully!")
            except smtplib.SMTPException as e:
                print(f"Error: {e}")


# if __name__ == "__main__": 
#     if len(sys.argv)>1:
#         file = sys.argv[1]
#     weekly_prayer_buddies(file) #= "E:\prayer-partners\directory.xlsx"

weekly_prayer_buddies()