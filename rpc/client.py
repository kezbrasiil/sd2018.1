# -*- coding: iso-8859-1 -*-
u"""Implementa a View do Campo Minado que se comunicará com Servidor via UDP"""

from socket import socket, AF_INET, SOCK_DGRAM
import sys
import re
import zmq
import random

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5559
HOST = '127.0.0.1'

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
    
def inicio(sock):
    menu()
    comando = input(': ')
    
    if (comando == '1'):
        sock.send(comando.encode(ENCODE))
    elif (comando == '2'):
        sock.send(comando.encode(ENCODE))
    elif (comando == '9'):
        print('Au revoir!')
        sys.exit(0)
    else:
        print('Comando inválido.')
        inicio(sock)

    data = sock.recv()
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
        jogar(sock)

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
    
def jogar(sock):
    while (True):
        a = input('Informe a linha e coluna: ')
        
        if a == "q" or a == "qs":
            print('Au revoir!')
            sock.send(a.encode(ENCODE))
            sock.close()
            sys.exit(0)
        
        padrao = re.match("[0-9],[0-9]",a)
        
        if (padrao == None):
            print('Jogada inválida')
            print()
            continue
        
        sock.send(a.encode(ENCODE))
        data = sock.recv()
        response = data.decode(ENCODE)
        response = response.split("$")
        
        if response[0] == JOGADA_IRREGULAR:
            print("Jogada inválida")
            print()
            continue
        elif response[0] == JOGADA_REALIZADA:
            qtdLinhas = int(response[1])
            mapaQuantidade = eval(response[2])
            maximoJogadas = int(response[3])
        elif response[0] == ACERTOU_MINA:
            print("GAME OVER! Você acertou uma mina!")
            inicio(sock,dest)
        elif response[0] == TERMINOU:
            print('********************************************')
            print('********************************************')
            print("****************  PARABÉNS  ****************")
            print('********************************************')
            print('********************************************')
            inicio(sock,dest)
            
        mostrarCampo(qtdLinhas,mapaQuantidade)
        print('Faltam ',maximoJogadas,' jogadas.')
        print()

if __name__ == "__main__":
    context = zmq.Context()
    print("Conectando com o servidor...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:%s" % PORT)
    client_id = random.randrange(1, 10005)
    #sock = socket(AF_INET, SOCK_DGRAM)
    #dest = (HOST, PORT)
    inicio(socket)
    
