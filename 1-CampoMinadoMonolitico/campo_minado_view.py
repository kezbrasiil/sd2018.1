from campo_minado_negocio import CampoMinado
from os.path import isfile
from os import remove
import json
import sys

tabuleiro = CampoMinado(2, 2)

def menu():
    print("*****************************************")
    print("*              CAMPO MINADO             *")
    print("*****************************************")
    print("1 - INICIAR JOGO                         ")
    print("2 - RESTAURAR                            ")
    print("3 - SAIR                                 ")
    print("*****************************************\n")
    opcao = int(input("Digite uma Opção :"))
    if opcao == 1:
        start()
    elif opcao == 2:
        partida()
    else:
        pass

def start ():
    if tabuleiro.proximaJogada():
        tabuleiro.imprimirTabuleiro()
        linha = int(input("Digite a posição da linha :"))
        coluna = int(input("Digite a posição da coluna :"))
        tabuleiro.jogada(linha,coluna)
        start()
    else:
        print("Fim de jogo")


def partida():
    if isfile("game.json"):
        arquivo = open("game.json")
        game = json.loads(arquivo.read())
        tabuleiro.restaurar(game)
        arquivo.close()
        start()
    else:
        print("Não existe Jogo salvo!\n")

menu()
