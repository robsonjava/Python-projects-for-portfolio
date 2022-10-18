from tkinter import Tk, Text, ttk


root = Tk()
root.title("Python Tkinter")

# SINTAXE PARA CRIAR
#text = tk.Text(root, conf={}, **kw)

text = Text(
    root,
    height=8,
    width=10,
    font="Arial 14",
    background="blue", # Cor do fundo
    foreground="black" # Cor da fonte

)
text.pack()


root.mainloop()