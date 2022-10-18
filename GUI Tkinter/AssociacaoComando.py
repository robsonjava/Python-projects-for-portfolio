from logging import root
import tkinter as tk
from tkinter import ttk

#def button_clicked():
    #root.config(background="red")
    #print("Botão clicado!")

#def select(arg):
    #root.config(background=arg)

def return_pressed(event):
    print("Tecla enter pressionada!")

root = tk.Tk()
root.title("Estado Inicial")
root.geometry("600x400+500+200")


btn1 = ttk.Button(root, text="Exercutar")
btn1.bind("<Return>", return_pressed)
btn1.focus()
btn1.pack(expand=True)

root.mainloop()