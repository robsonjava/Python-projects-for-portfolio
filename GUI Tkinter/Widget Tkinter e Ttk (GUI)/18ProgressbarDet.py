import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


root = tk.Tk()
root.title("Python Tkinter")
root.geometry("600x400")


def update_progress_label():
    return f"Progresso atual: {pb['value']}%"

def progress():
    if pb['value'] < 100:
        pb['value'] += 20
        value_label['text'] = update_progress_label()
    else:
        showinfo(message='O progresso esta completo!')

def stop():
    pb.stop()
    value_label["text"] = update_progress_label()

# PERMITI QUE Dê UM FEDBECK AO USUARIO SOBRE O ANDAMENTO DE UMA TAREFA
pb = ttk.Progressbar(
    root,
    orient="horizontal", # vertical
    length=280,
    mode="determinate" # "indeterminate" "determinate"
)
#pb.pack()

pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

value_label = ttk.Label(root, text=update_progress_label())
value_label.grid(column=0, row=1, columnspan=2)


start_button = ttk.Button(
    root,
    text="Progress",
    command=progress
)
start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

stop_button = ttk.Button(
    root,
    text="Stop",
    command=stop
)
stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)



root.mainloop()