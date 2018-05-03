# -*- coding: iso-8859-1 -*-
u"""Implementa a View do Campo Minado que se comunicará com Servidor via UDP"""

import rpyc

JOGADA_REALIZADA = "JR"
JOGADA_IRREGULAR = "JI"
ACERTOU_MINA = "AM"
JOGO_CRIADO = "JC"
JOGO_RECUPERADO = "RE"
TERMINOU = "TR"

def menu():
    print('------------------------------------------')
    print('---------------Campo Minado---------------')
    print('------------------------------------------')
    print('---    O que voc� quer fazer?          ---')
    print('---    1) Iniciar novo jogo            ---')
    print('---    2) Continuar um jogo            ---')
    print('---    9) Sair                         ---')
    print('------------------------------------------')
    print('------------------------------------------')
    print('------------------------------------------')
    
def inicio(proxy):
    menu()
    comando = input(': ')
    
    if (comando == '1'):
        jogo = proxy.FUNCAOCRIARJOGO
    elif (comando == '2'):
        jogo = proxy.FUNCAOCONTINUARJOGO
    elif (comando == '9'):
        print('Au revoir!')
        sys.exit(0)
    else:
        print('Comando inválido.')
    
    if jogo[0] == JOGO_CRIADO or jogo[0]==JOGO_RECUPERADO:
        qtdLinhas = int(jogo[1])
        mapaQuantidade = eval(jogo[2])
        maximoJogadas = int(jogo[3])
        dicasInicio()
        mostrarCampo(qtdLinhas,mapaQuantidade)
        print('Faltam ',maximoJogadas,' jogadas.')
        print()
        jogar(proxy)

def dicasInicio():
    print()
    print('-----------------------------------------------------------------------')
    print('--------------------------------ATEN��O--------------------------------')
    print('-----------------------------------------------------------------------')
    print('---   Digite a posi��o no formato L,C.                              ---')
    print('---   O primeiro n�mero corresponde � linha, e o segundo, � coluna. ---')
    print('---   Caso deseja sair sem salvar, digite q.                        ---')
    print('---   Para salvar e sair, digite qs.                                ---')
    print('---   Bom jogo!                                                     ---')
    print('-----------------------------------------------------------------------')
    print('-----------------------------------------------------------------------')
    print()
    input('Pressione uma tecla para continuar')
    
def mostrarCampo(qtdLinhas,listaQtdBombas):
    print()
    print('   0   1   2   3   4')
    linha = 0
    for y in range(qtdLinhas):
        print(str(linha) + ' ',end='')
        for x in range(qtdLinhas):
            if [y,x] in [a[0] for a in listaQtdBombas]:
                for a in listaQtdBombas:
                    if a[0] == [y,x]:
                        print('(' + str(a[1]) + ') ',end='')
                        break
            else:
                print('(X) ',end='')
        print()
        linha += 1            
    
def jogar(proxy):
    while (True):
        a = input('Informe a linha e coluna: ')
        
        if a == "q": 
            proxy.SAIRDOJOGOSEMSALVAR
        elif a == "qs":
            proxy.SAIRDOJOGOSALVANDO
        
        padrao = re.match("[0-9],[0-9]",a)
        if (padrao == None):
            print('Jogada inválida')
            print()
            continue
        
        jogo = proxy.jogar(a)
                
        if jogo[0] == JOGADA_IRREGULAR:
            print("Jogada inválida")
            print()
            continue
        elif jogo[0] == JOGADA_REALIZADA:
            qtdLinhas = int(jogo[1])
            mapaQuantidade = eval(jogo[2])
            maximoJogadas = int(jogo[3])
        elif jogo[0] == ACERTOU_MINA:
            print("GAME OVER! Você acertou uma mina!")
            inicio(proxy)
        elif jogo[0] == TERMINOU:
            print('********************************************')
            print('********************************************')
            print("****************  PARABÉNS  ****************")
            print('********************************************')
            print('********************************************')
            inicio(proxy)
            
        mostrarCampo(qtdLinhas,mapaQuantidade)
        print('Faltam ',maximoJogadas,' jogadas.')
        print()

if __name__ == "__main__":
    config = {'allow_public_attrs': True}
    proxy = rpyc.connect('localhost', 18861, config=config)
    inicio(proxy)
    
