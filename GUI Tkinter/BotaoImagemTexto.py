import imp
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from click import command

def download_clicked():
    showinfo(
        title="Informação",
        message="Botão download cricado"
    )

root = tk.Tk()
root.title("Button Widget")
root.geometry("600x400+650+300")

btnIcon = tk.PhotoImage(file="imagens/download.png")

# BUTTON DE DOWNLOAD
btn1 = ttk.Button(
    root,
    image=btnIcon,
    text="Download",
    compound=tk.LEFT, #"left", "right", "top", "bottom"
    command=download_clicked
)
btn1.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()