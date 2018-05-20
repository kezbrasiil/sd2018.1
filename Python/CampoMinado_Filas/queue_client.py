import zmq
import sys
import random
import campo_minado_view
from campo_minado_negocio import GAME_OVER
from campo_minado_view import VITORIA


port = "5559"
ENCODE = "UTF-8"


context = zmq.Context()
print("Conectando com o servidor...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:%s" % port)
client_id = random.randrange(1, 10005)


def enviarMensagem(comandos):

        data = comandos.encode(ENCODE)
        socket.send(data)
        #  Pega a resposta.
        message = socket.recv()
        resposta = message.decode(ENCODE)
        return resposta


def tabuleiro_show():
    tabuleiro = enviarMensagem("imprimir_tabuleiro()")
    tabuleiro = tabuleiro.replace(" ","")
    inicio = 1
    fim = 18
    for tab in range(4):
        z = tabuleiro[inicio:fim]
        print(tabuleiro[inicio:fim])
        inicio = fim + 1
        fim = fim+18



def qtd_jogadas():

    jogadas_restantes = enviarMensagem("jogadas_restantes")
    return int(jogadas_restantes)


def novoJogo():

    campo_minado_view.menu_inicial()

    opcao = int(input("Selecione uma opção: "))
    if opcao == 1:
        comandos = "criar_novo_jogo(4,4)"
        enviarMensagem(comandos)
        minas = enviarMensagem("coordenada_bomba()")
        print(minas)
    elif opcao == 9:
        sys.exit(0)
    else:
         novoJogo()



def cliente():
    novoJogo()

    tabuleiro_show()
    while qtd_jogadas() > 0:
        linha = str(input("Defina uma linha: "))
        coluna = str(input("Defina uma coluna: "))
        print("\n\n")
        resposta = enviarMensagem(comandos="jogada" + "(" + linha + "," + coluna + ")")
        if resposta == GAME_OVER:
            return resposta
        elif resposta == "Coordenadas Invalidas":
            print("-" + resposta + "-")
        tabuleiro_show()
    return VITORIA


if __name__ == "__main__":

    resposta = cliente()
    print(
        "\n--------------------------"
        "\n--------------------------"
        "\n\t" + resposta + ""
        "\n--------------------------"
        "\n--------------------------\n\n"
    )