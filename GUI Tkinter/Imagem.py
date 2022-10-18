import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Estado Inicial")
root.geometry("600x400+650+300")

foto = tk.PhotoImage(file="imagens/python.png")

label1 = ttk.Label(
    root,
    image=foto,
    text="Python é vida!",
    font="Arial 20",
    compound="top" #"top","bottom","left","right","nome","text","image"
)
label1.pack()

root.mainloop()