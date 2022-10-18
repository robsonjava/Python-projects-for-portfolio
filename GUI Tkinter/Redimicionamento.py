from logging import root
import tkinter as tk

root = tk.Tk()

root.title("Redimisionar")
root.geometry("600x400")

# TAMANHO MINIMO
root.minsize(400, 400)

# TAMANHO MAXIMO
root.maxsize(500, 500)

# ATIVAR OU DESATIVAR O REDIMICIONAMENTO
root.resizable(False, True)

root.mainloop()