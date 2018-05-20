from random import randint
from os.path import isfile
import json

COORDENADAS_INVALIDAS = "Coodenadas Invalidas"
JOGADA_SEGURA = "Jogada Segura"
GAME_OVER = "Game Over"

class CampoMinado:

    def criar_novo_jogo(self, linha, coluna):
        """ Inicializando campo minado com linha X coluna posicoes """
        self.__linha = int(linha)
        self.__coluna = int(coluna)
        self.jogadas_restantes = self.__calcular_total_jogadas(linha, coluna)
        self.__tabuleiro = self.__inicializar_tabuleiro(linha, coluna)
        self.__coordenadas_bombas = self.__distribuir_bombas(linha,coluna)

    def jogada(self, linha, coluna):
        """ 1. Verifica se as coordenadas são válidas
            2. Validar se acertei uma mina: 
                caso sim:
                    Game Over 
                caso não: 
                    marcar a posição escolhida no tabuleiro com a quantidade de 
                    bombas existentes nos nós vizinhos """
        linha = int(linha)
        coluna = int(coluna)

        if not self.__validar_coordenadas(linha, coluna):
            return COORDENADAS_INVALIDAS
        
        if  (linha, coluna) in self.__coordenadas_bombas:
            return GAME_OVER
        
        self.__tabuleiro[linha][coluna] = str(self.__conta_bombas_vizinhos(linha, coluna))
        self.jogadas_restantes -=1
        self.__salvar_jogo()
        return JOGADA_SEGURA

    def imprimir_tabuleiro(self):
        for posicao in self.__tabuleiro:
            print(str(posicao))

    def tabuleiro(self):
        return self.__tabuleiro

    def qtd_jogadas(self):
        return self.jogadas_restantes

    def __inicializar_tabuleiro(self, linha, coluna):
        return [[str('X') for x in range(coluna)] for j in range(linha)]

    def __distribuir_bombas(self, linha, coluna):
        """ Consulta o total de bombas permitidas e aleatoriamente definie as coordenadas de cada bomba"""
        coordenadas_bombas = [(randint(0, linha - 1), randint(0, coluna - 1)) for x in range(self.__total_bombas())]
        print(coordenadas_bombas)
        return coordenadas_bombas

    def __total_bombas(self):
        return int((self.__linha*self.__coluna)/3)
    
    def __calcular_total_jogadas(self,linha, coluna):
        return (linha*coluna) - self.__total_bombas()

    def __validar_coordenadas(self, linha, coluna):
        if linha in range(0, self.__linha) and coluna in range(0, self.__coluna):
            return True
        return False
    
    def __coordenada_e_bomba(self, coordenada):
        """ Verifica se a coodenada informada possui uma bomba """
        return coordenada in self.__coordenadas_bombas

    def __conta_bombas_vizinhos(self, linha, coluna):
        """ Soma -1,0 e 1 em linha e coluna e verifica se elas possuem uma bomba, caso sim, essa coordenada entra em uma lista """
        return len([(linha + x, coluna + y) for x in (-1,0,1) for y in (-1,0,1) if self.__coordenada_e_bomba((linha + x, coluna + y))])

    def __salvar_jogo(self):
        """ Salva o estado do jogo para poder comecar a jogar de onde parou na proxima vez """
        jogo = {
            'linha': self.__linha,
            'coluna': self.__coluna,
            'restante': self.jogadas_restantes,
            'tabuleiro': self.__tabuleiro,
            'cordenadas': self.__coordenadas_bombas,
            'incompleto': True
        }

        file = open("jogo_salvo.json", 'w')

        file.write(json.dumps(jogo))
        file.close()

    def restaurar(self, jogo):
        self.__linha = jogo['linha']
        self.__coluna = jogo['coluna']
        self.jogadas_restantes = jogo['restante']
        self.__tabuleiro = jogo['tabuleiro']
        self.__coordenadas_bombas = jogo['cordenadas']

    def jogo_incompleto(self):
        if isfile("jogo_salvo.json"):
            arquivo = open("jogo_salvo.json")
            jogo = json.loads(arquivo.read())
            incompleto = jogo['incompleto']
            arquivo.close()
            return incompleto
        else:
            print("Não há jogo salvo !\n")
            return False