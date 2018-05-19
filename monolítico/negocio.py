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
        
def salvarJogo(jogadas):
    arq = open("jogada.txt",'w')
    arq.write(str(qtdLinhas)+"\n")
    arq.write(str(minas)+"\n")
    arq.write(str(jogadas))
    arq.close()

view.menu()
comando = input(':')

qtdLinhas = 5
minas = colocaMinas(qtdLinhas)
mapaQuantidades = []
view.mostrarCampo(qtdLinhas,mapaQuantidades)
maximoJogadas = qtdLinhas*qtdLinhas-len(minas)
print('Máximo de Jogadas',maximoJogadas)

salvarJogo([])

while (True):
    a = input('digite a linha e coluna').split(',')
    a[0]=int(a[0])
    a[1]=int(a[1])
    if a[0] >= qtdLinhas or a[1] >= qtdLinhas:
        print('não pode')
        continue
    if (verificaBomba([a[0],a[1]],minas)):
    #acaba jogo
        raise SystemExit("Você acertou uma mina!")
    else:
        qtdMinas = 0
        for y in [-1,0,1]:
            for x in [-1,0,1]:
                if verificaBomba([a[0]+y,a[1]+x], minas):
                    qtdMinas += 1
        mapaQuantidades.append([[a[0],a[1]],qtdMinas])
        salvarJogo(mapaQuantidades)
    maximoJogadas -= 1
    view.mostrarCampo(qtdLinhas,mapaQuantidades)
    print('Faltam ',maximoJogadas,' jogadas.')
