import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk


conjuntos_aux = []

# Funções relacionadas ao arquivo e manipulação de dados
def salvar_em_planilha(conjuntos, nome_arquivo):
    df = pd.DataFrame(conjuntos, columns=["Nome", "Forma de Contato", "Números Escolhidos"])
    df.to_excel(nome_arquivo, index=False)

def editar_conjunto(conjuntos, indice, novo_nome, nova_forma_contato, novo_conjunto, nome_arquivo):
    conjuntos[indice - 1] = [novo_nome, nova_forma_contato, novo_conjunto]
    salvar_em_planilha(conjuntos, nome_arquivo)

def excluir_conjunto(conjuntos, indice, nome_arquivo):
    del conjuntos[indice - 1]
    salvar_em_planilha(conjuntos, nome_arquivo)
    
def adicionar():
    try:
        nome = entry_nome.get()
        forma_contato = entry_forma_contato.get()
        conjunto_str = entry_conjunto.get()

        if not conjunto_str.replace(" ", "").isdigit():
            messagebox.showerror("Erro", "Digite apenas números no conjunto!")
            return

        conjunto = list(map(int, conjunto_str.split()))

        # Permitir números iguais em diferentes entradas
        conjuntos_aux.append([nome, forma_contato, conjunto])
        salvar_em_planilha(conjuntos_aux, 'conjuntos.xlsx')
        messagebox.showinfo("Sucesso", "Conjunto adicionado com sucesso!")
        update_treeview()  # Atualizar a exibição na Treeview
    except ValueError:
        messagebox.showerror("Erro", "Digite um conjunto válido!")

def obter_resultados(conjuntos, numeros_digitados):
    resultados = []
    for conjunto in conjuntos:
        acertos = set(conjunto[2]) & set(numeros_digitados)
        resultados.append({
            "Nome": conjunto[0],
            "Números Escolhidos": conjunto[2],
            "Acertos": list(acertos),
            "Quantidade de Acertos": len(acertos)
        })

    # Ordenar os resultados pelos maiores acertos
    resultados = sorted(resultados, key=lambda x: x["Quantidade de Acertos"], reverse=True)

    # Retornar os 10 primeiros colocados, se houver
    return resultados[:10]

def exibir_resultados(resultados):
    janela_resultados = tk.Toplevel(root)
    janela_resultados.title("Resultados")

    # Adicionar uma barra de rolagem vertical e horizontal à lista de resultados
    scrollbar_y = tk.Scrollbar(janela_resultados, orient=tk.VERTICAL)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

    scrollbar_x = tk.Scrollbar(janela_resultados, orient=tk.HORIZONTAL)
    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

    # Adicionar uma lista para exibir os resultados
    lista_resultados = tk.Listbox(
        janela_resultados, height=20,
        yscrollcommand=scrollbar_y.set,
        xscrollcommand=scrollbar_x.set,
        font=("Courier", 10)
    )
    lista_resultados.pack(fill=tk.BOTH, expand=True)
    scrollbar_y.config(command=lista_resultados.yview)
    scrollbar_x.config(command=lista_resultados.xview)

    # Adicionar resultados à lista
    for resultado in resultados:
        linha = f"Nome: {resultado['Nome']}, Números Escolhidos: {resultado['Números Escolhidos']}, " \
                f"Acertos: {resultado['Quantidade de Acertos']}, Números Acertados: {resultado['Acertos']}"
        lista_resultados.insert(tk.END, linha)

# Funções relacionadas à interface gráfica
def editar_selecionado():
    item_selecionado = tree.focus()
    if not item_selecionado:
        messagebox.showwarning("Aviso", "Selecione uma entrada para editar.")
        return

    try:
        # Obter os dados da entrada selecionada
        indice = int(tree.item(item_selecionado, "values")[0]) - 1
        novo_nome = entry_novo_nome.get()
        nova_forma_contato = entry_nova_forma_contato.get()
        novo_conjunto_str = entry_novo_conjunto.get()

        if not novo_conjunto_str.replace(" ", "").isdigit():
            messagebox.showerror("Erro", "Digite apenas números no novo conjunto!")
            return

        novo_conjunto = list(map(int, novo_conjunto_str.split()))

        # Atualizar dados e refletir as mudanças na Treeview
        editar_conjunto(conjuntos_aux, indice, novo_nome, nova_forma_contato, novo_conjunto, 'conjuntos.xlsx')
        tree.item(item_selecionado, values=(indice + 1, novo_nome, nova_forma_contato, novo_conjunto))
        messagebox.showinfo("Sucesso", "Conjunto editado com sucesso!")

    except ValueError:
        messagebox.showerror("Erro", "Erro ao editar o conjunto!")

def verificar():
    numeros_digitados_str = entry_numeros.get().strip()
    if not numeros_digitados_str.replace(" ", "").isdigit():
        messagebox.showerror("Erro", "Digite apenas números!")
        return

    numeros_digitados = list(map(int, numeros_digitados_str.split()))

    # Converter os números dos conjuntos para inteiros
    conjuntos_int = []
    for nome, forma_contato, numeros in conjuntos_aux:
        if isinstance(numeros, list):
            numeros = [int(num) for num in numeros]
        else:
            numeros = numeros.strip('[]')
            if numeros:
                numeros = [int(num) for num in numeros.split(',')]
            else:
                numeros = []
        conjuntos_int.append([nome, forma_contato, numeros])

    resultados = obter_resultados(conjuntos_int, numeros_digitados)

    # Exibir os resultados em uma nova janela
    exibir_resultados(resultados)

def editar():
    try:
        indice = int(entry_indice.get())
        novo_nome = entry_novo_nome.get()
        nova_forma_contato = entry_nova_forma_contato.get()
        novo_conjunto_str = entry_novo_conjunto.get()
        if not novo_conjunto_str.replace(" ", "").isdigit():
            messagebox.showerror("Erro", "Digite apenas números no novo conjunto!")
            return

        novo_conjunto = list(map(int, novo_conjunto_str.split()))
        editar_conjunto(conjuntos_aux, indice, novo_nome, nova_forma_contato, novo_conjunto, 'conjuntos.xlsx')
        messagebox.showinfo("Sucesso", "Conjunto editado com sucesso!")
        update_treeview()  # Atualizar a exibição na Treeview
    except ValueError:
        messagebox.showerror("Erro", "Índice inválido!")

def excluir():
    try:
        indice = int(entry_indice.get())
        excluir_conjunto(conjuntos_aux, indice, 'conjuntos.xlsx')
        update_treeview()  # Atualizar a exibição na Treeview
        messagebox.showinfo("Sucesso", "Conjunto excluído com sucesso!")

    except ValueError:
        messagebox.showerror("Erro", "Índice inválido!")

def limpar_todos_os_dados():
    confirmacao = messagebox.askyesno("Confirmação", "Tem certeza de que deseja limpar todos os dados da planilha?")
    if confirmacao:
        tree.delete(*tree.get_children())
        conjuntos_aux.clear()
        salvar_em_planilha(conjuntos_aux, 'conjuntos.xlsx')

def update_treeview():
    tree.delete(*tree.get_children())
    for i, conjunto in enumerate(conjuntos_aux, start=1):
        tree.insert("", "end", values=(i, conjunto[0], conjunto[1], conjunto[2]))

# Funções de pesquisa
def pesquisar_por_nome():
    nome_pesquisado = entry_pesquisar.get().lower()
    if not nome_pesquisado:
        messagebox.showwarning("Aviso", "Digite um nome para pesquisar.")
        return

    tree.delete(*tree.get_children())
    for i, conjunto in enumerate(conjuntos_aux, start=1):
        if nome_pesquisado in conjunto[0].lower():
            tree.insert("", "end", values=(i, conjunto[0], conjunto[1], conjunto[2]))

def on_item_click(event):
    selected_items = tree.selection()
    if not selected_items:
        return

    item = selected_items[0]
    values = tree.item(item, "values")

    if not values:
        return

    indice = int(values[0])
    entry_indice.delete(0, tk.END)
    entry_indice.insert(0, str(indice))
    entry_novo_nome.delete(0, tk.END)
    entry_novo_nome.insert(0, values[1])
    entry_nova_forma_contato.delete(0, tk.END)
    entry_nova_forma_contato.insert(0, values[2])
    entry_novo_conjunto.delete(0, tk.END)
    entry_novo_conjunto.insert(0, " ".join(map(str, values[3])))


def atualizar():
    update_treeview()

try:
    conjuntos = pd.read_excel('conjuntos.xlsx').values.tolist()
except FileNotFoundError:
    conjuntos = []

root = tk.Tk()
root.title("Verificador de Acertos")

label_nome = tk.Label(root, text="Nome:")
entry_nome = tk.Entry(root)

label_forma_contato = tk.Label(root, text="Forma de Contato:")
entry_forma_contato = tk.Entry(root)

label_pesquisar = tk.Label(root, text="Pesquisar por Nome:")
entry_pesquisar = tk.Entry(root)
button_pesquisar = tk.Button(root, text="Pesquisar", command=pesquisar_por_nome)

label_conjunto = tk.Label(root, text="Números Escolhidos:")
entry_conjunto = tk.Entry(root)

button_adicionar = tk.Button(root, text="Adicionar", command=adicionar)

label_numeros = tk.Label(root, text="Digite alguns números aleatórios:")
entry_numeros = tk.Entry(root)

button_verificar = tk.Button(root, text="Verificar", command=verificar)

label_indice = tk.Label(root, text="Índice do Conjunto:")
entry_indice = tk.Entry(root)

label_novo_nome = tk.Label(root, text="Novo Nome:")
entry_novo_nome = tk.Entry(root)

label_nova_forma_contato = tk.Label(root, text="Nova Forma de Contato:")
entry_nova_forma_contato = tk.Entry(root)

label_novo_conjunto = tk.Label(root, text="Novos Números Escolhidos:")
entry_novo_conjunto = tk.Entry(root)


# Adicionar botão para limpar todos os dados
btn_limpar_todos = tk.Button(root, text="Limpar Todos os Dados", command=limpar_todos_os_dados)
btn_limpar_todos.grid(row=3, column=2, pady=10)

button_editar = tk.Button(root, text="Editar", command=editar)
button_excluir = tk.Button(root, text="Excluir", command=excluir)

# Adicionar Treeview para exibir os dados
tree_columns = ("#", "Nome", "Forma de Contato", "Números Escolhidos")
tree = ttk.Treeview(root, columns=tree_columns, show="headings", selectmode="browse")
for col in tree_columns:
    tree.heading(col, text=col)
tree.bind("<ButtonRelease-1>", on_item_click)
tree.grid(row=1, column=0, columnspan=4, pady=10)  # Use grid() em vez de pack()

# Posicionar widgets na interface usando grid() em vez de pack()
label_nome = tk.Label(root, text="Nome:")
entry_nome = tk.Entry(root)
label_nome.grid(row=3, column=0, pady=5, padx=5, sticky="e")
entry_nome.grid(row=3, column=1, pady=5, padx=5)

label_forma_contato = tk.Label(root, text="Forma de Contato:")
entry_forma_contato = tk.Entry(root)
label_forma_contato.grid(row=4, column=0, pady=5, padx=5, sticky="e")
entry_forma_contato.grid(row=4, column=1, pady=5, padx=5)

label_conjunto = tk.Label(root, text="Números Escolhidos:")
entry_conjunto = tk.Entry(root)
label_conjunto.grid(row=5, column=0, pady=5, padx=5, sticky="e")
entry_conjunto.grid(row=5, column=1, pady=5, padx=5)

button_adicionar = tk.Button(root, text="Adicionar", command=adicionar)
button_adicionar.grid(row=5, column=2, pady=5, padx=5)

label_numeros = tk.Label(root, text="Digite alguns números aleatórios:")
entry_numeros = tk.Entry(root)
label_numeros.grid(row=6, column=0, pady=5, padx=5, sticky="e")
entry_numeros.grid(row=6, column=1, pady=5, padx=5)

button_verificar = tk.Button(root, text="Verificar", command=verificar)
button_verificar.grid(row=6, column=2, pady=5, padx=5)

label_pesquisar = tk.Label(root, text="Pesquisar por Nome:")
entry_pesquisar = tk.Entry(root)
label_pesquisar.grid(row=7, column=0, pady=5, padx=5, sticky="e")
entry_pesquisar.grid(row=7, column=1, pady=5, padx=5)

button_pesquisar = tk.Button(root, text="Pesquisar", command=pesquisar_por_nome)
button_pesquisar.grid(row=7, column=2, pady=5, padx=5)

label_indice = tk.Label(root, text="Índice do Conjunto:")
entry_indice = tk.Entry(root)
label_indice.grid(row=8, column=0, pady=5, padx=5, sticky="e")
entry_indice.grid(row=8, column=1, pady=5, padx=5)

label_novo_nome = tk.Label(root, text="Novo Nome:")
entry_novo_nome = tk.Entry(root)
label_novo_nome.grid(row=9, column=0, pady=5, padx=5, sticky="e")
entry_novo_nome.grid(row=9, column=1, pady=5, padx=5)

label_nova_forma_contato = tk.Label(root, text="Nova Forma de Contato:")
entry_nova_forma_contato = tk.Entry(root)
label_nova_forma_contato.grid(row=10, column=0, pady=5, padx=5, sticky="e")
entry_nova_forma_contato.grid(row=10, column=1, pady=5, padx=5)

label_novo_conjunto = tk.Label(root, text="Novos Números Escolhidos:")
entry_novo_conjunto = tk.Entry(root)
label_novo_conjunto.grid(row=11, column=0, pady=5, padx=5, sticky="e")
entry_novo_conjunto.grid(row=11, column=1, pady=5, padx=5)

button_editar = tk.Button(root, text="Editar", command=editar)
button_editar.grid(row=12, column=0, pady=10)

button_excluir = tk.Button(root, text="Excluir", command=excluir)
button_excluir.grid(row=12, column=1, pady=10)

# Botão para atualizar a Treeview manualmente
button_atualizar = tk.Button(root, text="Atualizar", command=atualizar)
button_atualizar.grid(row=13, column=0, pady=10, columnspan=2)

# Iniciar loop da interface
root.mainloop()
