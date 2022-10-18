import tkinter as tk
from turtle import window_height, window_width

root = tk.Tk()
root.title("Centralizar Janela")

window_width1 = 300
window_height2 = 200

# Obter as dimensoes da tela
screen_windth = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Encontrar o ponto central
center_x = int(screen_windth / 2 - window_width1 / 2)
center_y = int(screen_height / 2 - window_height2 / 2)

# Definir a posição no centro da tela

root.geometry(f"{window_width1}x{window_height2}+{center_x}+{center_y}")

root.mainloop()