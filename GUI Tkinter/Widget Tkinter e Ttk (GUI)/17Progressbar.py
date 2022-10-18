import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400")
root.resizable(True, True)
root.grid()

# PERMITI QUE Dê UM FEDBECK AO USUARIO SOBRE O ANDAMENTO DE UMA TAREFA
pb = ttk.Progressbar(
    root,
    orient="horizontal", # vertical
    length=300,
    mode="indeterminate" # "indeterminate" "determinate"
)
#pb.pack()
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

start_button = ttk.Button(
    root,
    text="Start",
    command=lambda: pb.start(10)
)
start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

stop_button = ttk.Button(
    root,
    text="Stop",
    command=lambda: pb.stop()
)
stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)

pb.start()

root.mainloop()