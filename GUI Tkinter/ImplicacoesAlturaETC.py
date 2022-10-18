from ctypes import sizeof
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Estado Inicial")
root.geometry("600x400+650+300")


label1 = ttk.Label(
    root,
    text="123456789",
    font="Arial 20",
    borderwidth=1, 
    relief="groove", #"groove","ridge","sunken","raised","flat","solid"
    #width=5,
    wraplength=50
    
)
label1.pack()

label2 = tk.Label(
    root,
    text="123456789",
    font="Arial 20",
    borderwidth=1, #bd
    relief="solid", #"groove","ridge","sunken","raised","flat","solid"
    width=5,
    height=2
)
label2.pack()

root.mainloop()