import socket
from datetime import datetime
from ast import literal_eval
from campo_minado_negocio import CampoMinado
import threading

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
        t = threading.Thread(target=tratamento, args=(jogo, sock, data, address))
        t.start()

def tratamento(jogo, sock, data, address):
    mensagem = data.decode(ENCODE)        
    contexto = literal_eval(mensagem)
    comando = contexto["COMANDO"]

    switch = {
       "CRIAR_NOVO_JOGO": criar_novo_jogo,
       "EFETUAR_JOGADA": jogada,
       "QTD_JOGADAS": quatidade_jogadas,
       "TABULEIRO": tabuleiro,
       "JOGO_INCOMPLETO": jogo_incompleto
    }

    func = switch.get(str(comando))
    data = func(jogo, contexto).encode(ENCODE)
    sock.sendto(data, address)

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