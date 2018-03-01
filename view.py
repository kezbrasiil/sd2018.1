def menu():
    print('------------------')
    print('---Campo Minado---')
    print('------------------')
    print('O que você quer fazer?')
    print('1- Jogar')
    print('9- Sair')

def mostrarCampo(qtdLinhas,listaQtdBombas):
    print(qtdLinhas)    
    print(listaQtdBombas)
    for y in range(qtdLinhas):
        for x in range(qtdLinhas):
            for lista in listaQtdBombas:
                if lista[0] == [y,x]:
                    print('(' + str(lista[1]) + ')',end='')
                else:
                    print('(X)',end='')
        print()
