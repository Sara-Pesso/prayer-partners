import tkinter as tk

def get_entries():
    """Function to retrieve content from all entry boxes."""
    contents = []
    for entry in entries:
        contents.append(entry.get())
    print("Contents:", contents)

ws = tk.Tk()
ws.title("Multiple Entries Example")

# List to hold the Entry widgets
entries = []

# Create multiple entry widgets using a for loop
for i in range(5):
    # Create a Label for each entry
    tk.Label(ws, text=f"Entry {i+1}:").grid(row=i, column=0, padx=10, pady=5)
    
    # Create the Entry widget
    e = tk.Entry(ws)
    e.grid(row=i, column=1, padx=10, pady=5)
    
    # Append the entry widget reference to the list
    entries.append(e)

# Add a button to retrieve the contents
button = tk.Button(ws, text="Get Values", command=get_entries)
button.grid(row=5, column=0, columnspan=2, pady=10)

ws.mainloop()
