from quiz import *

if __name__ == '__main__':
    q1 = Quiz(10,2)
    q2 = Quiz2A(5,7)
    q3 = Quiz3A(11, 1)

    print(q1)
    print(q2)
    print(q3)
    lista_qs = [q1, q2, q3]
    a1 = Aluno(1, "Raphael", lista_qs)
    a2 = Aluno(2, "Thalyta", lista_qs)
    a3 = Aluno(nome="Thais", mat=3, kahoots=lista_qs)

    print(a1)
    print(a2)

    d = Disciplina("POO", "Feruache", 2024, 4)
    d.add_aluno(a1)
    d.add_aluno(a2)
    d.add_aluno(a3)
    print(d)
