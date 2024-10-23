from abc import ABC, abstractmethod
from typing import List


class Operacao(ABC):
    operador: float

    def __init__(self, n):
        self.operador = n

    @abstractmethod
    def calcular(self, n: float):
        pass

    def calcular_inverso(self, n: float):
        pass


class Adicao(Operacao):
    def calcular(self, n):
        return n + self.operador

    def calcular_inverso(self, n):
        return n - self.operador


class Subtracao(Operacao):

    def calcular(self, n):
        return n - self.operador

    def calcular_inverso(self, n):
        return n + self.operador


class Divisao(Operacao):

    def calcular(self, n):
        return n / self.operador

    def calcular_inverso(self, n):
        return n * self.operador


class Multiplicacao(Operacao):

    def calcular(self, n):
        return n * self.operador

    def calcular_inverso(self, n):
        return n / self.operador


class Calculadora:
    resultado: float
    operacoes: List[Operacao]

    def __init__(self):
        self.resultado = 0
        self.operacoes = []

    def add_operacao(self, op: Operacao):
        self.operacoes.append(op)

    def desfazer_ultima(self):
        op = self.operacoes.pop()
        self.resultado = op.calcular_inverso(self.resultado)

    def calcular_total(self):
        calculo = 0
        for op in self.operacoes:
            calculo = op.calcular(calculo)
        self.resultado = calculo


if __name__ == '__main__':
    calc = Calculadora()
    print(f'>> {calc.resultado}')
    op = input('>> ')

    while op != 'q':
        if op == '+' or op == '-' or op == '*' or op == '/':
            n = float(input('>> '))

            if op == '+':
                o = Adicao(n)
            elif op == '-':
                o = Subtracao(n)
            elif op == '*':
                o = Multiplicacao(n)
            elif op == '/':
                o = Divisao(n)

            calc.add_operacao(o)
        elif op == '=':
            calc.calcular_total()
            print(f'>> {calc.resultado}')
        elif op == 'd':
            calc.desfazer_ultima()
            print(f'>> {calc.resultado}')
        op = input('>> ')
