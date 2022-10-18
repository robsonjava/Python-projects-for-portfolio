import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400")

langs = ('Java','C#', 'C', 'C++', 'Python', 'Go', 'JavaScript')

langs_var = tk.StringVar(value=langs)

listbox = tk.Listbox(
    root,
    listvariable=langs_var,
    height=6,
    font="Arial 16",
    selectmode="browse" # extended
)
listbox.pack()



root.mainloop()