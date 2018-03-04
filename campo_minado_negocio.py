from random import randint

class CampoMinadoNegocio(object):
    def __init__(self):
        self.bombas = []
        self.__gerar_bombas()

    def __gerar_bombas(self):
        for j in range(10):
            x = randint(0,7)
            y = randint(0,5)
            self.bombas.append((x,y))

if __name__ == "__main__":
    negocio = CampoMinadoNegocio()
    print(negocio.bombas)
