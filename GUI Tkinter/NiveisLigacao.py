from logging import root
from multiprocessing import Event
import tkinter as tk
from tkinter import ttk

#def button_clicked():
    #root.config(background="red")
    #print("Botão clicado!")

def log(event):
    print(event)

root = tk.Tk()
root.title("Estado Inicial")
root.geometry("600x400+500+200")


btn1 = tk.Button(root, text="Exercutar 1")
btn1.focus()
btn1.bind_class("Button", "<Any-KeyPress>", log)
btn1.pack()

btn2 = tk.Button(root, text="Exercutar 2")
btn2.pack()

btn3 = tk.Button(root, text="Exercutar 3")
btn3.pack()

root.mainloop()