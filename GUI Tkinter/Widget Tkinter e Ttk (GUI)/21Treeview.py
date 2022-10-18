from struct import pack
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Python Tkinter")
root.geometry("800x600")

# 01-Definir as colunas
columns = ('nome', 'sobrenome', 'email')

tree = ttk.Treeview(
    root,
    columns=columns,
    show='headings' # 'tree', 'headings', 'tree headings'
)
# 02-Definir cabeçalhos
tree.heading('nome', text='Nome', anchor=tk.W)
tree.heading('sobrenome', text='Sobrenome', anchor=tk.W)
tree.heading('email', text='Email', anchor=tk.W)

tree.column('nome', width=200, anchor=tk.W)
tree.column('sobrenome', width=200, anchor=tk.W)
tree.column('email', anchor=tk.CENTER)

# 03-Adicionar dados na tabela
# tree.insert("", tk.END, values=('Robson', 'Bento', 'robsondev22@hotmail.com'))
# tree.insert("", tk.END, values=('Roque', 'Bento', 'teste1@hotmail.com'))
# tree.insert("", tk.END, values=('Rosania', 'Bento', 'teste2@hotmail.com'))
# tree.insert("", tk.END, values=('Roseane', 'Bento', 'teste3@hotmail.com'))
# tree.insert("", tk.END, values=('Joao', 'Bento', 'teste4@hotmail.com'))
# tree.insert("", tk.END, values=('Fernando', 'Bento', 'teste5@hotmail.com'))
# tree.insert("", tk.END, values=('Cremilda', 'Bento', 'teste6@hotmail.com'))
# tree.insert("", tk.END, values=('Robson', 'Bento', 'robsondev22@hotmail.com'))
# tree.insert("", tk.END, values=('Roque', 'Bento', 'teste1@hotmail.com'))
# tree.insert("", tk.END, values=('Rosania', 'Bento', 'teste2@hotmail.com'))
# tree.insert("", tk.END, values=('Roseane', 'Bento', 'teste3@hotmail.com'))
# tree.insert("", tk.END, values=('Joao', 'Bento', 'teste4@hotmail.com'))
# tree.insert("", tk.END, values=('Fernando', 'Bento', 'teste5@hotmail.com'))
# tree.insert("", tk.END, values=('Cremilda', 'Bento', 'teste6@hotmail.com'))
# tree.insert("", tk.END, values=('Robson', 'Bento', 'robsondev22@hotmail.com'))
# tree.insert("", tk.END, values=('Roque', 'Bento', 'teste1@hotmail.com'))
# tree.insert("", tk.END, values=('Rosania', 'Bento', 'teste2@hotmail.com'))
# tree.insert("", tk.END, values=('Roseane', 'Bento', 'teste3@hotmail.com'))
# tree.insert("", tk.END, values=('Joao', 'Bento', 'teste4@hotmail.com'))
# tree.insert("", tk.END, values=('Fernando', 'Bento', 'teste5@hotmail.com'))
# tree.insert("", tk.END, values=('Cremilda', 'Bento', 'teste6@hotmail.com'))

# 04 Adicionar na interface
tree.grid(row=0, column=0, sticky='nsew')

# ========================= Definir Função ===========================================
def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        print(record)

# Associar a função
tree.bind("<<TreeviewSelect>>", item_selected)

# ========================= Adicionar barra de Rolagem =================================
scrollbar = ttk.Scrollbar(
    root,
    orient=tk.VERTICAL,
    command=tree.yview
)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# ============================ Gerar dados de exemplo ===================================
contacts = []
for n in range(1, 100):
    contacts.append((f'nome {n}', f'sobrenome{n}', f'email{n}'))

for contact in contacts:
    tree.insert('', tk.END, values=contact)

# =========================== Para excluir item ============================================
def item_selected(event):
    for selected_item in tree.selection():
        tree.delete(selected_item)

tree.bind("<<TreeviewSelect>>", item_selected)

# ==================== Usando Tkinter Treeview para exibir dados hierárquicos================
# Configurar o layout
root.columnconfigure(0, weight=1)
root.rowconfigure(0,weight=1)
# Criar o treeview
tree =ttk.Treeview(root, columns="text", show='tree headings')
tree.heading('text', text='Departamentos', anchor='w')
# Adicionar dados
tree.insert("", tk.END, values=('Python'), iid=0, open=False)
tree.insert("", tk.END, values=('Java'), iid=1, open=False)
tree.insert("", tk.END, values=('JavaScript'), iid=2, open=False)
tree.insert("", tk.END, values=('HTML'), iid=3, open=False)
tree.insert("", tk.END, values=('CSS'), iid=4, open=False)

# Adicionar dados filhos
tree.insert("0", tk.END, values=('Robson'), iid=5, open=False)
tree.insert("1", tk.END, values=('Alexandra'), iid=6, open=False)
tree.insert("2", tk.END, values=('Roque'), iid=7, open=False)
tree.insert("3", tk.END, values=('Antonio'), iid=8, open=False)
tree.insert("4", tk.END, values=('Roseane'), iid=9, open=False)

# ================= Movendo itens aninhados no Treeview ====================
tree.move(4, 3, tk.END) # <-- se colocar tk.END ele fica no final. Se colocar 0 ele fica no inicio. 


# rodar a aplicação
root.mainloop()