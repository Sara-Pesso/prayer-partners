from mass_notifications import *
import json
import re
import os
os.chdir(r"E:\prayer-partners")

def check_for_weekly_reminders():
    # Email account details
    USERNAME = "pessognellisa20@gmail.com"
    PASSWORD = "axyf rity yzjb hcdo" # Use an App Password
    IMAP_SERVER = "imap.gmail.com"
    DIRECTORY = "E:\prayer-partners\directory.xlsx"

    # Run the search
    # The string to search for and the time to search for 
    SEARCH_STRING = "#weekly-reminder"
    NEW_MAILBOX =  'Weekly Reminders'
    
    day_hashtags = [        
        "#Monday",
        "#Tuesday",
        "#Wednesday",
        "#Thursday",
        "#Friday",
        "#Saturday",
        "#Sunday"
        ]

    found_emails = search_email_for_prayer_requests(USERNAME, PASSWORD, IMAP_SERVER, SEARCH_STRING, NEW_MAILBOX)
    for reminder in found_emails:
        MESSAGE_SUBJECT = "Reminder: " + " " + reminder['Subject']
        MESSAGE_CONTENT = reminder['Body']
        SENDER = reminder['From']
        DAYOFWEEK = None
        for day in day_hashtags:
            if day in MESSAGE_CONTENT:
                DAYOFWEEK = re.sub(r'#(\S+)', r'\1', day)

        if DAYOFWEEK == None:
            DAYOFWEEK = datetime.date.today().strftime("%A")


        # add reminder subject/content to JSON for correct day
        json_file = os.path.join("./weekly_reminder_json/",DAYOFWEEK.lower() + "_reminders.json")
        print(json_file)
        with open(json_file, 'r') as file:
            data = json.load(file)

        new_reminder = {
            "reminder_title": MESSAGE_SUBJECT,
            "details":{
                "subject": MESSAGE_SUBJECT,
                "content": MESSAGE_CONTENT
            }
        }

        data["reminders"].append(new_reminder)
        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4) 
        
        
        
check_for_weekly_reminders()


