import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Login")
root.geometry("250x100+750+400")

# cofigurar o grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# username
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

password_label = ttk.Entry(root, show="*")
password_label.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)



root.mainloop()
