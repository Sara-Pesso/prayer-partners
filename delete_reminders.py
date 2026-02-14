import json
import os
os.chdir(r"E:\prayer-partners")

def delete_reminder_from_json(weekday):
    json_file = os.path.join("weekly_reminder_json", weekday.lower() +"_reminders.json") 
    print(json_file)

    with open(json_file, 'r') as file:
        reminder_data = json.load(file)
    reminders = reminder_data["reminders"]
    for reminder in reminders:
        EMAIL_SUBJECT = reminder['details']['subject']
        EMAIL_CONTENT = reminder['details']['content']
        print(EMAIL_SUBJECT)

    return []

delete_reminder_from_json("FRIDAY")