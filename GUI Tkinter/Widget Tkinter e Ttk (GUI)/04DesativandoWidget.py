from tkinter import Tk, Text, ttk


root = Tk()
root.title("Python Tkinter")

# SINTAXE PARA CRIAR
#text = tk.Text(root, conf={}, **kw)

text = Text(
    root,
    height=20,
    width=50,
    font="Arial 14"

)
text.pack()

text.insert("1.0", "Esta é um widget text.")
txt = text.get("1.0", "end")
print(txt)

#text["state"] = "disabled" # Para disabilitar

# Botão para ativar
ttk.Button(
    root,
    text="Ativar",
    command=lambda: text.config(state="normal")
).pack()

# Botão para desativar
ttk.Button(
    root,
    text="Desativar",
    command=lambda: text.config(state="disabled")
).pack()

root.mainloop()