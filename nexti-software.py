import tkinter as tk
from tkinter import ttk

# Função a ser chamada quando o botão "Solicitar" for clicado
def solicitar_acao():
    print("Botão Solicitar clicado")

# Função a ser chamada quando o botão "Manuseio" for clicado
def exibir_tabela():
    # Remove todos os widgets do root, exceto o frame_botoes
    for widget in root.winfo_children():
        if widget != frame_botoes:
            widget.destroy()
    
    # Cria um frame para a tabela
    frame_tabela = tk.Frame(root, bg="lightblue")
    frame_tabela.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")  # Centraliza o frame na janela
    
    # Define as colunas da tabela
    colunas = ("Tipo", "Área", "Nº do carrinho", "Status", "Visualizar")
    
    # Cria a tabela usando Treeview
    tabela = ttk.Treeview(frame_tabela, columns=colunas, show='headings')
    
    # Define os cabeçalhos das colunas e centraliza o texto
    for coluna in colunas:
        tabela.heading(coluna, text=coluna)
        tabela.column(coluna, width=150, anchor=tk.CENTER)  # Ajuste para centralizar o texto
    
    # Adiciona alguns dados de exemplo à tabela
    dados = [
        ("Porcas", 6, "112436", "PENDENTE"),
        ("Parafusos", 4, "112437", "CONCLUIDO"),
        ("Paralama L.D", 1, "PRD1421", "EM ANDAMENTO"),
        ("Porta L.E", 2, "PTE1755", "EM ANDAMENTO"),
        ("MY 25", 3, "MY25X", "PENDENTE")
    ]
    
    for item in dados:
        tabela.insert("", tk.END, values=item)
    
    # Adiciona a tabela ao frame
    tabela.pack(fill=tk.BOTH, expand=True)

    # Ajusta o grid para que o frame_tabela se expanda com a janela
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

# Cria a janela principal
root = tk.Tk()
root.title("Minha Aplicação")
root.geometry("900x500")  # Define o tamanho da janela (largura x altura)
root.configure(bg="lightblue")  # Define a cor de fundo da janela

# Cria um frame para os botões
frame_botoes = tk.Frame(root, bg="lightblue")
frame_botoes.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Cria um frame dentro do frame_botoes para centralizar os botões
frame_botoes_centralizados = tk.Frame(frame_botoes, bg="lightblue")
frame_botoes_centralizados.grid(row=0, column=0, padx=20, pady=20)

# Centraliza o frame_botoes_centralizados na tela
frame_botoes.grid_rowconfigure(0, weight=1)
frame_botoes.grid_columnconfigure(0, weight=1)
frame_botoes_centralizados.grid_rowconfigure(0, weight=1)
frame_botoes_centralizados.grid_columnconfigure(0, weight=1)
frame_botoes_centralizados.grid_rowconfigure(1, weight=1)

# Cria o botão "Solicitar"
botao_solicitar = tk.Button(frame_botoes_centralizados, text="Solicitar", command=solicitar_acao,
                            bg="lightgreen", fg="black", font=("Arial", 12, "bold"), width=15, height=2,
                            relief="raised", padx=20, pady=10)
botao_solicitar.grid(row=0, column=0, padx=20, pady=10)  # Posiciona o botão no grid

# Cria o botão "Manuseio"
botao_manuseio = tk.Button(frame_botoes_centralizados, text="Manuseio", command=exibir_tabela,
                           bg="lightcoral", fg="white", font=("Arial", 12, "bold"), width=15, height=2,
                           relief="raised", padx=20, pady=10)
botao_manuseio.grid(row=1, column=0, padx=20, pady=10)  # Posiciona o botão no grid

# Ajusta o grid para que o frame_botoes se expanda com a janela
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Inicia o loop principal da interface gráfica
root.mainloop()
