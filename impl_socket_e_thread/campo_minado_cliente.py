from tkinter import *
from tkinter import messagebox
from socket import socket, AF_INET, SOCK_DGRAM

class CampoMinadoCliente:

    master = None

    __x0 = 3
    __x1 = 47
    __x2 = 91
    __x3 = 135
    __x4 = 179
    __x5 = 223
    __x6 = 267
    __x7 = 311
    __x8 = 355

    __y0 = 40
    __y1 = 80
    __y2 = 120
    __y3 = 160
    __y4 = 200
    __y5 = 240

    ENCODE = "UTF-8"
    MAX_BYTES = 65535
    PORT = 5000
    HOST = "127.0.0.1"

    def __init__(self, master, flag, jogadas):

        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.dest = (self.HOST, self.PORT)

        # contabiliza a quantidade de jogadas
        # total de 40 jogadas para ganhar
        self.__contador = StringVar()
        
        # iniciar o contador na tela
        self.__incrementar_jogada()

        self.__label_00 = StringVar()
        self.__label_01 = StringVar()
        self.__label_02 = StringVar()
        self.__label_03 = StringVar()
        self.__label_04 = StringVar()
        self.__label_05 = StringVar()
        self.__label_06 = StringVar()
        self.__label_07 = StringVar()
        self.__label_08 = StringVar()
        self.__label_10 = StringVar()
        self.__label_11 = StringVar()
        self.__label_12 = StringVar()
        self.__label_13 = StringVar()
        self.__label_14 = StringVar()
        self.__label_15 = StringVar()
        self.__label_16 = StringVar()
        self.__label_17 = StringVar()
        self.__label_18 = StringVar()
        self.__label_20 = StringVar()
        self.__label_21 = StringVar()
        self.__label_22 = StringVar()
        self.__label_23 = StringVar()
        self.__label_24 = StringVar()
        self.__label_25 = StringVar()
        self.__label_26 = StringVar()
        self.__label_27 = StringVar()
        self.__label_28 = StringVar()
        self.__label_30 = StringVar()
        self.__label_31 = StringVar()
        self.__label_32 = StringVar()
        self.__label_33 = StringVar()
        self.__label_34 = StringVar()
        self.__label_35 = StringVar()
        self.__label_36 = StringVar()
        self.__label_37 = StringVar()
        self.__label_38 = StringVar()
        self.__label_40 = StringVar()
        self.__label_41 = StringVar()
        self.__label_42 = StringVar()
        self.__label_43 = StringVar()
        self.__label_44 = StringVar()
        self.__label_45 = StringVar()
        self.__label_46 = StringVar()
        self.__label_47 = StringVar()
        self.__label_48 = StringVar()
        self.__label_50 = StringVar()
        self.__label_51 = StringVar()
        self.__label_52 = StringVar()
        self.__label_53 = StringVar()
        self.__label_54 = StringVar()
        self.__label_55 = StringVar()
        self.__label_56 = StringVar()
        self.__label_57 = StringVar()
        self.__label_58 = StringVar()       

        self.master = master
        self.master.title("Campo Minado")
        self.master.geometry("401x290+500+350")
        self.master.maxsize(401,290)
        self.master.minsize(401,290)
        self.master["background"] = "#343434"

        self.label_contador = Label(master, width=5, textvariable=self.__contador, background="#EFEFEF")
        self.label_contador.place(x=179,y=5)

        self.button_00 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_00, command=self.button00_click)
        self.button_00.place(x=self.__x0, y=self.__y0)
        self.button_01 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_01, command=self.button01_click)
        self.button_01.place(x=self.__x1, y=self.__y0)
        self.button_02 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_02, command=self.button02_click)
        self.button_02.place(x=self.__x2, y=self.__y0)
        self.button_03 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_03, command=self.button03_click)
        self.button_03.place(x=self.__x3, y=self.__y0)
        self.button_04 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_04, command=self.button04_click)
        self.button_04.place(x=self.__x4, y=self.__y0)
        self.button_05 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_05, command=self.button05_click)
        self.button_05.place(x=self.__x5, y=self.__y0)
        self.button_06 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_06, command=self.button06_click)
        self.button_06.place(x=self.__x6, y=self.__y0)
        self.button_07 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_07, command=self.button07_click)
        self.button_07.place(x=self.__x7, y=self.__y0)
        self.button_08 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_08, command=self.button08_click)
        self.button_08.place(x=self.__x8, y=self.__y0)

        self.button_10 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_10, command=self.button10_click)
        self.button_10.place(x=self.__x0, y=self.__y1)
        self.button_11 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_11, command=self.button11_click)
        self.button_11.place(x=self.__x1, y=self.__y1)
        self.button_12 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_12, command=self.button12_click)
        self.button_12.place(x=self.__x2, y=self.__y1)
        self.button_13 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_13, command=self.button13_click)
        self.button_13.place(x=self.__x3, y=self.__y1)
        self.button_14 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_14, command=self.button14_click)
        self.button_14.place(x=self.__x4, y=self.__y1)
        self.button_15 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_15, command=self.button15_click)
        self.button_15.place(x=self.__x5, y=self.__y1)
        self.button_16 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_16, command=self.button16_click)
        self.button_16.place(x=self.__x6, y=self.__y1)
        self.button_17 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_17, command=self.button17_click)
        self.button_17.place(x=self.__x7, y=self.__y1)
        self.button_18 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_18, command=self.button18_click)
        self.button_18.place(x=self.__x8, y=self.__y1)

        self.button_20 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_20, command=self.button20_click)
        self.button_20.place(x=self.__x0, y=self.__y2)
        self.button_21 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_21, command=self.button21_click)
        self.button_21.place(x=self.__x1, y=self.__y2)
        self.button_22 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_22, command=self.button22_click)
        self.button_22.place(x=self.__x2, y=self.__y2)
        self.button_23 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_23, command=self.button23_click)
        self.button_23.place(x=self.__x3, y=self.__y2)
        self.button_24 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_24, command=self.button24_click)
        self.button_24.place(x=self.__x4, y=self.__y2)
        self.button_25 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_25, command=self.button25_click)
        self.button_25.place(x=self.__x5, y=self.__y2)
        self.button_26 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_26, command=self.button26_click)
        self.button_26.place(x=self.__x6, y=self.__y2)
        self.button_27 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_27, command=self.button27_click)
        self.button_27.place(x=self.__x7, y=self.__y2)
        self.button_28 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_28, command=self.button28_click)
        self.button_28.place(x=self.__x8, y=self.__y2)

        self.button_30 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_30, command=self.button30_click)
        self.button_30.place(x=self.__x0, y=self.__y3)
        self.button_31 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_31, command=self.button31_click)
        self.button_31.place(x=self.__x1, y=self.__y3)
        self.button_32 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_32, command=self.button32_click)
        self.button_32.place(x=self.__x2, y=self.__y3)
        self.button_33 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_33, command=self.button33_click)
        self.button_33.place(x=self.__x3, y=self.__y3)
        self.button_34 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_34, command=self.button34_click)
        self.button_34.place(x=self.__x4, y=self.__y3)
        self.button_35 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_35, command=self.button35_click)
        self.button_35.place(x=self.__x5, y=self.__y3)
        self.button_36 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_36, command=self.button36_click)
        self.button_36.place(x=self.__x6, y=self.__y3)
        self.button_37 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_37, command=self.button37_click)
        self.button_37.place(x=self.__x7, y=self.__y3)
        self.button_38 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_38, command=self.button38_click)
        self.button_38.place(x=self.__x8, y=self.__y3)

        self.button_40 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_40, command=self.button40_click)
        self.button_40.place(x=self.__x0, y=self.__y4)
        self.button_41 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_41, command=self.button41_click)
        self.button_41.place(x=self.__x1, y=self.__y4)
        self.button_42 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_42, command=self.button42_click)
        self.button_42.place(x=self.__x2, y=self.__y4)
        self.button_43 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_43, command=self.button43_click)
        self.button_43.place(x=self.__x3, y=self.__y4)
        self.button_44 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_44, command=self.button44_click)
        self.button_44.place(x=self.__x4, y=self.__y4)
        self.button_45 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_45, command=self.button45_click)
        self.button_45.place(x=self.__x5, y=self.__y4)
        self.button_46 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_46, command=self.button46_click)
        self.button_46.place(x=self.__x6, y=self.__y4)
        self.button_47 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_47, command=self.button47_click)
        self.button_47.place(x=self.__x7, y=self.__y4)
        self.button_48 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_48, command=self.button48_click)
        self.button_48.place(x=self.__x8, y=self.__y4)

        self.button_50 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_50, command=self.button50_click)
        self.button_50.place(x=self.__x0, y=self.__y5)
        self.button_51 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_51, command=self.button51_click)
        self.button_51.place(x=self.__x1, y=self.__y5)
        self.button_52 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_52, command=self.button52_click)
        self.button_52.place(x=self.__x2, y=self.__y5)
        self.button_53 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_53, command=self.button53_click)
        self.button_53.place(x=self.__x3, y=self.__y5)
        self.button_54 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_54, command=self.button54_click)
        self.button_54.place(x=self.__x4, y=self.__y5)
        self.button_55 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_55, command=self.button55_click)
        self.button_55.place(x=self.__x5, y=self.__y5)
        self.button_56 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_56, command=self.button56_click)
        self.button_56.place(x=self.__x6, y=self.__y5)
        self.button_57 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_57, command=self.button57_click)
        self.button_57.place(x=self.__x7, y=self.__y5)
        self.button_58 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=0.5, textvariable=self.__label_58, command=self.button58_click)
        self.button_58.place(x=self.__x8, y=self.__y5)

        self.__continuar_jogo(flag, jogadas)
        
    def button00_click(self):
        self.button_clicked(self.button_00)
        self.__label_00.set(self.__tem_bomba((0,0)))
        
    def button01_click(self):
        self.button_clicked(self.button_01)
        self.__label_01.set(self.__tem_bomba((0,1)))
    
    def button02_click(self):
        self.button_clicked(self.button_02)
        self.__label_02.set(self.__tem_bomba((0,2)))
    
    def button03_click(self):
        self.button_clicked(self.button_03)
        self.__label_03.set(self.__tem_bomba((0,3)))
    
    def button04_click(self):
        self.button_clicked(self.button_04)
        self.__label_04.set(self.__tem_bomba((0,4)))
    
    def button05_click(self):
        self.button_clicked(self.button_05)
        self.__label_05.set(self.__tem_bomba((0,5)))
    
    def button06_click(self):
        self.button_clicked(self.button_06)
        self.__label_06.set(self.__tem_bomba((0,6)))
    
    def button07_click(self):
        self.button_clicked(self.button_07)
        self.__label_07.set(self.__tem_bomba((0,7)))
    
    def button08_click(self):
        self.button_clicked(self.button_08)
        self.__label_08.set(self.__tem_bomba((0,8)))
    
    def button10_click(self):
        self.button_clicked(self.button_10)
        self.__label_10.set(self.__tem_bomba((1,0)))
    
    def button11_click(self):
        self.button_clicked(self.button_11)
        self.__label_11.set(self.__tem_bomba((1,1)))
    
    def button12_click(self):
        self.button_clicked(self.button_12)    
        self.__label_12.set(self.__tem_bomba((1,2)))
    
    def button13_click(self):
        self.button_clicked(self.button_13)
        self.__label_13.set(self.__tem_bomba((1,3)))
    
    def button14_click(self):
        self.button_clicked(self.button_14)
        self.__label_14.set(self.__tem_bomba((1,4)))
    
    def button15_click(self):
        self.button_clicked(self.button_15)
        self.__label_15.set(self.__tem_bomba((1,5)))
    
    def button16_click(self):
        self.button_clicked(self.button_16)
        self.__label_16.set(self.__tem_bomba((1,6)))
    
    def button17_click(self):
        self.button_clicked(self.button_17)
        self.__label_17.set(self.__tem_bomba((1,7)))
    
    def button18_click(self):
        self.button_clicked(self.button_18)
        self.__label_18.set(self.__tem_bomba((1,8)))
    
    def button20_click(self):
        self.button_clicked(self.button_20)
        self.__label_20.set(self.__tem_bomba((2,0)))
    
    def button21_click(self):
        self.button_clicked(self.button_21)
        self.__label_21.set(self.__tem_bomba((2,1)))
    
    def button22_click(self):
        self.button_clicked(self.button_22)
        self.__label_22.set(self.__tem_bomba((2,2)))
    
    def button23_click(self):
        self.button_clicked(self.button_23)
        self.__label_23.set(self.__tem_bomba((2,3)))
    
    def button24_click(self):
        self.button_clicked(self.button_24)
        self.__label_24.set(self.__tem_bomba((2,4)))
    
    def button25_click(self):
        self.button_clicked(self.button_25)
        self.__label_25.set(self.__tem_bomba((2,5)))
    
    def button26_click(self):
        self.button_clicked(self.button_26)
        self.__label_26.set(self.__tem_bomba((2,6)))
    
    def button27_click(self):
        self.button_clicked(self.button_27)
        self.__label_27.set(self.__tem_bomba((2,7)))
    
    def button28_click(self):
        self.button_clicked(self.button_28)
        self.__label_28.set(self.__tem_bomba((2,8)))
    
    def button30_click(self):
        self.button_clicked(self.button_30)
        self.__label_30.set(self.__tem_bomba((3,0)))
    
    def button31_click(self):
        self.button_clicked(self.button_31)
        self.__label_31.set(self.__tem_bomba((3,1)))
    
    def button32_click(self):
        self.button_clicked(self.button_32)
        self.__label_32.set(self.__tem_bomba((3,2)))
    
    def button33_click(self):
        self.button_clicked(self.button_33)
        self.__label_33.set(self.__tem_bomba((3,3)))
    
    def button34_click(self):
        self.button_clicked(self.button_34)
        self.__label_34.set(self.__tem_bomba((3,4)))
    
    def button35_click(self):
        self.button_clicked(self.button_35)
        self.__label_35.set(self.__tem_bomba((3,5)))
    
    def button36_click(self):
        self.button_clicked(self.button_36)
        self.__label_36.set(self.__tem_bomba((3,6)))
    
    def button37_click(self):
        self.button_clicked(self.button_37)
        self.__label_37.set(self.__tem_bomba((3,7)))
    
    def button38_click(self):
        self.button_clicked(self.button_38)
        self.__label_38.set(self.__tem_bomba((3,8)))
    
    def button40_click(self):
        self.button_clicked(self.button_40)
        self.__label_40.set(self.__tem_bomba((4,0)))
    
    def button41_click(self):
        self.button_clicked(self.button_41)
        self.__label_41.set(self.__tem_bomba((4,1)))
    
    def button42_click(self):
        self.button_clicked(self.button_42)
        self.__label_42.set(self.__tem_bomba((4,2)))
    
    def button43_click(self):
        self.button_clicked(self.button_43)
        self.__label_43.set(self.__tem_bomba((4,3)))
    
    def button44_click(self):
        self.button_clicked(self.button_44)
        self.__label_44.set(self.__tem_bomba((4,4)))
        
    def button45_click(self):
        self.button_clicked(self.button_45)
        self.__label_45.set(self.__tem_bomba((4,5)))
    
    def button46_click(self):
        self.button_clicked(self.button_46)
        self.__label_46.set(self.__tem_bomba((4,6)))
    
    def button47_click(self):
        self.button_clicked(self.button_47)
        self.__label_47.set(self.__tem_bomba((4,7)))
    
    def button48_click(self):
        self.button_clicked(self.button_48)
        self.__label_48.set(self.__tem_bomba((4,8)))
    
    def button50_click(self):
        self.button_clicked(self.button_50)
        self.__label_50.set(self.__tem_bomba((5,0)))
    
    def button51_click(self):
        self.button_clicked(self.button_51)
        self.__label_51.set(self.__tem_bomba((5,1)))
    
    def button52_click(self):
        self.button_clicked(self.button_52)
        self.__label_52.set(self.__tem_bomba((5,2)))
    
    def button53_click(self):
        self.button_clicked(self.button_53)
        self.__label_53.set(self.__tem_bomba((5,3)))
        
    def button54_click(self):
        self.button_clicked(self.button_54)
        self.__label_54.set(self.__tem_bomba((5,4)))
        
    def button55_click(self):
        self.button_clicked(self.button_55)
        self.__label_55.set(self.__tem_bomba((5,5)))
    
    def button56_click(self):
        self.button_clicked(self.button_56)
        self.__label_56.set(self.__tem_bomba((5,6)))
    
    def button57_click(self):
        self.button_clicked(self.button_57)
        self.__label_57.set(self.__tem_bomba((5,7)))

    def button58_click(self):
        self.button_clicked(self.button_58)
        self.__label_58.set(self.__tem_bomba((5,8)))
    
    def button_clicked(self, button):
        button["state"] = DISABLED
        button["background"] = "#999999"
        button["borderwidth"] = 2
        button["relief"] = FLAT
        self.__incrementar_jogada()
            
    def __continuar_jogo(self, flag, jogadas):
        # utilizando reflexao para executar os botoes 
        if flag:
           actions = jogadas.split(",")
           for action in actions:
                if hasattr(self,action):
                   getattr(self,action)()
                else:
                    print('Metodo inexistente')

    def __requisicao(self, texto):
        dados = texto.encode(self.ENCODE)
        self.sock.sendto(dados, self.dest)
        dados, endereco = self.sock.recvfrom(self.MAX_BYTES)
        return dados.decode(self.ENCODE)
    
    def __fechar_conexao(self):
        self.sock.close()
            
    def __tem_bomba(self, tupla):
        texto = str(tupla)
        resposta = self.__requisicao(texto)

        if resposta == "sim":
            self.__derrota()
        else:
            self.__vitoria()
            return resposta # retorna a quantidade de bombas ao redor

    def __vitoria(self):
        texto = "JOGADOR VENCEU?"
        resposta = self.__requisicao(texto)

        if resposta == "sim":
            retorno = messagebox.askyesno("Vitória!", "Parabéns! Você venceu.\nDeseja iniciar uma nova partida?", icon=messagebox.INFO)
            if retorno:
                texto = "CRIAR NOVO JOGO"
                self.__requisicao(texto)
                self.__fechar_conexao()
                self.master.destroy()
                CampoMinadoCliente.criar_partida()
            else:
                self.__fechar_conexao()
                self.master.destroy()
    
    def __derrota(self):
        resposta = messagebox.askyesno("Derrota!", "Você acertou uma Bomba!\nDeseja iniciar uma nova partida?", icon=messagebox.WARNING)
        if resposta:
            texto = "CRIAR NOVO JOGO"
            self.__requisicao(texto)
            self.__fechar_conexao()
            self.master.destroy()
            CampoMinadoCliente.criar_partida()
        else:
            self.__fechar_conexao()
            self.master.destroy()

    def __incrementar_jogada(self):
        texto = "NUMERO DE JOGADAS?"
        self.__contador.set(self.__requisicao(texto))
    
    @staticmethod
    def criar_partida():
        janela = Tk()
        jogo = CampoMinadoCliente(janela, False, None)
        janela.mainloop()

if __name__ == "__main__":
    CampoMinadoCliente.criar_partida()