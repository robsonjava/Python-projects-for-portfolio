import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400")

current_value = tk.StringVar(value=0)

def value_changed():
    print(current_value.get())
    #print(spin_box.get())

valores = (0, 2, 4, 6, 8, 10)

# Permiti que selecione um valor do conjunto
spin_box = ttk.Spinbox(
    root,
    from_=0,
    to=10,
    font="Arial 18",
    textvariable=current_value,
    command=value_changed,
    wrap=True,
    values=valores
)

spin_box.pack()


root.mainloop()