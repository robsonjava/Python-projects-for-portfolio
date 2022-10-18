from logging import root
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Estado Inicial")
root.geometry("600x400+500+200")

# USANDO ARGUMENTO DE PALAVRA-CHAVE AO CRIAR O WIDGET
ttk.Label(root, text="Ola Mundo!").pack()

# USANDO UM INDICE DE DICIONARIO APOS A CRIACAO DO WIDGET
lbl1 = ttk.Label(root)
lbl1["text"] = "Outro Ola Mundo!"
lbl1.pack()

# USANDO O METODO CONFIG() COM ATRIBUTOS DE PALAVRA-CHAVE
lbl2 = ttk.Label(root)
lbl2.config(text="Mais um Ola Mundo!")
lbl2.pack() 

root.mainloop()