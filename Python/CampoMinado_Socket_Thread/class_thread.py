# coding: utf-8
import threading

ENCODE = "UTF-8"
"""
MAX_BYTES = 65535
PORT = 5000  # Porta que o servidor escuta
HOST = ''  # Endereco IP do Servidor


def server_thread_oo():
    # Abrindo uma porta UDP
    orig = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(orig)
    while True:
        # recebi dados
        data, address = sock.recvfrom(MAX_BYTES)

        # Criação de thread orientada a objeto
        tratador = ThreadTratador(sock, data, address)
        tratador.start()
"""

class ThreadTratador(threading.Thread):

    def __init__(self, sock, data, address,jogo):
        threading.Thread.__init__(self)
        self.sock = sock
        self.data = data
        self.address = address
        self.jogo = jogo

    def run(self):
        self.__tratar_conexao(self.sock, self.data, self.address,self.jogo)

    def __tratar_conexao(self, sock, data, address,jogo):

        mensagem = data.decode(ENCODE)
        funcao = "jogo." + mensagem  # transformar a string na função

        resposta = eval(funcao)
        valor = str(resposta).encode(ENCODE)
        sock.sendto(valor, address)
    '''
        print(text)
        # Envia resposta
        text = "Quantidade de bytes enviados: " + str(len(data))
        data = text.encode(ENCODE)
        sock.sendto(data, address)
    '''
