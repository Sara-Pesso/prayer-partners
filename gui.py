import tkinter as tk
import tomllib
from pathlib import Path
import os
os.chdir(r"E:\prayer-partners")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("N2H Notification App")

        # Grab current toml entries
        with Path('config.toml').open("rb") as f:
            config_info = tomllib.load(f)
        USERNAME = config_info['email']['username']
        PASSWORD = config_info['email']['password']
        DIR = config_info['directory']['dir']

        self.config_toml_entry_box("Email Username:", USERNAME)
        self.config_toml_entry_box("Email App Passowrd:", PASSWORD)
        

    def config_toml_entry_box(self, toml_entry, CONFIG_ENTRY):
        self.label = tk.Label(root, text=toml_entry)
        self.label.grid(row= 0, column=0, pady=5)

        self.entry_var = tk.StringVar()
        self.entry_var.set(CONFIG_ENTRY) # Dispaly current toml entry in corresponding textbox

        self.entry_widget = tk.Entry(root, textvariable=self.entry_var, width=30)
        self.entry_widget.grid(row=0,column=1,pady=10)

        self.button = tk.Button(root, text="Update", command=self.update_toml_with_new_value)
        self.button.grid(row=0,column=2,pady=5)
        return []
     
    def update_toml_with_new_value(self):
        current_value = self.entry_var.get()
        print(f"The current value of the variable is: {current_value}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()