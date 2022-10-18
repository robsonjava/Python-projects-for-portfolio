import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400")

selected_size = tk.StringVar()

ttk.Label(
    root,
    text="Qual é o tamanho da camiseta?"
).pack()

# PERMITE QUE SELECIONE UMA DAS VARIAS OPCOES
ttk.Radiobutton(
    root,
    text="Pequena",
    value="P",
    variable=selected_size
).pack(fill="x", padx=5, pady=5)

ttk.Radiobutton(
    root,
    text="Medio",
    value="M",
    variable=selected_size
).pack(fill="x", padx=5, pady=5)

ttk.Radiobutton(
    root,
    text="Grande",
    value="G",
    variable=selected_size
).pack(fill="x", padx=5, pady=5)

ttk.Button(
    root,
    text="Obter o tamanho selecionado",
    command=lambda: showinfo(title="Resultado", message=selected_size.get())
).pack(fill="x", padx=5, pady=5)

root.mainloop()