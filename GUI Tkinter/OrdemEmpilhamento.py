from logging import RootLogger, root
import tkinter as tk

root = tk.Tk()
root.title("Estado Inicial")
root.geometry("600x400")

# FICA SEMPRE NA FRENTE DAS JANELAS
#root.attributes("-topmost", 1)

# PARA MOVER PARA CIMA
#root.lift()

# PARA MOVER PARA BAIXO
root.lower()

root.mainloop()