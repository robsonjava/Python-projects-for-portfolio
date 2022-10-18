import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400")

ttk.Label(
    root,
    text="Label 1",
    font="Arial 16"
).pack()

# SEPARADOR
separador = ttk.Separator(root, orient="horizontal")
separador.pack(fill="x")

ttk.Label(
    root,
    text="Label 2",
    font="Arial 16"
).pack()


root.mainloop()