import tkinter as tk
from tkinter import Scrollbar, ttk


root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

langs = ('Java','C#', 'C', 'C++', 'Python', 'Go', 'JavaScript')

langs_var = tk.StringVar(value=langs)

listbox = tk.Listbox(
    root,
    listvariable=langs_var,
    height=6,
    font="Arial 16",
    selectmode="browse" # extended
)
# Usar o "grid" no lugar do "pack" para criar uma barra de rolagem
listbox.grid(
    column=0,
    row=0,
    sticky="nwes"
) 

Scrollbar = ttk.Scrollbar(
    root,
    orient="vertical",
    command=listbox.yview
)

listbox['yscrollcommand'] = Scrollbar.set

Scrollbar.grid(
    column=1,
    row=0,
    sticky="ns"
)

# MOSTRAR NO PRINT
def items_selected(event):
    selected_indices = listbox.curselection()
    for i in selected_indices:
        print(listbox.get(i))

listbox.bind("<<ListboxSelect>>", items_selected)



root.mainloop()

