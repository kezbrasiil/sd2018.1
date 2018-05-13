u"""Esse módulo possui a implementação de um servidor UDP."""
from socket import socket, AF_INET, SOCK_DGRAM
from campo_minado_negocio import CampoMinado
import time

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000
HOST = ''

def server():
    u"""Essa função implementa um servidor que faz uso de um socket UDP"""

    orig = (HOST, PORT)
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(orig)

    jogo = CampoMinado()

    while True:

        data, address = sock.recvfrom(MAX_BYTES)
        mensagem = data.decode(ENCODE)
        funcao = "jogo." + mensagem  # transformar a string na função

        resposta = eval(funcao)
        valor = str(resposta).encode(ENCODE)
        sock.sendto(valor, address)


if __name__ == "__main__":
    server()
