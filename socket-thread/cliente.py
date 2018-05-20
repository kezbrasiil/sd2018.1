import sys
from ast import literal_eval
from socket import socket, AF_INET, SOCK_DGRAM
from datetime import datetime

ENCODE = "UTF-8"
HOST = '127.0.0.1'   # Endereco IP do Servidor
PORT = 5000          # Porta que o Servidor esta
MAX_BYTES = 65535    # Quantidade de Bytes a serem ser recebidos

def enviar(comando):
    dest = (HOST, PORT)
    sock = socket(AF_INET, SOCK_DGRAM)

    data = comando.encode(ENCODE)
    sock.sendto(data, dest)

    data, address = sock.recvfrom(MAX_BYTES)
    respota = data.decode(ENCODE)

    sock.close()

    return respota
"""Função para receber as jogadas e enviar para o servidor"""

def menu():
    print("---------------------------------------")
    print("------------ Campo Minado -------------")
    print("---------------------------------------")
    print("\n")
    print(" Selecione uma opção")
    print("1. Criar novo jogo")
    print("9. Sair do Jogo")

def sair():
    sys.exit(0)
    
def qtd_jogadas():
    contexto = {"COMANDO": "QTD_JOGADAS"}
    comando = str(contexto)

    resposta = literal_eval(enviar(comando))
    return (str(resposta))

def imprimir_tabuleiro():
    contexto = {"COMANDO": "TABULEIRO"}
    comando = str(contexto)
    resposta = literal_eval(enviar(comando))

    for posicao in resposta:
        print (str(posicao))

def tratar_jogadas():
    while True:
        contexto = {"COMANDO": "EFETUAR_JOGADA"}
        contexto["LINHA"] = input("Informe a linha: ")
        contexto["COLUNA"] = input("Informe a coluna: ")
        
        comando = str(contexto)

        resposta = enviar(comando)
        
        if resposta == "Game Over":
            print("GAMEOVER")
            sair()

        qtd = qtd_jogadas()
        print('jogadas restantes', qtd)
        
        imprimir_tabuleiro()

def iniciar_novo_jogo():
    contexto = {"COMANDO": "CRIAR_NOVO_JOGO"}

    comando = str(contexto)

    return literal_eval(enviar(comando))

def cliente():

    switcher = {
        1: iniciar_novo_jogo,
        9: sair,
    }

    while True:
        menu()
        opcao = int(input("Opção escolhida: "))

        func = switcher.get(opcao)
        
        resposta = func()

        for posicao in resposta:
             print (str(posicao))
        # print(resposta)

        tratar_jogadas()

if __name__ == "__main__":
    cliente()