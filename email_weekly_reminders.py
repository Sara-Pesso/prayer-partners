from mass_notifications import *
import datetime
import json
import os
os.chdir(r"E:\prayer-partners")

def send_weekly_reminders_each_day():
    # Email account details
    USERNAME = "pessognellisa20@gmail.com"
    PASSWORD = "axyf rity yzjb hcdo" # Use an App Password
    IMAP_SERVER = "imap.gmail.com"
    DIRECTORY = "E:\prayer-partners\directory.xlsx"
    today = datetime.datetime.now().strftime("%A")
    json_file = os.path.join("weekly_reminder_json", today.lower() +"_reminders.json") 
    print(json_file)

    # E:\prayer-partners\weekly_reminder_json

    ## Grab the reminders stored for whatever weekday it is
    with open(json_file, 'r') as file:
        reminder_data = json.load(file)
    reminders = reminder_data["reminders"]
    for reminder in reminders:
        EMAIL_SUBJECT = reminder['details']['subject']
        EMAIL_CONTENT = reminder['details']['content']

        send_mass_email(EMAIL_SUBJECT, EMAIL_CONTENT, USERNAME, PASSWORD, DIRECTORY)
    return []

send_weekly_reminders_each_day()