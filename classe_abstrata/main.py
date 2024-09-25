from funcionarios import *

if __name__ == "__main__":
    g = Gerente("Joao", "12345", 1234)
    print(g)
    if g.autenticar("12345", 1234):
        print(g.cancelar_operacao())
    else:
        print("Falha na autenticacao")

    op = Operador_caixa("Maria", "23231", 4321, 1)
    print(op)
    if op.autenticar("1", 4321):
        print(op.registrar_produto())
    else:
        print("Falha na autenticacao")

    seg = Seguranca("Jose", "333333", 2233, 34)
    print(seg)
    if seg.autenticar("34", 2233):
        print(seg.acionar_alarme())
    else:
        print("Falha na autenticacao")