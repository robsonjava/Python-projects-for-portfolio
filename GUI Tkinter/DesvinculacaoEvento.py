from logging import root
from multiprocessing import Event
import tkinter as tk
from tkinter import ttk

def log(event):
    print("Evento disparado...")

root = tk.Tk()
root.title("Estado Inicial")
root.geometry("600x400+500+200")

btn1 = ttk.Button(root, text="Exercutar")
btn1.bind("<Any-KeyPress>", log)
btn1.focus()
btn1.pack()
# Para desvincular
#btn1.unbind("<Any-KeyPress>")

btn2 = ttk.Button(
    root,
    text="Desvincular evento",
    command=lambda: btn1.unbind("<Any-KeyPress>")
)
btn2.pack()

btn3 = ttk.Button(
    root,
    text="Vincular evento",
    command=lambda: btn1.bind("<Any-KeyPress>", log)
)
btn3.pack()

root.mainloop()