import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Votação para Presidente")
root.geometry("600x400")

selected_size = tk.StringVar()

ttk.Label(
    root,
    text="Qual o seu voto para presidente do Brasil?"
).pack()

# PERMITE QUE SELECIONE UMA DAS VARIAS OPCOES
ttk.Radiobutton(
    root,
    text="Luiz Inácio Lula da Silva",
    value="13",
    variable=selected_size
).pack(fill="x", padx=5, pady=5)

ttk.Radiobutton(
    root,
    text="Jair Messias Bolsonaro",
    value="22",
    variable=selected_size
).pack(fill="x", padx=5, pady=5)


ttk.Button(
    root,
    text="VOTAR",
    command=lambda: showinfo(title="Resultado", message=selected_size.get())
).pack(fill="x", padx=5, pady=5)

root.mainloop()