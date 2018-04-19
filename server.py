# -*- coding: iso-8859-1 -*-
u"""Este módulo possui a implementação de UDP Server"""
from socket import socket, AF_INET, SOCK_DGRAM
from random import randint
import re
import threading
from datetime import datetime

class Server:
    ENCODE = "UTF-8"
    MAX_BYTES = 65535
    PORT = 5000
    HOST = ''
    
    qtdLinhas = 0
    mapaQuantidades = []
    mapaMinas = []
    maximoJogadas = 0
    
    JOGADA_REALIZADA = "JR"
    JOGADA_IRREGULAR = "JI"
    ACERTOU_MINA = "AM"
    JOGO_CRIADO = "JC"
    JOGO_RECUPERADO = "RE"

    def server_thread_procedural(self):
        #Abrindo uma porta UDP
        origem = (self.HOST,self.PORT)
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.bind(origem)
        
        while True:
            #recebi dados
            data, address = sock.recvfrom(self.MAX_BYTES)
            # Criação de thread procedural
            t = threading.Thread(target=self.server, args=(sock, data, address))
            t.start()

    # def tratar_conexao(self, sock, data, address):
    #     text = data.decode(self.ENCODE)
    #     print(text)
    #     #Envia resposta
    #     text = "Quantidade de bytes enviados: " + str(len(data))
    #     data = text.encode(ENCODE)
    #     sock.sendto(data, address)
    
    def criarJogo(self):
        self.mapaMinas = self.colocaMinas(self.qtdLinhas)
        self.mapaQuantidades = []
        self.maximoJogadas = self.qtdLinhas*self.qtdLinhas-len(self.mapaMinas)
        print('Jogo criado',self.qtdLinhas,self.mapaMinas,self.maximoJogadas)
        
    def continuarJogo(self):
        arquivo = open('jogada.txt', 'r')
        self.qtdLinhas = int(arquivo.readline())
        self.mapaQuantidades  = eval(arquivo.readline())
        self.mapaMinas = eval(arquivo.readline())
        self.maximoJogadas = int(arquivo.readline())
        arquivo.close()
        
    def colocaMinas(self,qtdLinhas):
        minas = []
        qtdMinas = randint(int((qtdLinhas*qtdLinhas)/5),int((qtdLinhas*qtdLinhas)/3))
        for i in range(qtdMinas):
            linha = randint(0,qtdLinhas-1)
            coluna = randint(0,qtdLinhas-1)
            if ([linha,coluna] in minas):
                qtdMinas += 1
            else:
                minas.append([linha,coluna])
        return minas
    
    def isJogadaValida(self,tupla):
        if (tupla[0] < 0 or tupla[1] < 0) or (tupla[0] > self.qtdLinhas or tupla[1] > self.qtdLinhas):
            print("Jogada inválida",tupla[0],tupla[1],self.qtdLinhas)
            return False, "Jogada inválida"
        for qtd in self.mapaQuantidades:
            if tupla == qtd[0]:
                print("Jogada repetida.")
                return False,"Jogada repetida."
        return True, "ok"
    
    def jogar(self,tupla):
        print(tupla)
        print(self.mapaMinas)
        if tupla in self.mapaMinas:
            print('FIM DE JOGO! Você acertou uma mina!')
            return(self.ACERTOU_MINA)
        qtdMinas = 0
        for y in [-1,0,1]:
            for x in [-1,0,1]:
                if self.verificaBomba([tupla[0]+y,tupla[1]+x], self.mapaMinas):
                    qtdMinas += 1
        self.mapaQuantidades.append([[tupla[0],tupla[1]],qtdMinas])
        self.maximoJogadas -= 1
        return(self.JOGADA_REALIZADA)
        
    def verificaBomba(self,posicao,minas):
        if (posicao[0]>=0 and posicao[1]>=0) and (posicao[0]<self.qtdLinhas and posicao[1]<self.qtdLinhas):
            if (posicao in minas):
                return True
            else:
                return False
    
    def salvarJogo(self):
        arq = open("jogada.txt",'w')
        arq.write(str(self.qtdLinhas)+"\n")
        arq.write(str(self.mapaQuantidades)+"\n")
        arq.write(str(self.mapaMinas)+"\n")
        arq.write(str(self.maximoJogadas))
        arq.close()
    
    def server(self, sock, data, address):
        print("Aguardando início do jogo")
        text = data.decode(self.ENCODE)
        
        if (text == '1'):
            self.criarJogo()
            print("Jogo criado")
            retorno = self.JOGO_CRIADO + "$" + str(self.qtdLinhas) + "$" + str(self.mapaQuantidades) + "$" + str(self.maximoJogadas)
            data = retorno.encode(self.ENCODE)
            sock.sendto(data,address)
            return ;
        elif (text == '2'):
            self.continuarJogo()
            print("Jogo recuperado")
            retorno = self.JOGO_RECUPERADO + "$" + str(self.qtdLinhas) + "$" + str(self.mapaQuantidades) + "$" + str(self.maximoJogadas)
            data = retorno.encode(self.ENCODE)
            sock.sendto(data,address)
            return ;
                    
        padrao = re.match("[0-9],[0-9]",text)
            
        if (padrao == None):
            if (text == "q"):
                print('Jogo encerrado pelo usuário')
                retorno = ""
                data = text.encode(self.ENCODE)
                sock.sendto(data,address)
                return ;
            if (text == "qs"):
                print('Salvando jogo')
                self.salvarJogo()
                print('Jogo encerrado pelo usuário')
                retorno = ""
                data = text.encode(self.ENCODE)
                sock.sendto(data,address)
            print('Comando inválido')
            return ;
        
        tupla = text.split(",")
        tupla[0] = int(tupla[0])
        tupla[1] = int(tupla[1])
        isValida, msg = self.isJogadaValida(tupla)
        
        if (isValida):
            print('tupla valida',tupla)
            jogo = self.jogar(tupla)
            retorno = jogo + "$" + str(self.qtdLinhas) + "$" + str(self.mapaQuantidades) + "$" + str(self.maximoJogadas)
            data = retorno.encode(self.ENCODE)
            sock.sendto(data,address)
            return ;
        else:
            print('tupla invalida')
            retorno = self.JOGADA_IRREGULAR + "$" + str(self.qtdLinhas) + "$" + str(self.mapaQuantidades) + "$" + str(self.maximoJogadas)
            data = retorno.encode(self.ENCODE)
            sock.sendto(data,address)
            return ;
    
    def __init__(self, linhas):
        self.qtdLinhas = linhas
        self.server_thread_procedural()    
            
        
if __name__ == "__main__":
    Server(5)