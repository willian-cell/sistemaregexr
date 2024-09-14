# mostrar_tabela.py

import csv
from tabulate import tabulate

class MostrarTabela:
    def __init__(self, texto, arquivo_csv='cadastros.csv'):
        self.texto = texto
        self.arquivo_csv = arquivo_csv

    def mostrar(self):
        regex_padroes = {
            'E-mail': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
            'Telefone': r'\+\d{2} \d{2} \d{5}-\d{4}',
            'URL': r'https?://[^\s]+',
            'Data': r'\d{2}/\d{2}/\d{4}',
            'Senha': r'[A-Za-z0-9@#\$%\^\&\*\(\)_\+\-]+',
            'CPF': r'\d{3}\.\d{3}\.\d{3}-\d{2}',
            'CNPJ': r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}',
            'Números': r'\d+(?:\.\d+)?',
            'Código Postal': r'\d{5}-\d{3}',
            'Palavra-Chave': r'\b[a-zA-Z]+\b',
            'Endereço IP': r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
            'Código de País': r'\b[A-Z]{2}\b'
        }

        dados = []

        for tipo, padrao in regex_padroes.items():
            encontrados = re.findall(padrao, self.texto)
            if encontrados:
                for item in encontrados:
                    dados.append([tipo, item])

        cabecalho = ['Tipo de Informação', 'Valor']
        print("\nTabela de Informações Extraídas:")
        print(tabulate(dados, headers=cabecalho, tablefmt="grid"))

        self._gerar_csv()
        self._mostrar_csv()

    def _gerar_csv(self):
        regex_padroes = {
            'E-mail': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
            'Telefone': r'\+\d{2} \d{2} \d{5}-\d{4}',
            'URL': r'https?://[^\s]+',
            'Data': r'\d{2}/\d{2}/\d{4}',
            'Senha': r'[A-Za-z0-9@#\$%\^\&\*\(\)_\+\-]+',
            'CPF': r'\d{3}\.\d{3}\.\d{3}-\d{2}',
            'CNPJ': r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}',
            'Números': r'\d+(?:\.\d+)?',
            'Código Postal': r'\d{5}-\d{3}',
            'Palavra-Chave': r'\b[a-zA-Z]+\b',
            'Endereço IP': r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
            'Código de País': r'\b[A-Z]{2}\b'
        }

        dados = []

        for tipo, padrao in regex_padroes.items():
            encontrados = re.findall(padrao, self.texto)
            if encontrados:
                for item in encontrados:
                    dados.append([tipo, item])

        with open(self.arquivo_csv, 'w', newline='') as csvfile:
            fieldnames = ['Tipo de Informação', 'Valor']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for linha in dados:
                writer.writerow({'Tipo de Informação': linha[0], 'Valor': linha[1]})

    def _mostrar_csv(self):
        with open(self.arquivo_csv, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            csv_dados = [row for row in reader]

        print("\nTabela de Cadastros:")
        print(tabulate(csv_dados, headers='keys', tablefmt="grid"))
