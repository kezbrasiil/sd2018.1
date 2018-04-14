from random import randint
from ast import literal_eval
import os.path
from socket import socket, AF_INET, SOCK_DGRAM
import threading

class CampoMinadoServidor(object):

    PATH = '../save/bombas.save'
    ENCODE = "UTF-8"
    MAX_BYTES = 65535
    PORT = 5000
    HOST = ''
    __contador = None
    __bombas = None
    __arquivo = None
    
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.origem = (self.HOST, self.PORT)
        self.sock.bind(self.origem)

    def server(self):
        print("[Servidor Ativo]\n")
        while True:
            dados, endereco = self.sock.recvfrom(self.MAX_BYTES)
            t = threading.Thread(target=self.tratar_conexao, args=(self.sock, dados, endereco))
            t.start()

    def tratar_conexao(self, sock, dados, endereco):
        texto = dados.decode(self.ENCODE)

        print("[Mensagem Recebida] " + texto)

        if '(' in texto:
            tupla = literal_eval(texto)
            self.__salvar_jogada(tupla)
            retorno = self.__tem_bomba(tupla)
            if retorno:
                texto = "sim"
                self.__contador = 0
            else:
                texto = self.__bombas_vizinhas(tupla)
        elif texto == "JOGADOR VENCEU?":
            texto = self.__vitoria()
        elif texto == "NUMERO DE JOGADAS?":
            texto = str(self.__contador)
            self.__incrementar_jogada()
        elif texto == "EXISTE ARQUIVO DE SAVE?":
            texto = self.__save_existe()
        elif texto == "CRIAR NOVO JOGO":
            self.__bombas = []
            self.__gerar_bombas()
            self.__criar_save()
            self.__contador = 0
            texto = "ok"
        elif texto == "CARREGAR JOGO SALVO":
            texto = self.__carregar_partida()
            self.__contador = 0
            self.__criar_save()

        print("[Enviando Resposta] " + texto)

        dados = texto.encode(self.ENCODE)
        self.sock.sendto(dados, endereco)

        print("[Fim da Requisição]\n")
    
    def __carregar_partida(self):
        arq = open(self.PATH, 'r')
        linha = arq.readline() # primeira linha recupera as bombas
        self.__bombas = literal_eval(linha)
        return arq.readline() # segunda linha recupera os botoes clicados

    def __gerar_bombas(self):
        while(len(self.__bombas) < 14):
            linha = randint(0,5)
            coluna = randint(0,8)
            tupla = (linha,coluna)
            if tupla not in self.__bombas:
                self.__bombas.append(tupla)
    
    def __tem_bomba(self, tupla):
        var = False
        if tupla in self.__bombas:
            var = True
            self.__deletar_arquivo()
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
    
    def __incrementar_jogada(self):
        self.__contador = self.__contador + 1
        return self.__contador

    def __vitoria(self):
        var = "nao"
        if self.__contador == 40:
            var = "sim"
            self.__contador = 0
            self.__deletar_arquivo()
        return var
    
    def __deletar_arquivo(self):
        self.__arquivo.close()
        os.remove(self.PATH)

    def __criar_save(self):
        self.__arquivo = open(self.PATH, 'w+')
        texto = str(self.__bombas)
        self.__arquivo.writelines(texto+"\n")
        self.__arquivo.close()
    
    def __salvar_jogada(self, tupla):
        self.__arquivo = open(self.PATH, 'a')
        texto = "button"+str(tupla[0])+str(tupla[1])+"_click,"
        self.__arquivo.writelines(texto)
        self.__arquivo.close()
    
    def __save_existe(self):
        var = "nao"
        if os.path.isfile(self.PATH):
            var = "sim"
        return var

if __name__ == "__main__":
    server = CampoMinadoServidor()
    server.server()
    
