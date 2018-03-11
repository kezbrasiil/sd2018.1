from random import randint

class CampoMinadoNegocio(object):
    def __init__(self):
        self.__contador = -1
        self.__bombas = []
        self.__gerar_bombas()

    def __gerar_bombas(self):
        while(len(self.__bombas) < 10):
            x = randint(0,7)
            y = randint(0,5)
            tupla = (x,y)
            if tupla not in self.__bombas:
                self.__bombas.append((x,y))
    
    def incrementar_jogada(self):
        self.__contador = self.__contador + 1
        return self.__contador
    
    def recuperar_contador():
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
    
    def imprimir_bombas(self):
        print(self.__bombas)

if __name__ == "__main__":
    negocio = CampoMinadoNegocio()
    negocio.imprimir_bombas()
    negocio.bombas_vizinhas((1,1))
