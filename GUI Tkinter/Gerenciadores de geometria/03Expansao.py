import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Entry Widget")
root.geometry("600x400+650+300")

# box 1
box1 = tk.Label(
    root,
    text="Box-1",
    bg="green",
    fg="white"
)

box1.pack(
    ipadx=10,
    ipady=10,
    # Preenchimento em raio
    fill="y", # "x", "y", "buth"
    expand=True
)

# box 2
box2 = tk.Label(
    root,
    text="Box-2",
    bg="red",
    fg="white"
)

box2.pack(
    ipadx=10,
    ipady=10,
    fill="x",
    expand=True
)

root.mainloop()