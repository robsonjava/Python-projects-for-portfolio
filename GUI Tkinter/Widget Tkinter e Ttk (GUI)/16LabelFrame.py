import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400")
root.resizable(True, True)

alignment_var = tk.StringVar()

# CONTENE QUE CONTEM OUTORS ITENS
lf = ttk.Labelframe(root, text="Aliamento", labelanchor="se")
lf.grid(column=0, row=0, padx=20, pady=20)

rb1 = ttk.Radiobutton(lf, text="Esquerda",value="E", variable=alignment_var)
rb1.grid(column=0, row=0, ipadx=10, ipady=10)

rb2 = ttk.Radiobutton(lf, text="Centro",value="C", variable=alignment_var)
rb2.grid(column=1, row=0, ipadx=10, ipady=10)

rb3 = ttk.Radiobutton(lf, text="Direita",value="D", variable=alignment_var)
rb3.grid(column=2, row=0, ipadx=10, ipady=10)

root.mainloop()