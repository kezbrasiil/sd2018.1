from tkinter import *
from campo_minado_cliente import *
from campo_minado_servidor import *
import rpyc
import sys

class CampoMinadoMenuCliente:

    master = None

    def __init__(self, master):
        self.config = {'allow_public_attrs': True}
        self.proxy = rpyc.connect('localhost', 18861, config=self.config)
        self.conn = self.proxy.root.CampoMinadoServidorImpl()

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
   
    def __novo_jogo_click(self):
        self.conn.criar_novo_jogo()
        self.__criar_jogo(False, None, self.conn)
    
    def __continuar_jogo_click(self):
        jogadas = self.conn.carregar_partida()
        self.__criar_jogo(True, jogadas, self.conn)
    
    def __criar_jogo(self, flag, jogadas, conn):
        self.master.destroy()
        janela = Tk()
        jogo = CampoMinadoCliente(janela, flag, jogadas, conn)
        janela.mainloop()

    def __save_existe(self):
        resposta = self.conn.save_existe()
        if not resposta:
            self.__continuar["state"] = DISABLED
        
if __name__ == "__main__":
    try:
        janela = Tk()
        jogo = CampoMinadoMenuCliente(janela)
        janela.mainloop()
    except:
        for val in sys.exc_info():
            print(val)