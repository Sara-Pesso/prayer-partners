from mass_notifications import *
import json

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

    found_emails = search_email_for_prayer_requests(USERNAME, PASSWORD, IMAP_SERVER, SEARCH_STRING, NEW_MAILBOX)
    for request in found_emails:
        MESSAGE_SUBJECT = "Reminder: " + date.today().strftime("%Y-%m-%d")+ " " + request['Subject']
        MESSAGE_CONTENT = request['Body']
        # add reminder subject/content to JSON for correct day
        # send_mass_email(MESSAGE_SUBJECT, MESSAGE_CONTENT, USERNAME, PASSWORD, DIRECTORY)
        
# check_for_weekly_reminders()

with open(r'E:\prayer-partners\friday_reminders.json', 'r') as file:
    data = json.load(file)
new_entry = {
    "reminder_title": "example2",
    "details":{
        "subject":"test subject",
        "content":"make up some content!"
    }
}
data["reminders"].append(new_entry)
with open(r'E:\prayer-partners\friday_reminders.json', 'w') as file:
    json.dump(data, file, indent=4) 
