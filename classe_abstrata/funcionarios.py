from abc import ABC, abstractmethod

class Funcionario(ABC):
    nome: str
    cpf: str
    __senha: int

    def __init__(self, n: str, cpf: str, s: int):
        self.nome = n
        self.cpf = cpf
        self.__senha = s

    @abstractmethod
    def autenticar(self, user: str, senha: int):
        pass

    def get_senha(self):
        return self.__senha

    def __str__ (self):
        info = f'Nome: {self.nome}'
        info += f'CPF: {self.cpf}'
        return info

class Gerente(Funcionario):

    def autenticar(self, user: str, senha: int):
        if user == self.cpf and senha == self.get_senha():
            return True
        else:
            return False

    def cancelar_operacao(self):
        return "Operacao Cancelada!"

class Operador_caixa(Funcionario):

    numero_caixa: int

    def __init__(self, n: str, cpf: str, s: int, n_cx: int):
        super().__init__(n, cpf, s)
        self.numero_caixa = n_cx

    def autenticar(self, user: str, senha: int):
        if user == str(self.numero_caixa) and senha == self.get_senha():
            return True
        else:
            return False

    def registrar_produto(self):
        return "Produto registrado!"

class Seguranca(Funcionario):
    posto: int

    def __init__(self, n: str, cpf: str, s: int, p: int):
        super().__init__(n, cpf, s)
        self.posto = p

    def autenticar(self, user: str, senha: int):
        if user == str(self.posto) and senha == self.get_senha():
            return True
        else:
            return False

    def acionar_alarme(self):
        return "Uouuuuuuouuuuuuuuouu"







