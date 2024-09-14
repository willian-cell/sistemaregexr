from validadores import *
from mostrar_tabela import MostrarTabela

def mostrar_resultados(opcao, texto):
    validadores = {
        0: exit,
        1: ValidadorEmail,
        2: ValidadorTelefone,
        3: ValidadorURL,
        4: ValidadorData,
        5: ValidadorSenha,
        6: ValidadorCPF,
        7: ValidadorCNPJ,
        8: lambda texto: ValidadorPalavras(texto, input("Digite a palavra a ser buscada: ")),
        9: ValidadorNumeros,
        10: ValidadorCodigoPostal,
        11: lambda texto: ValidadorPalavrasComLetras(texto, input("Digite as letras a serem encontradas nas palavras: ")),
        12: ValidadorIP,
        13: ValidadorCodigoPais,
        14: MostrarTabela,
    }

    if opcao in validadores:
        validador = validadores[opcao](texto)
        if hasattr(validador, 'mostrar'):
            validador.mostrar()
        else:
            validador.exibir_resultado()
    else:
        print("Opção inválida. Tente novamente.")

def menu():
    texto = """
    Meu e-mail é exemplo@dominio.com e meu número de telefone é +55 11 98765-4321.
    A URL do meu site é https://www.exemplo.com.br.
    A data de hoje é 09/09/2024.
    A senha segura é Exemplo@123.
    Meu CPF é 123.456.789-00 e meu CNPJ é 12.345.678/0001-95.
    Os números são 123, 456.78, e o código postal é 12345-678.
    A palavra chave abc está aqui.
    O endereço IP é 192.168.0.1 e o código de país é BR.
    segundo codigo postal 72900-314
    """

    while True:
        print("\nMenu de Busca")
        print("1. Validar Email")
        print("2. Validar Telefone")
        print("3. Validar URL")
        print("4. Validar Data (DD/MM/YYYY)")
        print("5. Validar Senha")
        print("6. Validar CPF")
        print("7. Validar CNPJ")
        print("8. Buscar Palavras ou Frases")
        print("9. Extrair Números")
        print("10. Encontrar Códigos Postais")
        print("11. Identificar Palavras que Contêm Letras Específicas")
        print("12. Validar Endereço IP")
        print("13. Validar Código de País")
        print("14. Mostrar em forma de tabela")
        print("15. Gerar Arquivo CSV")
        print("0. Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            continue

        if opcao == 0:
            print("Saindo...")
            break

        mostrar_resultados(opcao, texto)

if __name__ == "__main__":
    menu()
