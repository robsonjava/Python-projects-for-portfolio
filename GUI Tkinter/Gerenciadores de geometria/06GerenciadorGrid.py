import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Entry Widget")
root.geometry("600x400+650+300")

# Configurar as linhas e colunas da grade
root.columnconfigure(index=0, weight=2)

root.rowconfigure(index=0, weight=1)

root.mainloop()