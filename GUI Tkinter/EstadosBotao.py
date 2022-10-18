import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Button Widget")
root.geometry("600x400+650+300")

#def sair():
    #root.quit()

btn1 = ttk.Button(
    root,
    text="Sair",
    command=lambda: root.quit()
)
# PARA DISABILITAR O BOTAO, O SINAL DE ESCLAMAÇÃO ! É DE NEGAÇÃO
btn1.pack()

btn2 = ttk.Button(
    root,
    text="Desabilitar",
    command=lambda: btn1.state(["disabled"])
)
btn2.pack()

btn3 = ttk.Button(
    root,
    text="Habilitar",
    command=lambda: btn1.state(["!disabled"])
)
btn3.pack()

root.mainloop()