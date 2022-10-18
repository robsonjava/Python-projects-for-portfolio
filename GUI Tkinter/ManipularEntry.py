import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Entry Widget")
root.geometry("600x400+650+300")

def btn1_clicked(event=None):
    if texto.get() != "insira seu nome: ":
        msg = f"Bem vindo(a) {texto.get()}!"
        showinfo(title="Informação", message=msg)
        texto.set("Insira seu nome: ")
        textbox.select_range(0, tk.END)
        textbox.focus()

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
textbox.bind("<Return>", btn1_clicked)
textbox.pack()

btn1 = ttk.Button(
    root,
    text="exercutar",
    command=btn1_clicked
)
btn1.pack()

root.mainloop()