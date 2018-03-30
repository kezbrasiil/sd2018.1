from random import randint
from ast import literal_eval
import os.path
from socket import socket, AF_INET, SOCK_DGRAM

class CampoMinadoNegocio(object):

    ENCODE = "UTF-8"
    MAX_BYTES = 65535
    PORT = 5000
    HOST = ''

    def __init__(self):
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.origem = (self.HOST, self.PORT)
        self.sock.bind(self.origem)

        self.__contador = 0
        self.__bombas = []
        self.__gerar_bombas()
        self.imprimir_bombas()

    def server(self):
        print("[Servidor Ativo]\n")
        while True:
            datos, endereco = self.sock.recvfrom(self.MAX_BYTES)
            texto = datos.decode(self.ENCODE)

            print("[Mensagem Recebida] " + texto)

            if '(' in texto:
                self.__incrementar_jogada()
                tupla = literal_eval(texto)
                retorno = self.__tem_bomba(tupla)
                if retorno:
                    texto = "sim"
                else:
                    texto = self.__bombas_vizinhas(tupla)
            elif texto == "jogador venceu?":
                texto = self.__vitoria()
            elif texto == "numero de jogadas?":
                texto = str(self.__contador)
            
            print("[Enviando Resposta] " + texto)   

            dados = texto.encode(self.ENCODE)
            self.sock.sendto(dados, endereco)

            print("[Fim da Requisição]\n")

    def __gerar_bombas(self):
        while(len(self.__bombas) < 14):
            linha = randint(0,5)
            coluna = randint(0,8)
            tupla = (linha,coluna)
            if tupla not in self.__bombas:
                self.__bombas.append(tupla)
    
    def __incrementar_jogada(self):
        self.__contador = self.__contador + 1
        return self.__contador

    def __tem_bomba(self, tupla):
        var = False
        if tupla in self.__bombas:
            var = True
        return var
    
    def __bombas_vizinhas(self, tupla):
        lista = []
        lista.append((tupla[0]-1,tupla[1]-1))
        lista.append((tupla[0]-1,tupla[1]))
        lista.append((tupla[0]-1,tupla[1]+1))
        lista.append((tupla[0],tupla[1]-1))
        lista.append((tupla[0],tupla[1]+1))
        lista.append((tupla[0]+1,tupla[1]-1))
        lista.append((tupla[0]+1,tupla[1]))
        lista.append((tupla[0]+1,tupla[1]+1))
        
        qtd_bombas = [i for i in self.__bombas if i in lista]
        return str(len(qtd_bombas))
    
    def __vitoria(self):
        var = "nao"
        if self.__contador == 14:
            var = "sim"
        return var

    def imprimir_bombas(self):
        arquivo = open('save/bombas.save', 'w+')
        texto = str(self.__bombas)
        arquivo.writelines(texto)
        arquivo.close()
    
    @staticmethod
    def save_existe():
        var = False
        if os.path.isfile('save/bombas.save'):
            var = True
        return var

if __name__ == "__main__":
    server = CampoMinadoNegocio()
    server.server()
    
