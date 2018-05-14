from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from campo_minado_negocio import CampoMinado



campo_minado = CampoMinado()



def criar_novo_jogo(linhas,colunas):
    campo_minado.criar_novo_jogo(linhas, colunas)


def efetuar_jogada(linha, coluna):
    return campo_minado.jogada(linha, coluna)


def retorna_tabuleiro():
    return campo_minado.imprimir_tabuleiro()


def jogadas_restantes():
    return campo_minado.jogadas_restantes

def jogada(linha, coluna):
    return campo_minado.jogada(linha,coluna)

def bombas():
    return campo_minado.bombas()



def server():
    serverRPC = SimpleJSONRPCServer(('localhost', 7002))
    serverRPC.register_function(criar_novo_jogo)
    serverRPC.register_function(efetuar_jogada)
    serverRPC.register_function(jogadas_restantes)
    serverRPC.register_function(retorna_tabuleiro)
    serverRPC.register_function(jogada)
    serverRPC.register_function(bombas)
    print("Starting server")
    serverRPC.serve_forever()
