import tkinter as tk
import tomllib
import toml
from pathlib import Path
import os
os.chdir(r"E:\prayer-partners")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("N2H Notification App")
        self.variables = {}

        # Grab current toml entries
        with Path('config.toml').open("rb") as f:
            config_info = tomllib.load(f)
        USERNAME = config_info['email']['username']
        PASSWORD = config_info['email']['password']
        DIR = config_info['directory']['dir']
        AUTH = config_info['authorized-user']['username']

        self.config_toml_entry_box("Email Username:", USERNAME,row=0)
        self.config_toml_entry_box("Email App Password:", PASSWORD,row=1)
        self.config_toml_entry_box("Authorized User:", AUTH,row=2)
        self.config_toml_entry_box("Email Distribution Directory:", DIR,row=3)
        self.button = tk.Button(root, text="Update", command=self.update_toml_with_new_value)
        self.button.grid(row=4,column=1,pady=5)
        
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