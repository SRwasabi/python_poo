from frota import *
def operar(carro: Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

    print('Infos atuais do carro')
    print(carro)
    print('\n')

if __name__ == "__main__":
    print('Cadastre o primeiro carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    kms = 0.0
    n_tanque = float(input('Digite quantos Litros tem o tanque: '))
    c_medio = float(input('Digite o consumo médio do carro: '))
    carro1 = Carro(modelo=nm_modelo, marca=nm_marca, cor=nm_cor, odometro=kms, tanque=n_tanque, consumo_medio=c_medio, motor=False)

    print('Cadastre o segundo carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    kms = 0.0
    n_tanque = float(input('Digite quantos Litros tem o tanque: '))
    c_medio = float(input('Digite o consumo médio do carro: '))
    carro2 = Carro(modelo=nm_modelo, marca=nm_marca, cor=nm_cor, odometro=kms, tanque=n_tanque, consumo_medio=c_medio, motor=False)
    '''
    Controlando dois carros até ele atingir 600 Km
    '''
    while ((carro1.get_odometro() < 600) and (carro2.get_odometro() < 600)) and ((carro1.get_tanque() > 0) or (carro2.get_tanque() > 0)):
        try:
            op = 0
            while op not in (1,2):
                op = int(input('Qual carro deseja operar? '))
            if op == 1:
                operar(carro1)
            else:
                operar(carro2)

        except Exception as e:
            print("Erro!")
            print(e)

    if carro1.motor_on:
        carro1.desligar()
    if carro2.motor_on:
        carro2.desligar()

    print(carro1)
    print(carro2)
    if carro1.get_odometro() > carro2.get_odometro():
        print('Carro 1 chegou ao seu destino primeiro')
    else:
        print('Carro 2 chegou ao seu destino primeiro')
