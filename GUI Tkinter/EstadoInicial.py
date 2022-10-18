from logging import root
import tkinter as tk

root = tk.Tk()

root.title("Estado Inicial")
root.geometry("600x400+500+200")

#  APRESENTAR MAXIMIZADA
root.state('zoomed')

#  APRESENTAR MINIMIZADA
#root.state("iconic")

root.mainloop()