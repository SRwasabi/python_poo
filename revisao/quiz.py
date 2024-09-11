from typing import List
class Quiz:
    __acertos: int
    __erros: int

    def __init__(self, acertos: int, erros: int):
        self.__acertos = acertos
        self.__erros = erros

    def get_acertos(self):
        return self.__acertos

    def get_erros(self):
        return self.__erros

    def calcular(self):
        return self.__acertos - self.__erros

    def __str__(self):
        info = f'Acertos: {self.__acertos} Erros {self.__erros}\n'
        info += f'Total: {self.calcular()}\n\n'
        return info


class Quiz2A(Quiz):
   def calcular(self):
       return self.get_acertos() - 4 *(self.get_erros())
class Quiz3A(Quiz):
    def calcular(self):
        return self.get_acertos() - 2 *(self.get_erros())

class Aluno:
    __matricula: int
    __nome: str

    def __init__(self, mat: int, nome: str, kahoots: List[Quiz]):
        self.__matricula = mat
        self.__nome = nome
        self.__quizes = kahoots

    def __str__(self):
        info = f'Matricula: {self.__matricula}\n'
        info += f'Nome: {self.__nome}\n'
        soma = 0
        for q in self.__quizes:
            soma += q.calcular()
        info += f'Total de pontos {soma}\n'
        return info

    def get_matricula(self):
        return self.__matricula
class Disciplina:
    __nome: str
    __professor: str
    __ano: int
    __semestre: int
    __alunos: List[Aluno] = []

    def __init__(self, n: str, p: str, a: int, sem: int):
        self.__nome = n
        self.__professor = p
        self.__ano = a
        self.__semestre = sem

    def add_aluno(self, a: Aluno):
        for aluno in self.__alunos:
            if aluno.get_matricula() == a.get_matricula():
                raise Exception('Aluno ja existe!')
        self.__alunos.append(a)

    def __str__(self):
        info = f'Disciplina: {self.__nome} Professor: {self.__professor}\n'
        info += f'Ano {self.__ano} Semestre {self.__semestre}\n\n'
        for aluno in self.__alunos:
            info += f'{aluno}\n'
        return info
