from logging import root
from multiprocessing import Event
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Estado Inicial")
root.geometry("600x400+500+200")

# PROPRIEDADES DO LABEL
label1 = ttk.Label(
    root,
    text="Este é um label\nCurso de Python Tkinter",
    # PRIMEIRO NOME, DEPOIS TAMANHO
    #font="Arial 24 bold italic"

    # COMO TUPLA
    font=("Verdana", 30, "bold", "italic")
)
label1.pack()

root.mainloop()