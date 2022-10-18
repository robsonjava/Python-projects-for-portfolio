from ctypes import sizeof
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Estado Inicial")
root.geometry("600x400+650+300")


label1 = ttk.Label(
    root,
    text="Python é vida!",
    font="Arial 20",
    borderwidth=10, 
    relief="groove" #"groove","ridge","sunken","raised","flat","solid"
)
label1.pack()

label2 = tk.Label(
    root,
    text="Python é lindo!",
    font="Arial 20",
    borderwidth=10, #bd
    relief="solid" #"groove","ridge","sunken","raised","flat","solid"
)
label2.pack()

root.mainloop()