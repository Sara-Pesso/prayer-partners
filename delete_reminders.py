import json
import os
os.chdir(r"E:\prayer-partners")

def display_reminders_for_day(weekday):
    json_file = os.path.join("weekly_reminder_json", weekday.lower() +"_reminders.json") 

    with open(json_file, 'r') as file:
        reminder_data = json.load(file)
    reminders = reminder_data["reminders"]

    reminder_titles = []
    for reminder in reminders:
        EMAIL_SUBJECT = reminder['details']['subject']
        reminder_titles.append(EMAIL_SUBJECT)

    return reminder_titles

# display_reminders_for_day("FRIDAY")

def delete_reminder_from_json(reminder_title, weekday):
    json_file = os.path.join("weekly_reminder_json", weekday.lower() +"_reminders.json") 

    with open(json_file, 'r') as file:
        reminder_data = json.load(file)

    for i in range(len(reminder_data['reminders'])-1,0, -1):
        if reminder_data['reminders'][i]['reminder_title'] == reminder_title:
            del reminder_data['reminders'][i]

    with open(json_file, 'w') as file:
            json.dump(reminder_data, file, indent=4)

    return []

# delete_reminder_from_json("Reminder: 2026-02-13 quick test of the weekly reminder search", "FRIDAY")

# display_reminders_for_day("FRIDAY")