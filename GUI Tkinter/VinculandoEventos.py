from logging import root
import tkinter as tk
from tkinter import ttk


def log(event):
    print(event)

root = tk.Tk()
root.title("Estado Inicial")
root.geometry("600x400+500+200")

root.bind("<Any-KeyPress>", log)

root.mainloop()