from functools import partial
from tkinter import *
from tkinter import messagebox
from ast import literal_eval
from campo_minado_negocio import *

class CampoMinadoJogoJanela:

    __x0 = 25
    __x1 = 69
    __x2 = 113
    __x3 = 157
    __x4 = 201
    __x5 = 245
    __x6 = 289
    __x7 = 333

    __y0 = 25
    __y1 = 65
    __y2 = 105
    __y3 = 145
    __y4 = 185
    __y5 = 225 

    def __init__(self, master):
        self.negocio = CampoMinadoNegocio()

        self.__label_00 = StringVar()
        self.__label_01 = StringVar()
        self.__label_02 = StringVar()
        self.__label_03 = StringVar()
        self.__label_04 = StringVar()
        self.__label_05 = StringVar()
        self.__label_06 = StringVar()
        self.__label_07 = StringVar()
        self.__label_10 = StringVar()
        self.__label_11 = StringVar()
        self.__label_12 = StringVar()
        self.__label_13 = StringVar()
        self.__label_14 = StringVar()
        self.__label_15 = StringVar()
        self.__label_16 = StringVar()
        self.__label_17 = StringVar()
        self.__label_20 = StringVar()
        self.__label_21 = StringVar()
        self.__label_22 = StringVar()
        self.__label_23 = StringVar()
        self.__label_24 = StringVar()
        self.__label_25 = StringVar()
        self.__label_26 = StringVar()
        self.__label_27 = StringVar()
        self.__label_30 = StringVar()
        self.__label_31 = StringVar()
        self.__label_32 = StringVar()
        self.__label_33 = StringVar()
        self.__label_34 = StringVar()
        self.__label_35 = StringVar()
        self.__label_36 = StringVar()
        self.__label_37 = StringVar()
        self.__label_40 = StringVar()
        self.__label_41 = StringVar()
        self.__label_42 = StringVar()
        self.__label_43 = StringVar()
        self.__label_44 = StringVar()
        self.__label_45 = StringVar()
        self.__label_46 = StringVar()
        self.__label_47 = StringVar()
        self.__label_50 = StringVar()
        self.__label_51 = StringVar()
        self.__label_52 = StringVar()
        self.__label_53 = StringVar()
        self.__label_54 = StringVar()
        self.__label_55 = StringVar()
        self.__label_56 = StringVar()
        self.__label_57 = StringVar()

        master.title("Campo Minado")
        master.geometry("400x290+500+350")
        master["background"] = "#343434"

        self.__button_00 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_00, command=self.__button00_click)
        self.__button_00.place(x=self.__x0, y=self.__y0)
        self.__button_01 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_01, command=self.__button01_click)
        self.__button_01.place(x=self.__x1, y=self.__y0)
        self.__button_02 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_02, command=self.__button02_click)
        self.__button_02.place(x=self.__x2, y=self.__y0)
        self.__button_03 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_03, command=self.__button03_click)
        self.__button_03.place(x=self.__x3, y=self.__y0)
        self.__button_04 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_04, command=self.__button04_click)
        self.__button_04.place(x=self.__x4, y=self.__y0)
        self.__button_05 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_05, command=self.__button05_click)
        self.__button_05.place(x=self.__x5, y=self.__y0)
        self.__button_06 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_06, command=self.__button06_click)
        self.__button_06.place(x=self.__x6, y=self.__y0)
        self.__button_07 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_07, command=self.__button07_click)
        self.__button_07.place(x=self.__x7, y=self.__y0)

        self.__button_10 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_10, command=self.__button10_click)
        self.__button_10.place(x=self.__x0, y=self.__y1)
        self.__button_11 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_11, command=self.__button11_click)
        self.__button_11.place(x=self.__x1, y=self.__y1)
        self.__button_12 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_12, command=self.__button12_click)
        self.__button_12.place(x=self.__x2, y=self.__y1)
        self.__button_13 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_13, command=self.__button13_click)
        self.__button_13.place(x=self.__x3, y=self.__y1)
        self.__button_14 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_14, command=self.__button14_click)
        self.__button_14.place(x=self.__x4, y=self.__y1)
        self.__button_15 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_15, command=self.__button15_click)
        self.__button_15.place(x=self.__x5, y=self.__y1)
        self.__button_16 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_16, command=self.__button16_click)
        self.__button_16.place(x=self.__x6, y=self.__y1)
        self.__button_17 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_17, command=self.__button17_click)
        self.__button_17.place(x=self.__x7, y=self.__y1)

        self.__button_20 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_20, command=self.__button20_click)
        self.__button_20.place(x=self.__x0, y=self.__y2)
        self.__button_21 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_21, command=self.__button21_click)
        self.__button_21.place(x=self.__x1, y=self.__y2)
        self.__button_22 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_22, command=self.__button22_click)
        self.__button_22.place(x=self.__x2, y=self.__y2)
        self.__button_23 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_23, command=self.__button23_click)
        self.__button_23.place(x=self.__x3, y=self.__y2)
        self.__button_24 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_24, command=self.__button24_click)
        self.__button_24.place(x=self.__x4, y=self.__y2)
        self.__button_25 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_25, command=self.__button25_click)
        self.__button_25.place(x=self.__x5, y=self.__y2)
        self.__button_26 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_26, command=self.__button26_click)
        self.__button_26.place(x=self.__x6, y=self.__y2)
        self.__button_27 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_27, command=self.__button27_click)
        self.__button_27.place(x=self.__x7, y=self.__y2)

        self.__button_30 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_30, command=self.__button30_click)
        self.__button_30.place(x=self.__x0, y=self.__y3)
        self.__button_31 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_31, command=self.__button31_click)
        self.__button_31.place(x=self.__x1, y=self.__y3)
        self.__button_32 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_32, command=self.__button32_click)
        self.__button_32.place(x=self.__x2, y=self.__y3)
        self.__button_33 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_33, command=self.__button33_click)
        self.__button_33.place(x=self.__x3, y=self.__y3)
        self.__button_34 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_34, command=self.__button34_click)
        self.__button_34.place(x=self.__x4, y=self.__y3)
        self.__button_35 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_35, command=self.__button35_click)
        self.__button_35.place(x=self.__x5, y=self.__y3)
        self.__button_36 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_36, command=self.__button36_click)
        self.__button_36.place(x=self.__x6, y=self.__y3)
        self.__button_37 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_37, command=self.__button37_click)
        self.__button_37.place(x=self.__x7, y=self.__y3)

        self.__button_40 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_40, command=self.__button40_click)
        self.__button_40.place(x=self.__x0, y=self.__y4)
        self.__button_41 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_41, command=self.__button41_click)
        self.__button_41.place(x=self.__x1, y=self.__y4)
        self.__button_42 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_42, command=self.__button42_click)
        self.__button_42.place(x=self.__x2, y=self.__y4)
        self.__button_43 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_43, command=self.__button43_click)
        self.__button_43.place(x=self.__x3, y=self.__y4)
        self.__button_44 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_44, command=self.__button44_click)
        self.__button_44.place(x=self.__x4, y=self.__y4)
        self.__button_45 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_45, command=self.__button45_click)
        self.__button_45.place(x=self.__x5, y=self.__y4)
        self.__button_46 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_46, command=self.__button46_click)
        self.__button_46.place(x=self.__x6, y=self.__y4)
        self.__button_47 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_47, command=self.__button47_click)
        self.__button_47.place(x=self.__x7, y=self.__y4)

        self.__button_50 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_50, command=self.__button50_click)
        self.__button_50.place(x=self.__x0, y=self.__y5)
        self.__button_51 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_51, command=self.__button51_click)
        self.__button_51.place(x=self.__x1, y=self.__y5)
        self.__button_52 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_52, command=self.__button52_click)
        self.__button_52.place(x=self.__x2, y=self.__y5)
        self.__button_53 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_53, command=self.__button53_click)
        self.__button_53.place(x=self.__x3, y=self.__y5)
        self.__button_54 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_54, command=self.__button54_click)
        self.__button_54.place(x=self.__x4, y=self.__y5)
        self.__button_55 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_55, command=self.__button55_click)
        self.__button_55.place(x=self.__x5, y=self.__y5)
        self.__button_56 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_56, command=self.__button56_click)
        self.__button_56.place(x=self.__x6, y=self.__y5)
        self.__button_57 = Button(master, width=5, height=2, background="#EFEFEF", borderwidth=1, textvariable=self.__label_57, command=self.__button57_click)
        self.__button_57.place(x=self.__x7, y=self.__y5)
    
    def __button00_click(self):
        self.__button_clicked(self.__button_00)
        self.__label_00.set("0")
        self.__mensagem_derrota(self.__label_00)
        
        
    def __button01_click(self):
        self.__button_clicked(self.__button_01)
        self.__label_01.set("0")
    
    def __button02_click(self):
        self.__button_clicked(self.__button_02)
        self.__label_02.set("0")
    
    def __button03_click(self):
        self.__button_clicked(self.__button_03)
        self.__label_03.set("0")
    
    def __button04_click(self):
        self.__button_clicked(self.__button_04)
        self.__label_04.set("0")
    
    def __button05_click(self):
        self.__button_clicked(self.__button_05)
        self.__label_05.set("0")
    
    def __button06_click(self):
        self.__button_clicked(self.__button_06)
        self.__label_06.set("0")
    
    def __button07_click(self):
        self.__button_clicked(self.__button_07)    
        self.__label_07.set("0")
    
    def __button10_click(self):
        self.__button_clicked(self.__button_10)
        self.__label_10.set("0")
    
    def __button11_click(self):
        self.__button_clicked(self.__button_11)
        self.__label_11.set("0")
    
    def __button12_click(self):
        self.__button_clicked(self.__button_12)         
        self.__label_12.set("0")
    
    def __button13_click(self):
        self.__button_clicked(self.__button_13)
        self.__label_13.set("0")
    
    def __button14_click(self):
        self.__button_clicked(self.__button_14)
        self.__label_14.set("0")
    
    def __button15_click(self):
        self.__button_clicked(self.__button_15)
        self.__label_15.set("0")
    
    def __button16_click(self):
        self.__button_clicked(self.__button_16)
        self.__label_16.set("0")
    
    def __button17_click(self):
        self.__button_clicked(self.__button_17)
        self.__label_17.set("0")
    
    def __button20_click(self):
        self.__button_clicked(self.__button_20)
        self.__label_20.set("0")
    
    def __button21_click(self):
        self.__button_clicked(self.__button_21)
        self.__label_21.set("0")
    
    def __button22_click(self):
        self.__button_clicked(self.__button_22)
        self.__label_22.set("0")
    
    def __button23_click(self):
        self.__button_clicked(self.__button_23)
        self.__label_23.set("0")
    
    def __button24_click(self):
        self.__button_clicked(self.__button_24)
        self.__label_24.set("0")
    
    def __button25_click(self):
        self.__button_clicked(self.__button_25)
        self.__label_25.set("0")
    
    def __button26_click(self):
        self.__button_clicked(self.__button_26)
        self.__label_26.set("0")
    
    def __button27_click(self):
        self.__button_clicked(self.__button_27)
        self.__label_27.set("0")
    
    def __button30_click(self):
        self.__button_clicked(self.__button_30)
        self.__label_30.set("0")
    
    def __button31_click(self):
        self.__button_clicked(self.__button_31)
        self.__label_31.set("0")
    
    def __button32_click(self):
        self.__button_clicked(self.__button_32)
        self.__label_32.set("0")
    
    def __button33_click(self):
        self.__button_clicked(self.__button_33)
        self.__label_33.set("0")
    
    def __button34_click(self):
        self.__button_clicked(self.__button_34)
        self.__label_34.set("0")
    
    def __button35_click(self):
        self.__button_clicked(self.__button_35)
        self.__label_35.set("0")
    
    def __button36_click(self):
        self.__button_clicked(self.__button_36)
        self.__label_36.set("0")
    
    def __button37_click(self):
        self.__button_clicked(self.__button_37)
        self.__label_37.set("0")
    
    def __button40_click(self):
        self.__button_clicked(self.__button_40)
        self.__label_40.set("0")
    
    def __button41_click(self):
        self.__button_clicked(self.__button_41)
        self.__label_41.set("0")
    
    def __button42_click(self):
        self.__button_clicked(self.__button_42)
        self.__label_42.set("0")
    
    def __button43_click(self):
        self.__button_clicked(self.__button_43)
        self.__label_43.set("0")
    
    def __button44_click(self):
        self.__button_clicked(self.__button_44)
        self.__label_44.set("0")
    
    def __button45_click(self):
        self.__button_clicked(self.__button_45)
        self.__label_45.set("0")
    
    def __button46_click(self):
        self.__button_clicked(self.__button_46)
        self.__label_46.set("0")
    
    def __button47_click(self):
        self.__button_clicked(self.__button_47)
        self.__label_47.set("0")
    
    def __button50_click(self):
        self.__button_clicked(self.__button_50)
        self.__label_50.set("0")
    
    def __button51_click(self):
        self.__button_clicked(self.__button_51)
        self.__label_51.set("0")
    
    def __button52_click(self):
        self.__button_clicked(self.__button_52)
        self.__label_52.set("0")
    
    def __button53_click(self):
        self.__button_clicked(self.__button_53)
        self.__label_53.set("0")
    
    def __button54_click(self):
        self.__button_clicked(self.__button_54)
        self.__label_54.set("0")
    
    def __button55_click(self):
        self.__button_clicked(self.__button_55)
        self.__label_55.set("0")
    
    def __button56_click(self):
        self.__button_clicked(self.__button_56)
        self.__label_56.set("0")
    
    def __button57_click(self):
        self.__button_clicked(self.__button_57)
        self.__label_57.set("0")
    

    def __button_clicked(self, button):
        button["state"] = DISABLED
        button["background"] = "#999999"
        button["borderwidth"] = 2
        button["relief"] = FLAT
    
    def __mensagem_derrota(self, label):
        if label.get() == "0":
            messagebox.showinfo("Info", "Perdeu")
        

    def __tem_bomba(self, button):
        tupla = (0,0)
        valor = self.negocio.tem_bomba(tupla)
        return valor    

if __name__ == "__main__":
    janela = Tk()
    CampoMinadoJogoJanela(janela)
    janela.mainloop()