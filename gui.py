import tkinter as tk
import tomllib
import toml
from pathlib import Path
import subprocess
import os
os.chdir(os.getcwd())
# Grab current toml entries
with Path('config.toml').open("rb") as f:
    config_info = tomllib.load(f)
USERNAME = config_info['email']['username']
PASSWORD = config_info['email']['password']
DIR = config_info['directory']['dir']
AUTH = config_info['authorized-user']['username']
APP_DIR = config_info['paths']['dist'] 

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("N2H Notification App")
        self.variables = {}

        ## Update config toml functions
        self.config_toml_entry_box("Email Username:", USERNAME,row=0)
        self.config_toml_entry_box("Email App Password:", PASSWORD,row=1)
        self.config_toml_entry_box("Authorized User:", AUTH,row=2)
        self.config_toml_entry_box("Email Distribution Directory:", DIR,row=3)
        self.config_toml_entry_box("Application Directory:", APP_DIR,row=4)
        self.update_button = tk.Button(root, text="Update", command=self.update_toml_with_new_value)
        self.update_button.grid(row=5,column=1,pady=5)

        ## force prayer buddy naem drawing & email
        self.prayer_buddy_btn = tk.Button(root, text="Redraw Weekly Prayer Buddies", command=self.force_prayer_buddies)
        self.prayer_buddy_btn.grid(row=6,column=1,pady=5)

        ## force sending out today's weekday daily reminders
        self.send_weeklies_btn = tk.Button(root, text = "Send Today's Reminders", command=self.force_send_reminders)
        self.send_weeklies_btn.grid(row=7,column=1,pady=5)

        ## for prayer request search and send out
        self.check_prayer_reqs_btn = tk.Button(root, text = "Check for Prayer Requests", command=self.force_check_prayer_reqs)
        self.check_prayer_reqs_btn.grid(row=8,column=1,pady=5)

    #TODO change all the paths to be from the toml info, not hard coded!!! # Path(APP_DIR,"schedule_prayer_request_check.exe")

    def force_check_prayer_reqs(self):
        subprocess.Popen([Path(APP_DIR,"schedule_prayer_request_check.exe"), Path(APP_DIR,"prayer_requester.exe"), DIR])
        print("Check for prayer requests complete")

    def force_send_reminders(self):
        subprocess.Popen([Path(APP_DIR,"email_weekly_reminders.exe")])
        subprocess.Popen([Path(APP_DIR,'schedule_weekly_reminder_sender.exe'), Path(APP_DIR,"email_weekly_reminders.exe"), DIR])
        print("Send weekly reminders complete")

    def force_prayer_buddies(self):
        subprocess.Popen([Path(APP_DIR,"email_prayer_buddies.exe")])
        subprocess.Popen([Path(APP_DIR,'schedule_prayer_buddies.exe'), Path(APP_DIR,"email_prayer_buddies.exe"), DIR])
        print("Prayer buddy redraw complete")
        
    def config_toml_entry_box(self, toml_entry, CONFIG_ENTRY, row):
        self.label = tk.Label(root, text=toml_entry)
        self.label.grid(row= row, column=0, pady=5)

        self.variables[toml_entry] = tk.StringVar()
        self.variables[toml_entry].set(CONFIG_ENTRY) # Dispaly current toml entry in corresponding textbox

        self.entry_widget = tk.Entry(root, textvariable=self.variables[toml_entry], width=30)
        self.entry_widget.grid(row=row,column=1,pady=10)


    def update_toml_with_new_value(self):
        with open('config.toml','r') as f:
            config_data = toml.load(f)

        config_data['email']['username'] = self.variables["Email Username:"].get()
        config_data['email']['password'] = self.variables["Email App Password:"].get()
        config_data['directory']['dir'] = self.variables["Email Distribution Directory:"].get()
        config_data['authorized-user']['username'] = self.variables["Authorized User:"].get()

        with open('config.toml','w') as f:
            toml.dump(config_data,f)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()