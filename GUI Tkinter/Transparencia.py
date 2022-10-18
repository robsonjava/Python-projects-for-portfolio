from logging import root
import tkinter as tk

root = tk.Tk()
root.title("Transparente")
root.geometry("600x400+500+200")

# CANAL ALPHA VALORES ENTRE 0.0 e 1.0
root.attributes("-alpha", 0.75)

root.mainloop()