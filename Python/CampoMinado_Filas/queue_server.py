import zmq
import time
import sys
import random
from campo_minado_negocio import CampoMinado


def server():
    try:
        port = "5560"
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.connect("tcp://localhost:%s" % port)
        server_id = random.randrange(1,10005)
        jogo = CampoMinado()

        while True:
            #  Espera pela próxima requisição do cliente

            data = socket.recv()
            print("Recebi requisição de : ", data)
            mensagem = data.decode("UTF-8")

            funcao = "jogo." + mensagem  # transformar a string na função

            time.sleep (1)

            #resposta
            resposta = str(eval(funcao))
            data = resposta.encode("UTF-8")
            socket.send(data)

    except:
        for val in sys.exc_info():
            print(val)

    input("Saida Enter")

if __name__ == "__main__":
    server()
