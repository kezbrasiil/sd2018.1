def menu():
    print('------------------')
    print('---Campo Minado---')
    print('------------------')
    print('O que você quer fazer?')
    print('1- Jogar')
    print('9- Sair')

def mostrarCampo(qtdLinhas,listaQtdBombas):

    for y in range(qtdLinhas):
        for x in range(qtdLinhas):
            if [y,x] in [a[0] for a in listaQtdBombas]:
                for a in listaQtdBombas:
                    if a[0] == [y,x]:
                        print('(' + str(a[1]) + ')',end='')
                        break
            else:
                print('(X)',end='')
        print()
                
