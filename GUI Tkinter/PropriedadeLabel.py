from logging import root
from multiprocessing import Event
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Estado Inicial")
root.geometry("600x400+500+200")

# PROPRIEDADES DO LABEL
label1 = ttk.Label(
    root,
    text="Este é um label\nCurso de Python Tkinter",
    background="yellow",
    foreground="red",
    padding=20,
    width=25,
    justify="left", # RIGHT LEFT RIGHT
    anchor=tk.E #N S E W NE NW SE SW CENTER
)
label1.pack()

root.mainloop()