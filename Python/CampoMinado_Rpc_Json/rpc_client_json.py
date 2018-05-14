import sys
from jsonrpclib import Server
import os
from campo_minado_negocio import GAME_OVER




def client():
    proxy = Server('http://localhost:7002')
    print(proxy.printName("André", "Bessa"))


def menu_inicial():
    os.system('cls')
    print("---------------------------------------")
    print("------------ Campo Minado -------------")
    print("---------------------------------------")
    print("\n")
    #print(" Selecione uma opção")
    print("1. Criar novo jogo")
    print("9. Sair do Jogo")


def iniciar_novo_jogo(proxy):

    #Cria novo jogo
    proxy.criar_novo_jogo(4,4)
    #Imprimi tabuleiro
    imprimir_tabuleiro(proxy.retorna_tabuleiro(),proxy.bombas())

    efetuar_nova_jogada(proxy)


def efetuar_nova_jogada(proxy):
    # objeto = contexto.get(INSTANCIA)

    while proxy.jogadas_restantes() > 0:
        linha = int(input("Defina uma linha: "))
        coluna = int(input("Defina uma coluna: "))
        print("\n"*2)
        if proxy.jogada(linha, coluna) == GAME_OVER:
            print("\n\n----- Fim de Jogo -----\n\n")
            return GAME_OVER
        imprimir_tabuleiro(proxy.retorna_tabuleiro(), proxy.bombas())

    print("\n\n----- Vitoria -----\n\n")
    return "VITORIA"

def imprimir_tabuleiro(tabuleiro,coordenadas_bombas):
    print(coordenadas_bombas)
    for tab in tabuleiro:
        print(tab)


def sair(proxy):
    sys.exit(0)

def client():

    proxy = Server('http://localhost:7002')

    # Inserir as funcoes dentro de um dicionario
    switcher = {
        1: iniciar_novo_jogo,
        9: sair,
    }


    while True:
        menu_inicial()
        opcao = int(input("Opção escolhida: "))
        func = switcher.get(opcao)
        func(proxy)