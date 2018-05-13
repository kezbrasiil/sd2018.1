# -*- iso-8859-1 -*-
#Biblioteca para lidar com SO
import sys
#Importando classe Campo minado que é o negocio
from campo_minado_negocio import CampoMinado
#importar uma string chamada coordenadas invalidas
from campo_minado_negocio import COORDENADAS_INVALIDAS
#importar uma string chamada Game over
from campo_minado_negocio import GAME_OVER
#importar uma string chamada Jogada segura
from campo_minado_negocio import JOGADA_SEGURA
import os

INSTANCIA = "instancia"
VITORIA = "Parabéns você venceu"

""" 
    1. Menu para iniciar o jogo
    2. Menu declara jogada
    3. Regra pra vitória
    
    4. Salvar jogadas
    5. Continuar jogo 
 """

#Objeto é uma instancia do campo minado

def menu_inicial():
    os.system('cls')
    print("---------------------------------------")
    print("------------ Campo Minado -------------")
    print("---------------------------------------")
    print("\n")
    #print(" Selecione uma opção")
    print("1. Criar novo jogo")
    print("9. Sair do Jogo")

def iniciar_novo_jogo(contexto):

    #recebe a instancia do objeto
    #Cria novo jogo
    contexto.criar_novo_jogo(4,4)
    #Imprimi tabuleiro
    contexto.imprimir_tabuleiro()

    return efetuar_nova_jogada(contexto)




def continuar_jogo(contexto):
    pass

def efetuar_nova_jogada(contexto):

    #objeto = contexto.get(INSTANCIA)

    while contexto.jogadas_restantes > 0:
        linha = int(input("Defina uma linha: "))
        coluna = int(input("Defina uma coluna: "))
        if contexto.jogada(linha,coluna) == GAME_OVER:
            return GAME_OVER
        contexto.imprimir_tabuleiro()
    
    return VITORIA

def sair(contexto):
    sys.exit(0)

#definicao do Main
if __name__ == "__main__":

#Inserir as funcoes dentro de um dicionario
    switcher = {
        1: iniciar_novo_jogo,
        9: sair,
    }

#Instancia do campo minado
    objeto = CampoMinado()
#recebe dicionario chamado INSTANCIA:CAMPO MINADO
    contexto = {INSTANCIA: objeto}
    
    while True:
        #Chama a funcao que imprimir a tela inicial passando a instancia para manipulacao
        menu_inicial()

        #recebe uma opcao e armazena
        opcao = int(input("Opção escolhida: "))

        #armazena uma funcao com base na opcao escolhida
        func = switcher.get(opcao)


        #chama um metodo passando a classe campo minado como argumento
        print(func(objeto))



