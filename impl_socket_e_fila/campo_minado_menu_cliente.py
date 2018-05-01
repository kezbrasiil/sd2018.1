from tkinter import *
from campo_minado_cliente import *
from campo_minado_servidor import *

class CampoMinadoMenuCliente:

    master = None

    ENCODE = "UTF-8"
    PORT = "5559"

    def __init__(self, master):
        self.contexto = zmq.Context()
        self.socket = self.contexto.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:%s" % self.PORT)

        self.master = master
        self.master.title("Menu")
        self.master.geometry("250x250")
        self.master.maxsize(250,250)
        self.master.minsize(250,250)
        self.master["background"] = "#343434"

        self.__novo_jogo = Button(master, width=20, height=2, text="Novo Jogo", background="#EFEFEF", borderwidth=1, command=self.__novo_jogo_click)
        self.__novo_jogo.place(x=50, y=30)

        self.__continuar = Button(master, width=20, height=2, text="Continuar", background="#EFEFEF", borderwidth=1, command=self.__continuar_jogo_click)
        self.__continuar.place(x=50, y=100)

        self.__save_existe()

    def __requisicao(self, texto):
        dados = texto.encode(self.ENCODE)
        self.socket.send(dados)
        dados = self.socket.recv()
        return dados.decode(self.ENCODE)
    
    def __novo_jogo_click(self):
        texto = "CRIAR NOVO JOGO"
        self.__requisicao(texto)
        self.__criar_jogo(False, None)
    
    def __continuar_jogo_click(self):
        texto = "CARREGAR JOGO SALVO"
        jogadas = self.__requisicao(texto)
        self.__criar_jogo(True, jogadas)
    
    def __criar_jogo(self, flag, jogadas):
        self.master.destroy()
        janela = Tk()
        jogo = CampoMinadoCliente(janela, flag, jogadas)
        janela.mainloop()

    def __save_existe(self):
        texto = "EXISTE ARQUIVO DE SAVE?"
        resposta = self.__requisicao(texto)
        if resposta == "nao":
            self.__continuar["state"] = DISABLED
    
if __name__ == "__main__":
    janela = Tk()
    jogo = CampoMinadoMenuCliente(janela)
    janela.mainloop()