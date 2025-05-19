import tkinter as tk
import csv
import subprocess

def cv():
    subprocess.run(["python", "version3.currencyconv.py"])

def ip():
    subprocess.run(["python", "version4.sav&invest.py"])

def save_user_data():
    name = name_entry.get()
    email = email_entry.get()
    contact_number = contact_entry.get()

    with open('user_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, contact_number])

    # Clear the entry fields after saving
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)

    # Optional: Display a message to the user after saving
    status_label.config(text="User data saved successfully!")

# Create the main window
window = tk.Tk()
window.title("Enomy Finances")
window.geometry("400x200")

# Create and place labels and entry widgets for user input
name_label = tk.Label(window, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=5)

email_label = tk.Label(window, text="Email:")
email_label.grid(row=1, column=0, padx=10, pady=5)
email_entry = tk.Entry(window)
email_entry.grid(row=1, column=1, padx=10, pady=5)

contact_label = tk.Label(window, text="Contact Number:")
contact_label.grid(row=2, column=0, padx=10, pady=5)
contact_entry = tk.Entry(window)
contact_entry.grid(row=2, column=1, padx=10, pady=5)

# Button to save user data
save_button = tk.Button(window, text="Save User Data", command=save_user_data)
save_button.grid(row=3, column=1, pady=10)

# Optional: Label to display status message
status_label = tk.Label(window, text="")
status_label.grid(row=5, column=1)

# Buttons for other functionalities
button1 = tk.Button(window, text="Currency Conversion", command=cv)
button1.grid(row=6, column=1, padx=10, pady=2)

button2 = tk.Button(window, text="Saving & Investment", command=ip)
button2.grid(row=7, column=1, padx=10, pady=5)

# Start the main loop
window.mainloop()
