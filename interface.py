# interface.py

import tkinter as tk
import customtkinter as ctk
from tkinter import simpledialog
from validadores import *
from mostrar_tabela import MostrarTabela

# Função para tratar a ação do botão
def processar_texto():
    texto = text_input.get("1.0", tk.END).strip()
    opcao = var_opcao.get()

    if opcao == "Mostrar em forma de tabela":
        tabela = MostrarTabela(texto)
        tabela.mostrar()
    else:
        opcao_index = opcoes.index(opcao)
        if opcao_index in validadores:
            if opcao_index in [8, 11]:  # Opções que requerem input adicional
                input_valor = simpledialog.askstring("Input", "Digite a palavra a ser buscada:" if opcao_index == 8 else "Digite as letras a serem encontradas nas palavras:")
                if opcao_index == 8:
                    validador = ValidadorPalavras(texto, input_valor)
                elif opcao_index == 11:
                    validador = ValidadorPalavrasComLetras(texto, input_valor)
            else:
                validador = validadores[opcao_index](texto)
            result = validador.exibir_resultado()
            result_display.delete("1.0", tk.END)
            result_display.insert(tk.END, result)
        else:
            result_display.delete("1.0", tk.END)
            result_display.insert(tk.END, "Opção inválida. Tente novamente.")

# Inicializa a janela principal
app = ctk.CTk()
app.title("Validador de Texto")
app.geometry("800x600")

# Configura a opção de menu
var_opcao = tk.StringVar(value="Validar Email")

# Cria o frame principal
frame_main = ctk.CTkFrame(app)
frame_main.pack(pady=20, padx=20, fill="both", expand=True)

# Adiciona um texto de entrada
text_input_label = ctk.CTkLabel(frame_main, text="Texto:")
text_input_label.pack(anchor="w")
text_input = ctk.CTkTextbox(frame_main, height=10)
text_input.pack(fill="both", expand=True)

# Adiciona as opções de validação
opcoes = [
    "Validar Email", "Validar Telefone", "Validar URL", "Validar Data", 
    "Validar Senha", "Validar CPF", "Validar CNPJ", "Buscar Palavras ou Frases",
    "Extrair Números", "Encontrar Códigos Postais", "Identificar Palavras que Contêm Letras Específicas",
    "Validar Endereço IP", "Validar Código de País", "Mostrar em forma de tabela", "Gerar Arquivo CSV"
]

opcao_menu = ctk.CTkOptionMenu(frame_main, variable=var_opcao, values=opcoes)
opcao_menu.pack(pady=10)

# Adiciona o botão de processamento
botao_processar = ctk.CTkButton(frame_main, text="Processar", command=processar_texto)
botao_processar.pack(pady=10)

# Adiciona uma área para exibir os resultados
result_display = ctk.CTkTextbox(frame_main, height=15)
result_display.pack(fill="both", expand=True)

# Definição do dicionário de validadores para uso
validadores = {
    0: ValidadorEmail,
    1: ValidadorTelefone,
    2: ValidadorURL,
    3: ValidadorData,
    4: ValidadorSenha,
    5: ValidadorCPF,
    6: ValidadorCNPJ,
    7: ValidadorPalavras,
    8: ValidadorNumeros,
    9: ValidadorCodigoPostal,
    10: ValidadorPalavrasComLetras,
    11: ValidadorIP,
    12: ValidadorCodigoPais,
    13: MostrarTabela,
    14: None  # Placeholder para gerar CSV, se necessário
}

# Executa a aplicação
app.mainloop()
