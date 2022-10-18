import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Entry Widget")
root.geometry("600x400+650+300")

# Armazenar os valores dos textbox
# Definir o texto (GET), Definir o texto (SET)
texto = tk.StringVar()
texto.set("Insira seu nome: ")


# PERMITI CRIAR UM CAMPO DE ENTRADAS DE DADOS

textbox = ttk.Entry(
    root,
    textvariable=texto,
    font="Arial 12 italic"
)
# Selecionar o texto da caixa
textbox.select_range(0, tk.END)
textbox.focus()
textbox.pack()

btn1 = ttk.Button(
    root,
    text="exercutar",
    command=lambda: print(textbox.get())
)
btn1.pack()

root.mainloop()