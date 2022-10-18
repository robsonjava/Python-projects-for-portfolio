from logging import root
import tkinter as tk
from tkinter import ttk

def button_clicked():
    root.config(background="red")
    print("Botão clicado!")

root = tk.Tk()
root.title("Estado Inicial")
root.geometry("600x400+500+200")

ttk.Button(root, text="Clique me!", command=button_clicked).pack()


root.mainloop()