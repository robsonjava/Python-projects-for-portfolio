import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Login")
root.geometry("600x400+700+300")

# (PLACE) Permiti que posicione precisamente os itens dentro do contener
# widget.place(**options)

# label1
label1 = ttk.Label(
    root,
    text="Posição Absoluta",
    background="red",
    foreground="white",
    font="Arial 20"
)
# COORDENADA ABSOLUTA
label1.place(x=20, y=20)

# label2
label2 = ttk.Label(
    root,
    text="Posição Relativa",
    background="blue",
    foreground="white",
    font="Arial 20"
)
# COORDENADA RELATIVA
label2.place(relx=0.8, rely=0.5, anchor=tk.NE, relwidth=0.5)


root.mainloop()