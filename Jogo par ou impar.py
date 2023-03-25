import random

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

palpite_jogador1 = input("Jogador 1, escolha par ou ímpar: ")
valor_jogador1 = int(input("Jogador 1, digite um valor de 1 a 5: "))
palpite_jogador2 = input("Jogador 2, escolha par ou ímpar: ")
valor_jogador2 = int(input("Jogador 2, digite um valor de 1 a 5: "))

if valor_jogador1 < 1 or valor_jogador1 > 5 or valor_jogador2 < 1 or valor_jogador2 > 5:
    print("Esta rodada não valeu! Os valores devem ser de 1 a 5.")
else:

    soma_valores = valor_jogador1 + valor_jogador2
    print("A soma dos valores é:", soma_valores)

    resultado = par_ou_impar(soma_valores)
    print("O resultado é", resultado)

    if resultado == palpite_jogador1:
        print("Jogador 1 ganhou!")
    else:
        print("Jogador 2 ganhou!")
