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

        self.label1 = "Email Username:"
        self.label = tk.Label(root, textvariable=self.label1)
        self.label.pack(pady=5)
        
        self.entry_var = tk.StringVar()
        self.entry_var.set(USERNAME) # Dispaly current toml entry in corresponding textbox

        self.entry_widget = tk.Entry(root, textvariable=self.entry_var, width=30)
        self.entry_widget.pack(pady=10)

        self.button = tk.Button(root, text="Reset Variable", command=self.update_toml_with_new_value)
        self.button.pack(pady=5)

        

    def update_toml_with_new_value(self):
        current_value = self.entry_var.get()
        print(f"The current value of the variable is: {current_value}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()