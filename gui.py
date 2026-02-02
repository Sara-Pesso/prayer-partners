import tkinter as tk
from tkinter import scrolledtext 
from secret_santa import *


def secret_santa_outputs(output_widget):
    # Generate the list of items
    secret_santa_list = secret_santa_generator(names, spouses) # names and spouses from secret_santa.py

    # Clear previous content in the Text widget
    output_widget.config(state="normal") # Make the widget editable temporarily
    output_widget.delete('1.0', tk.END)  

    # Insert each item from the list into the Text widget
    for item in secret_santa_list:
        output_widget.insert(tk.END, item + "\n") # Insert at the end, followed by a newline

    # Make the widget read-only again to prevent user editing
    output_widget.config(state="disabled")

def display_spouse_dict(spouses_list_widget):
    # Check for new spouse pairs!!!!
    spouse1 = spouse_name1_box.get()
    spouse2 = spouse_name2_box.get()

    if spouse1 and spouse2:
        spouses.update({spouse1:spouse2})
        # Empty the textboxes
        spouse_name1_box.delete(0, tk.END)
        spouse_name2_box.delete(0, tk.END)

    # Clear previous content in the Text widget
    spouses_list_widget.config(state="normal") # Make the widget editable temporarily
    spouses_list_widget.delete('1.0', tk.END) 
    
    for key, value in spouses.items():
        spouses_list_widget.insert(tk.END, f"{key},{value}" + "\n")

    # Make the widget read-only again to prevent user editing
    spouses_list_widget.config(state="disabled")


def display_all_names(names_text_widget):
    # Check for added names
    new_name = add_name_box.get()
    if new_name:
        names.append(new_name)
        # Empty the textboxes
        add_name_box.delete(0, tk.END)

    # Display all names in santa draw
    names_text_widget.config(state="normal") # Make the widget editable temporarily
    names_text_widget.delete('1.0', tk.END)
    for name in names:
        names_text_widget.insert(tk.END, name + "\n")
        
    # Make the widget read-only again to prevent user editing
    names_text_widget.config(state="disabled")


# --- Main Tkinter Application ---
root = tk.Tk()
root.title("Secret Santa Generator")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window geometry to match the screen size
root.geometry(f"{screen_width}x{screen_height}+0+0")

### Displaying ALL names of people in secret santa pool, regardless of spousal relationship
names_textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", height=10, padx=5, pady=5)
names_textbox.pack(pady=10, fill=tk.BOTH, expand=True)

add_name_box = tk.Entry(root, width=30)
add_name_box.pack(pady=10)

display_button = tk.Button(root, text="Display/Add Names", command=lambda: display_all_names(names_textbox))
display_button.pack(pady=10)

### Displaying the names and spouse pairinings
spouse_textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", height=10, padx=5, pady=5)
spouse_textbox.pack(pady=10, fill=tk.BOTH, expand=True)

spouse_name1_box = tk.Entry(root, width=30)
spouse_name1_box.pack(pady=10)

spouse_name2_box = tk.Entry(root, width=30)
spouse_name2_box.pack(pady=10)

display_button = tk.Button(root, text="Display/Add Spouses", command=lambda: display_spouse_dict(spouse_textbox))
display_button.pack(pady=10)

### OUTPUT!
# Create a Button that triggers the secret santa generator function function
display_button = tk.Button(root, text="DRAW NAMES!", command=lambda: secret_santa_outputs(output_area))
display_button.pack(pady=10)

# Create a ScrolledText widget to display the secret santa pairings
output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", height=10, padx=5, pady=5)
output_area.pack(pady=10, fill=tk.BOTH, expand=True)

# Start Tkinter loop
root.mainloop()