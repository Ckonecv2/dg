import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def on_button_click():
    user_input = entry.get()
    if user_input.strip():
        label_output.config(text=f"Hello, {user_input}!")
    else:
        messagebox.showwarning("Input Error", "Please enter something in the text field.")

# Create the main window
root = tk.Tk()
root.title("Simple UI Example")
root.geometry("400x200")

# Create a label
label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
label.pack(pady=10)

# Create an entry widget
entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack(pady=5)

# Create a button
button = tk.Button(root, text="Submit", font=("Arial", 12), command=on_button_click)
button.pack(pady=10)

# Create a label to display output
label_output = tk.Label(root, text="", font=("Arial", 12), fg="green")
label_output.pack(pady=10)

# Start the GUI event loop
root.mainloop()
