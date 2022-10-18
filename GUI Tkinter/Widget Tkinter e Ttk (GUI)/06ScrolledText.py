from msilib.schema import Font
import tkinter as tk
from tkinter import Scrollbar, ttk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()
root.title("Python Tkinter")

# CAIXA DE TEXTO COM BARRA DE ROLAGEM
st = ScrolledText(
    root,
    width=50,
    height=10,
    font="Arial 12"
).pack(fill=tk.BOTH, side=tk.LEFT, expand=True)




root.mainloop()