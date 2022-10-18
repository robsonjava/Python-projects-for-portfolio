import imp
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Criação da classe
class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx':5, 'pady':5}

        # label
        self.label = ttk.Label(
            self,
            text="Olá, Mundo!"
        )
        self.label.pack(**options)

        # butoon
        self.button = ttk.Button(
            self,
            text="Start"
        )
        self.button["command"] = self.button_clicked
        self.button.pack(**options)

        self.pack(**options)

    def button_clicked(self):
        showinfo(title="Informação", message="Parabéns!!!")

# Para apresentar a janela
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Minha Pagina")
        self.geometry("300x100")

if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    app.mainloop()