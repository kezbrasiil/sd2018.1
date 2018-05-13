u"""Esse módulo possui a implementação de um cliente UDP. """
from socket import socket, AF_INET, SOCK_DGRAM
import campo_minado_view
import sys
from campo_minado_negocio import GAME_OVER
from campo_minado_view import VITORIA
from os import system

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000
HOST = '127.0.0.1'




def decode(lista):
    if isinstance(lista, list):
        return [decode(x) for x in lista]
    else:
        return lista.decode('utf-8')


def tabuleiro_show():
    tabuleiro = enviarComandoServidor("imprimir_tabuleiro()")
    tabuleiro = tabuleiro.replace(" ","")
    inicio = 1
    fim = 18
    for tab in range(4):
        z = tabuleiro[inicio:fim]
        print(tabuleiro[inicio:fim])
        inicio = fim + 1
        fim = fim+18


def novoJogo():


    campo_minado_view.menu_inicial()

    opcao = int(input("Selecione uma opção: "))
    if opcao == 1:
        comandos = "criar_novo_jogo(4,4)"
        enviarComandoServidor(comandos)
        minas = enviarComandoServidor("coordenada_bomba()")
        print(minas)
    elif opcao == 9:
        sys.exit(0)
    else:
         novoJogo()



def enviarComandoServidor(comandos):
    u"""Procedimento responsável por enviar dados para o servidor e receber alguma resposta por conta disso."""

    data = comandos.encode(ENCODE)

    sock = socket(AF_INET, SOCK_DGRAM)
    dest = (HOST, PORT)

    #Enviar
    sock.sendto(data, dest)

    data, address = sock.recvfrom(MAX_BYTES)
    resposta = data.decode(ENCODE)
    sock.close()  # Fechando Socket

    return resposta

def qtd_jogadas():

    jogadas_restantes = enviarComandoServidor("jogadas_restantes")
    return int(jogadas_restantes)

def client():

    novoJogo()
    tabuleiro_show()
    while qtd_jogadas() > 0:
        linha = str(input("Defina uma linha: "))
        coluna = str(input("Defina uma coluna: "))
        print("\n\n")
        resposta = enviarComandoServidor(comandos="jogada" + "(" + linha + "," + coluna + ")")
        if  resposta == GAME_OVER:
            return resposta
        elif resposta == "Coordenadas Invalidas":
            print("-"+resposta+"-")
        tabuleiro_show()
    return VITORIA





if __name__ == "__main__":

    while True:
        for x in range(20):
            resposta = client()
            print(
                "\n--------------------------"
                "\n--------------------------"
                "\n\t"+resposta+""
                "\n--------------------------"
                "\n--------------------------\n\n\n"
            )



