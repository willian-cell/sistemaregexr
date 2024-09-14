# validadores.py

import re

class Validador:
    def __init__(self, texto):
        self.texto = texto

    def validar(self):
        raise NotImplementedError("Método 'validar' não implementado.")

    def exibir_resultado(self):
        resultados = self.validar()
        return '\n'.join(resultados) if resultados else "Nenhum resultado encontrado."

class ValidadorEmail(Validador):
    def validar(self):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(pattern, self.texto)

class ValidadorTelefone(Validador):
    def validar(self):
        pattern = r'(?:\+55\s?)?\(?\d{2}\)?\s?\d{4,5}-\d{4}'
        return re.findall(pattern, self.texto)

class ValidadorURL(Validador):
    def validar(self):
        pattern = r'\b((http|https):\/\/)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(\.[a-zA-Z]{2})?(\S*)\b'
        return re.findall(pattern, self.texto)

class ValidadorData(Validador):
    def validar(self):
        pattern = r'\b\d{2}/\d{2}/\d{4}\b'
        return re.findall(pattern, self.texto)

class ValidadorSenha(Validador):
    def validar(self):
        pattern_validacao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        pattern_extracao = r'\b[A-Za-z0-9@#\$%\^\&\*\(\)_\+\-]{8,}\b'
        senhas_encontradas = re.findall(pattern_extracao, self.texto)
        return [senha for senha in senhas_encontradas if re.match(pattern_validacao, senha)]

class ValidadorCPF(Validador):
    def validar(self):
        pattern = r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b'
        return re.findall(pattern, self.texto)

class ValidadorCNPJ(Validador):
    def validar(self):
        pattern = r'\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b'
        return re.findall(pattern, self.texto)

class ValidadorPalavras(Validador):
    def __init__(self, texto, palavra):
        super().__init__(texto)
        self.palavra = palavra

    def validar(self):
        pattern = rf'(?i)\b{self.palavra}\b'
        return re.findall(pattern, self.texto)

class ValidadorNumeros(Validador):
    def validar(self):
        pattern = r'\b\d+(\.\d+)?\b'
        return re.findall(pattern, self.texto)

class ValidadorCodigoPostal(Validador):
    def validar(self):
        pattern = r'\b\d{5}-\d{3}\b'
        return re.findall(pattern, self.texto)

class ValidadorPalavrasComLetras(Validador):
    def __init__(self, texto, letras):
        super().__init__(texto)
        self.letras = letras

    def validar(self):
        pattern = rf'\b\w*{self.letras}\w*\b'
        return re.findall(pattern, self.texto)

class ValidadorIP(Validador):
    def validar(self):
        pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
        return re.findall(pattern, self.texto)

class ValidadorCodigoPais(Validador):
    def validar(self):
        pattern = r'\b[A-Z]{2}\b'
        return re.findall(pattern, self.texto)
