import tkinter as tk
from tkinter import Scrollbar, ttk

root = tk.Tk()
root.title("Python Tkinter")
root.resizable(False, False)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# CAIXA DE TEXTO
text1 = tk.Text(root, height=10, font="Arial 12")
text1.grid(row=0, column=0, sticky="ew")

# BARRA DE ROLAGEM
scrollbar = ttk.Scrollbar(
    root,
    orient="vertical",
    command=text1.yview
)
scrollbar.grid(
    row=0,
    column=1,
    sticky="ns"
)
# VERTICAL: "yscrollcommand" HORIZONTAL: "xscrollcommand"
text1["yscrollcommand"] = scrollbar.set

root.mainloop()