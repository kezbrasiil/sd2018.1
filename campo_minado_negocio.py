from random import randint
import os.path

class CampoMinadoNegocio(object):
    def __init__(self):
        self.__contador = -1
        self.__bombas = []
        self.__gerar_bombas()
        self.imprimir_bombas()

    def __gerar_bombas(self):
        while(len(self.__bombas) < 14):
            linha = randint(0,5)
            coluna = randint(0,8)
            tupla = (linha,coluna)
            if tupla not in self.__bombas:
                self.__bombas.append(tupla)
    
    def incrementar_jogada(self):
        self.__contador = self.__contador + 1
        return self.__contador

    def tem_bomba(self, tupla):
        var = False
        if tupla in self.__bombas:
            var = True
        return var
    
    def bombas_vizinhas(self, tupla):
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
    
    def vitoria(self):
        var = False
        if self.__contador == 14:
            var = True
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
    pass
