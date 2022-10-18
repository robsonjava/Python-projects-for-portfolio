import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Python Tkinter")

frame1 = ttk.Frame(
    root,
    width=600,
    height=300,
    borderwidth=5,
    relief="sunken",
    padding=(10,50) #(left, top, right, bottom)

)
frame1.pack()

label1 = ttk.Label(
    frame1,
    text="Label 1",
    background="green"
)
label1.pack()

root.mainloop()