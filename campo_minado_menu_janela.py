from tkinter import *
from campo_minado_jogo_janela import *

class CampoMinadoMenuJanela:

    master = None

    def __init__(self, master):
        self.master = master
        self.master.title("Campo Minado")
        self.master.geometry("250x250")
        self.master.maxsize(250,250)
        self.master.minsize(250,250)
        self.master["background"] = "#343434"

        self.__novo_jogo = Button(master, width=20, height=2, text="Novo Jogo", background="#EFEFEF", borderwidth=1, command=self.__novo_jogo_click)
        self.__novo_jogo.place(x=50, y=30)

        self.__continuar = Button(master, width=20, height=2, text="Continuar", background="#EFEFEF", borderwidth=1, command=self.__continuar_click)
        self.__continuar.place(x=50, y=100)

    def __novo_jogo_click(self):
        self.master.destroy()
        janela = Tk()
        jogo = CampoMinadoJogoJanela(janela)
        janela.mainloop()
        jogo.negocio.imprimir_bombas()
        
    def __continuar_click(self, arquivo):
        pass

if __name__ == "__main__":
    janela = Tk()
    jogo = CampoMinadoMenuJanela(janela)
    janela.mainloop()