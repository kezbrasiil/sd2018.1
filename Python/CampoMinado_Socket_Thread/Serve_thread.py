u"""Esse módulo possui a implementação de um servidor UDP."""
from socket import socket, AF_INET, SOCK_DGRAM
from campo_minado_negocio import CampoMinado
from class_thread import ThreadTratador

ENCODE = "UTF-8"
MAX_BYTES = 65535
PORT = 5000
HOST = ''

def server():
    # Abrindo uma porta UDP
    orig = (HOST, PORT)
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(orig)
    jogo = CampoMinado()

    while True:
        # recebi dados
        data, address = sock.recvfrom(MAX_BYTES)

        # Criação de thread orientada a objeto
        tratador = ThreadTratador(sock, data, address,jogo)
        tratador.start()


if __name__ == "__main__":
    server()
