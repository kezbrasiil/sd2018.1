import socket
from datetime import datetime
from ast import literal_eval
from campo_minado_negocio import CampoMinado

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000                    # Porta que o Servidor esta
HOST = '127.0.0.1'     	       # Endereco IP do Servidor

def servidor():
    #Abrindo um socket UDP na porta 5000
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)

    jogo = CampoMinado()

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        mensagem = data.decode(ENCODE)        
        contexto = literal_eval(mensagem)

        resposta = tratamento(jogo, contexto)

        data = resposta.encode(ENCODE)
        sock.sendto(data, address)

def tratamento(jogo, contexto):
    comando = contexto["COMANDO"]

    switch = {
       "CRIAR_NOVO_JOGO": criar_novo_jogo,
       "EFETUAR_JOGADA": jogada,
       "QTD_JOGADAS": quatidade_jogadas,
       "TABULEIRO": tabuleiro,
       "JOGO_INCOMPLETO": jogo_incompleto
    }

    func = switch.get(str(comando))
    
    return func(jogo, contexto)


def tabuleiro(jogo, contexto):
    tabuleiro = jogo.tabuleiro()
    return str(tabuleiro)

def jogo_incompleto(jogo, contexto):
    return jogo.jogo_incompleto()



def quatidade_jogadas(jogo, contexto):
    jogadas = jogo.qtd_jogadas()
    return str(jogadas)


def jogada(jogo, contexto):
    linha = int(contexto.get("LINHA"))
    coluna = int(contexto.get("COLUNA"))
    
    jogada = jogo.jogada(linha,coluna)

    return str(jogada) 


def criar_novo_jogo(jogo, contexto):
    jogo.criar_novo_jogo(4,4)
    tabuleiro = jogo.tabuleiro()
    
    return str(tabuleiro)

if __name__ == "__main__":
    servidor()