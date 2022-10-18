from logging import root
import tkinter as tk
from tkinter import ttk

#def button_clicked():
    #root.config(background="red")
    #print("Botão clicado!")

def select(arg):
    root.config(background=arg)

root = tk.Tk()
root.title("Estado Inicial")
root.geometry("600x400+500+200")


btn1 = ttk.Button(
    root,
    text="Vermelho",
    command=lambda: select("red")
)
btn1.pack()

btn2 = ttk.Button(
    root,
    text="Verde",
    command=lambda: select("green")
)
btn2.pack()

btn3 = ttk.Button(
    root,
    text="Azul",
    command=lambda: select("blue")
)
btn3.pack()

root.mainloop()