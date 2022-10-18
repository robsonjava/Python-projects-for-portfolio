from logging import root
import tkinter as tk

root = tk.Tk()

# TITULO DA JANELA
root.title("Sejam bem vindo!")

titulo = root.title()

# MENSAGEM DA CAIXA 
lbl = tk.Label(root, text=titulo)
lbl.pack()

root.mainloop()