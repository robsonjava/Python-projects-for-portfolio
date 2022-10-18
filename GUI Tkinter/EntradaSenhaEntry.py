import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Entry Widget")
root.geometry("600x400+650+300")

# PERMITI CRIAR UM CAMPO DE ENTRADAS DE DADOS

textbox = ttk.Entry(
    root,
    # ESCONDER
    show="*"
)
textbox.focus()
textbox.pack()


btn1 = ttk.Button(
    root,
    text="exercutar",
    command=lambda: print(textbox.get())
)
btn1.pack()

root.mainloop()