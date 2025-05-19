import tkinter as tk
import subprocess

def on_button_click():
    user_id = entry2.get()
    password = entry3.get()
    if user_id == "kamlesh" and password == "1234":
        label4.config(text="Authentication Successful!")
        subprocess.run(["python", "version2.menu.py"])
    elif user_id == "deeraj" and password == "abc":
        label4.config(text="Authentication Successful!")
        subprocess.run(["python", "version2.menu.py"])
    else:
        label4.config(text="Invalid Credentials")

# Create Tkinter window
window = tk.Tk()
window.title("Enomy Finances")
window.geometry("500x400")

# Labels and Entry widgets for user authentication
label1 = tk.Label(window, text="Authentication System:")
label1.grid(row=0, column=0, columnspan=2, pady=10)

label2 = tk.Label(window, text="Enter ID:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

label3 = tk.Label(window, text="Enter Password:")
label3.grid(row=2, column=0)
entry3 = tk.Entry(window, show="*")  # Password entry, characters are hidden
entry3.grid(row=2, column=1)

label4 = tk.Label(window, text="Log In Unsuccessful")
label4.grid(row=3, column=0, columnspan=2)

# Login button
button = tk.Button(window, text="Login", command=on_button_click)
button.grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()
