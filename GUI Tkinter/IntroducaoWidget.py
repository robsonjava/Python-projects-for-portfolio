from logging import root
from multiprocessing import Event
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Estado Inicial")
root.geometry("600x400+500+200")

label1 = ttk.Label(
    root,
    text="Este é um label\nCurso de Python Tkinter",
    background="#33CCFF",
    foreground="red"
)
label1.pack()

root.mainloop()