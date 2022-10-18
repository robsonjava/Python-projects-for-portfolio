import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400")

current_value = tk.DoubleVar()

def slider_changed(event):
    valor = current_value.get()
    print("{: .2f}".format(valor))
    #print(slider.get())

# Permiti que insira um valor movendo um indicador
slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient="vertical", #horizontal
    variable=current_value,
    command=slider_changed
)
slider.pack()

ttk.Button(
    root,
    text="Ativar",
    command=lambda: slider.configure(state="normal")
).pack()

ttk.Button(
    root,
    text="Desativar",
    command=lambda: slider.configure(state="disabled")
).pack()

root.mainloop()