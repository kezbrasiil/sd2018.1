# -*- coding: iso-8859-1 -*-
u"""Implementa a View do Campo Minado que se comunicarÃ¡ com Servidor via UDP"""

from socket import socket, AF_INET, SOCK_DGRAM
import sys
import re

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000
HOST = '127.0.0.1'

JOGADA_REALIZADA = "JR"
JOGADA_IRREGULAR = "JI"
ACERTOU_MINA = "AM"
JOGO_CRIADO = "JC"
JOGO_RECUPERADO = "RE"

def menu():
    print('------------------------------------------')
    print('---------------Campo Minado---------------')
    print('------------------------------------------')
    print('---    O que você quer fazer?          ---')
    print('---    1) Iniciar novo jogo            ---')
    print('---    2) Continuar um jogo            ---')
    print('---    9) Sair                         ---')
    print('------------------------------------------')
    print('------------------------------------------')
    print('------------------------------------------')
    
def inicio(sock,dest):
    menu()
    comando = input(': ')
    
    if (comando == '1'):
        sock.sendto(comando.encode(ENCODE),dest)
    elif (comando == '2'):
        sock.sendto(comando.encode(ENCODE),dest)
    elif (comando == '9'):
        print('Au revoir!')
        sys.exit(0)
    else:
        print('Comando invÃ¡lido.')
        inicio(sock, dest)

    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode(ENCODE)
    response = text.split("$")
    
    if response[0] == JOGO_CRIADO or response[0]==JOGO_RECUPERADO:
        qtdLinhas = int(response[1])
        mapaQuantidade = eval(response[2])
        maximoJogadas = int(response[3])
        dicasInicio()
        mostrarCampo(qtdLinhas,mapaQuantidade)
        print('Faltam ',maximoJogadas,' jogadas.')
        print()
        jogar(sock,dest)

def dicasInicio():
    print()
    print('-----------------------------------------------------------------------')
    print('--------------------------------ATENÇÃO--------------------------------')
    print('-----------------------------------------------------------------------')
    print('---   Digite a posição no formato L,C.                              ---')
    print('---   O primeiro número corresponde à linha, e o segundo, à coluna. ---')
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
    
def jogar(sock,dest):
    while (True):
        a = input('Informe a linha e coluna: ')
        
        if a == "q" or a == "qs":
            print('Au revoir!')
            sock.sendto(a.encode(ENCODE),dest)
            sock.close()
            sys.exit(0)
        
        padrao = re.match("[0-9],[0-9]",a)
        
        if (padrao == None):
            print('Jogada invÃ¡lida')
            print()
            continue
        
        sock.sendto(a.encode(ENCODE),dest)
        data, address = sock.recvfrom(MAX_BYTES)
        response = data.decode(ENCODE)
        response = response.split("$")
        
        if response[0] == JOGADA_IRREGULAR:
            print("Jogada invÃ¡lida")
            print()
            continue
        elif response[0] == JOGADA_REALIZADA:
            qtdLinhas = int(response[1])
            mapaQuantidade = eval(response[2])
            maximoJogadas = int(response[3])
        elif response[0] == ACERTOU_MINA:
            print("GAME OVER! VocÃª acertou uma mina!")
            inicio(sock,dest)
            
        mostrarCampo(qtdLinhas,mapaQuantidade)
        print('Faltam ',maximoJogadas,' jogadas.')
        print()

if __name__ == "__main__":
    sock = socket(AF_INET, SOCK_DGRAM)
    dest = (HOST, PORT)
    inicio(sock, dest)