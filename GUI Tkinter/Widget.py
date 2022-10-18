from logging import root
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Estado Inicial")
root.geometry("600x400+500+200")

# MODO CLASSICO
tk.Label(root, text="Label Classico").pack()

# MODO TTK
ttk.Label(root, text="Label Tematico").pack()

tk.Button(root, text="Label Classico").pack()
ttk.Button(root, text="Label Tematico").pack()


root.mainloop()