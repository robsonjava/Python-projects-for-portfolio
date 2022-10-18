from email.message import Message
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from click import command

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configurar a janela principal
        self.title("Minha Aplicação POO")
        self.geometry("300x50")

        # Label
        self.label = ttk.Label(
            self,
            text="Olá, Mundo!"
        )
        self.label.pack()

        # Botão
        self.button = ttk.Button(
            self,
            text="Start",
            )
        self.button["command"] = self.button_clicked
        self.button.pack()
    
    def button_clicked(self):
        showinfo(title="Informação", message="Olá, Tkinter!!!"
        )

if __name__ == "__main__":
    app = App()
    app.mainloop()