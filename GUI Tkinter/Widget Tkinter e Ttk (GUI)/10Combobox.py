import imp
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400")

selected_day = tk.StringVar()

def day_changed(event):
    showinfo(title="Resultado", message=f"Você selecionou {day_cb.get()}!"
    
    )

selected_size = tk.StringVar()

ttk.Label(
    root,
    text="Qual é o dia da semana?"
).pack()

# CAIXA DE LISTAGEM (SELECIONAR UM VALOR EM UM CONJUTO E PESONALIZADO TAMBEM)
day_cb = ttk.Combobox(
    root,
    state="readonly",# <-- O state="readonly" NÃO PERMITI ESCREVER. state="normal".
    textvariable=selected_day  
)

day_cb["values"] = ['Domingo', 'Segunda', 'Terça', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sabado']
#day_cb.set('Segunda') # DEIXAR PREDEFINIDO UM VALOR
selected_day.set('Segunda')
day_cb.pack(fill=tk.X, padx=5, pady=5)
day_cb.bind("<<ComboboxSelected>>", day_changed)



root.mainloop()