import tkinter as tk
from tkinter import font

# Definindo as cores
cor_fundo = "#2E2E2E"  # Fundo escuro
cor_display = "#1C1C1C"  # Fundo do display
cor_texto = "#FFFFFF"  # Texto branco
cor_botoes = "#4F4F4F"  # Cor dos botões
cor_botoes_operadores = "#FF9500"  # Cor dos botões de operadores
cor_botoes_especiais = "#D4D4D2"  # Cor dos botões especiais (C, =)

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora Moderna")
janela.geometry("400x600")
janela.configure(bg=cor_fundo)

# Criando o campo de exibição
display_font = font.Font(family="Helvetica", size=32, weight="bold")
display = tk.Entry(janela, font=display_font, borderwidth=0, relief="flat", justify="right", bg=cor_display, fg=cor_texto, insertbackground=cor_texto)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=(20, 10), ipady=20, sticky="nsew")

# Função para adicionar o valor do botão ao display
def clique_botao(valor):
    if valor == "=":
        try:
            resultado = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(resultado))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Erro")
    elif valor == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, valor)

# Função para criar botões estilizados
def criar_botao(texto, cor_fundo, cor_texto, row, column, colspan=1):
    botao = tk.Button(janela, text=texto, font=display_font, bg=cor_fundo, fg=cor_texto, relief="flat", borderwidth=0, 
                      command=lambda valor=texto: clique_botao(valor))
    botao.grid(row=row, column=column, columnspan=colspan, padx=5, pady=5, ipadx=20, ipady=20, sticky="nsew")
    return botao

# Criando os botões
criar_botao("C", cor_botoes_especiais, cor_fundo, 1, 0)
criar_botao("/", cor_botoes_operadores, cor_texto, 1, 3)
criar_botao("7", cor_botoes, cor_texto, 2, 0)
criar_botao("8", cor_botoes, cor_texto, 2, 1)
criar_botao("9", cor_botoes, cor_texto, 2, 2)
criar_botao("*", cor_botoes_operadores, cor_texto, 2, 3)
criar_botao("4", cor_botoes, cor_texto, 3, 0)
criar_botao("5", cor_botoes, cor_texto, 3, 1)
criar_botao("6", cor_botoes, cor_texto, 3, 2)
criar_botao("-", cor_botoes_operadores, cor_texto, 3, 3)
criar_botao("1", cor_botoes, cor_texto, 4, 0)
criar_botao("2", cor_botoes, cor_texto, 4, 1)
criar_botao("3", cor_botoes, cor_texto, 4, 2)
criar_botao("+", cor_botoes_operadores, cor_texto, 4, 3)
criar_botao("0", cor_botoes, cor_texto, 5, 0, colspan=2)
criar_botao(".", cor_botoes, cor_texto, 5, 2)
criar_botao("=", cor_botoes_operadores, cor_texto, 5, 3)

# Ajustando o layout das linhas e colunas
for i in range(6):
    janela.rowconfigure(i, weight=1)
for j in range(4):
    janela.columnconfigure(j, weight=1)

# Executando a aplicação
janela.mainloop()