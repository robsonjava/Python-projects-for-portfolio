import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400")

# funçao
def resultadoChek():
    showinfo("Resultado", f"O usuario {concordar.get()}!")

# Criar uma variavel
concordar = tk.StringVar()

# Modo tematico
ttk.Checkbutton(
    root,
    text="Eu concordo",
    variable=concordar,
    command=resultadoChek,
    onvalue="Concorda",
    offvalue="Não concorda"
).pack()


root.mainloop()