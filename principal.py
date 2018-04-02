from tabuleiro import *

j = Jogo()
j.inicio()

print("Menu:\n")
print("1. Iniciar jogo;")
print("2. Visualizar tabuleiro;")
print("3. Fazer jogada;")
print("4. Retornar para jogo passado;")
print("5. Acabar partida; \n")

print ("Escolha uma numeração do menu de 1 a 5, para fazer a acao desejada.")
escolha = int(input("Numero do menu"))
print("")


if escolhe == 1:
        j.criar_tabuleiro()
        j.menu()

elif escolha == 2:
        j.visualizar_tabuleiro()
        j.menu()

elif escolha == 3:
        j.jogada()
        j.menu()

elif escolha == 4:
        j.finalizar_jogo()

