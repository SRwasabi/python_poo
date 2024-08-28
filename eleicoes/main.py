import pickle
#import traceback

from common import *

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'

def menu_eleitor():
    print("1-Novo Eleitor")
    print("2-Atualizar Eleitor")
    print("3-Sair")
    op = int(input("Digite a opcao [1,2,3]? "))
    while op not in (1, 2, 3):
        op = int(input("Digite a opcao [1,2,3]? "))
    return op

def menu_candidatos():
    print("1- Novo candidato")
    print("2- Listar candidato")
    print("3- Sair")
    op = int(input("Digite a opcao [1,2,3]? "))
    while op not in (1, 2, 3):
        op = int(input("Digite a opcao [1,2,3]? "))
    return op

def inserir_candidatos(candidatos):
    numero = int(input("Digite o numero: "))

    if numero in candidatos:
        raise Exception("candidatos já existe!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")

    candidato = Candidato(nome, RG, CPF, numero)
    candidatos[numero] = candidato

    with open(FILE_CANDIDATOS, "wb") as arquivo:
        pickle.dump(candidatos, arquivo)

    print("Arquivo gravado com sucesso")

def lista_candidatos(candidatos):
    for c in candidatos.values():
        print("candidatos numero: "+str(c.get_numero()))
        print("----------------------------------------")
        print(c)

def inserir_eleitor(eleitores):
    titulo = int(input("Digite o Títlulo: "))

    if titulo in eleitores:
        raise Exception("Titulo já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")
    secao = input("Digite a secao: ")
    zona = input("Digite a zona: ")

    eleitor = Eleitor(nome, RG, CPF, titulo, secao, zona)
    eleitores[eleitor.get_titulo()] = eleitor

    with open(FILE_ELEITORES, 'wb') as arquivo:
        pickle.dump(eleitores, arquivo)

    print('Eleitor gravado com sucesso!')
    print(eleitor)

def atualizar_eleitor(eleitores):
    titulo = int(input('Digite o titulo do eleitor: '))

    if titulo in eleitores:
        eleitor = eleitores[titulo]
        print(eleitor)
        secao = input("Digite a nova secao: ")
        zona = input("Digite a nova zona: ")
        eleitor.secao = secao
        eleitor.zona = zona

        with open(FILE_ELEITORES, 'wb') as arquivo:
            pickle.dump(eleitores, arquivo)

        print('Atualizados dados do eleitor!')
        print(eleitor)
    else:
        raise Exception('Titulo inexistente')

if __name__ == "__main__":
    eleitores = {} #dicionário a chave será o titulo
    candidatos = {}
    try:
        print("Carregando arquivo de eleitores ...")

        with open(FILE_ELEITORES, 'rb') as arquivo:
            eleitores = pickle.load(arquivo)

        print("Carregando arquivo de candidatos...")
        with open(FILE_CANDIDATOS, "rb") as arquivo:
            candidatos = pickle.load(arquivo)

    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum eleitor carregado!")

    op_user = 0
    while op_user not in (1,2):
        op_user = int(input("Gerenciar 1- candidatos; 2- Eleitores [1,2]: "))

        if op_user == 1:
            opcao = 1
            while opcao in (1, 2, 3):
                try:
                    opcao = menu_candidatos()

                    if opcao == 1:
                        inserir_candidatos(candidatos)
                    elif opcao == 2:
                        lista_candidatos(candidatos)
                    elif opcao == 3:
                        print("Saindo!")
                        break

                except Exception as e:
                    # traceback.print_exc()
                    print(e)

        else:
            opcao = 1
            while opcao in (1, 2, 3):
                try:
                    opcao = menu_eleitor()

                    if opcao == 1:
                        inserir_eleitor(eleitores)
                    elif opcao == 2:
                        atualizar_eleitor(eleitores)
                    elif opcao == 3:
                        print("Saindo!")
                        break
                except Exception as e:
                    # traceback.print_exc()
                    print(e)