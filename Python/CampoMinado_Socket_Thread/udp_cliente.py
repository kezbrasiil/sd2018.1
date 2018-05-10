u"""Esse módulo possui a implementação de um cliente UDP. """
from socket import socket, AF_INET, SOCK_DGRAM
import campo_minado_view
import sys
from campo_minado_negocio import GAME_OVER
from campo_minado_view import VITORIA

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000
HOST = '127.0.0.1'





def tabuleiro_show():
    tabuleiro = list(enviarComandoServidor("imprimir_tabuleiro()"))
    for tab in tabuleiro:
        print(tab)

def novoJogo():
    campo_minado_view.menu_inicial()

    opcao = int(input("Selecione uma opção: "))
    if opcao == 1:
        comandos = "criar_novo_jogo(4,4)"
        enviarComandoServidor(comandos)
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
        resposta = enviarComandoServidor(comandos="jogada" + "(" + linha + "," + coluna + ")")
        if  resposta == GAME_OVER:
            return resposta
        elif resposta == "Coordenadas Invalidas":
            print("-"+resposta+"-")
        tabuleiro_show()
    return VITORIA





if __name__ == "__main__":
    print(
        "\n--------------------------"
        "\n--------------------------"
        "\n\t"+client()+""
        "\n--------------------------"
        "\n--------------------------"
    )



