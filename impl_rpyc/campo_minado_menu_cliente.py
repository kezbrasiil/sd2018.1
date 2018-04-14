from tkinter import *
from campo_minado_cliente import *
from campo_minado_servidor import *

class CampoMinadoMenuCliente:

    master = None

    ENCODE = "UTF-8"
    MAX_BYTES = 65535
    PORT = 5000
    HOST = "127.0.0.1"

    def __init__(self, master):
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.dest = (self.HOST, self.PORT)

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
        self.sock.sendto(dados, self.dest)
        dados, endereco = self.sock.recvfrom(self.MAX_BYTES)
        return dados.decode(self.ENCODE)
    
    def __fechar_conexao(self):
        self.sock.close()

    def __novo_jogo_click(self):
        texto = "CRIAR NOVO JOGO"
        self.__requisicao(texto)
        self.__criar_jogo(False, None)
    
    def __continuar_jogo_click(self):
        texto = "CARREGAR JOGO SALVO"
        jogadas = self.__requisicao(texto)
        self.__criar_jogo(True, jogadas)
    
    def __criar_jogo(self, flag, jogadas):
        self.__fechar_conexao()
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