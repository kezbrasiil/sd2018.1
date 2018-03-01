from random import randint
import view

def colocaMinas(qtdLinhas):
    minas = []
    qtdMinas = randint(int((qtdLinhas*qtdLinhas)/5),int((qtdLinhas*qtdLinhas)/3))
    for i in range(qtdMinas):
        linha = randint(0,qtdLinhas-1)
        coluna = randint(0,qtdLinhas-1)
        if ([linha,coluna] in minas):
            qtdMinas += 1
        else:
            minas.append([linha,coluna])
    return minas

def verificaBomba(posicao,minas):
    if (posicao[0]>=0 and posicao[1]>=0) and (posicao[0]<qtdLinhas and posicao[1]<qtdLinhas):
        if (posicao in minas):
            return True
        else:
            return False


view.menu()
comando = input(':')

qtdLinhas = 5
minas = colocaMinas(qtdLinhas)
mapaQuantidades = []
view.mostrarCampo(qtdLinhas,mapaQuantidades)
print(minas)

while (True):
    a = input('digite a linha e coluna').split(',')
    a[0]=int(a[0])
    a[1]=int(a[1])
    if (verificaBomba([a[0],a[1]],minas)):
        #acaba jogo
        print('acertou')
    else:
        qtdMinas = 0
        for y in [-1,0,1]:
            for x in [-1,0,1]:
                if verificaBomba([a[0]+y,a[1]+x], minas):
                    qtdMinas += 1
        mapaQuantidades.append([[a[0],a[1]],qtdMinas])
    view.mostrarCampo(qtdLinhas,mapaQuantidades)
