from cProfile import label
import tkinter as tk
from tkinter import ttk



root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400")

notebook = ttk.Notebook(root)
notebook.pack(padx=10, expand=True)

frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

label1 = ttk.Label(frame1, text="(humor injetado e afins).", font="Arial 18")
label1.pack()

label2 = ttk.Label(frame2, text="Lorem Ipsum é simplesmente um texto fictício da indústria tipográfica", font="Arial 18")
label2.pack()

notebook.add(frame1, text="Informação geral")
notebook.add(frame2, text="Profile")



root.mainloop()