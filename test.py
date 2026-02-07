import json
import os
os.chdir(r"E:\prayer-partners")
with open(r'friday_reminders.json', 'r') as file:
    data = json.load(file)
