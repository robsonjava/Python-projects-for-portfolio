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

text.insert("1.0", "Esta é um widget text.")
txt = text.get("1.0", "end")
print(txt)



root.mainloop()