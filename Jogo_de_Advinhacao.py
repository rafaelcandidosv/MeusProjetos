import random


def advinhacao():

    print("\n")
    print("\t\t\t\t\t********************************")
    print("\t\t\t\t\tBem vindo no jogo de Advinhação!")
    print("\t\t\t\t\t********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("\nQual o nível de dificuldade ? \n[1] FÁCIL [2] MÉDIO [3] DIFÍCIIL")

    nivel = int(input("\nEscolha o nível de dificuldade: "))

    # PASSO 1 - NÍVEL DE DIFICULDADE

    while (nivel < 1 or nivel > 3):
        print("\nVocê digitou um nível inexistente, tente digitar um número entre 1 e 3: ")
        nivel = int(input("\nEscolha o nível de dificuldade: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    elif (nivel == 3):
        total_de_tentativas = 5

        # PASSO 2 - NÚMERO DE RODADAS

    for rodada in range(1, total_de_tentativas + 1):
        print("\ntentativa {} de {}: ".format(rodada, total_de_tentativas))
        chute_str = input("\nDigite um número entre 1 e 100: ")
        print("\n\nVocê digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("\nVocê deve digitar um número entre 1 e 100, tente novamente")
            continue

            # PASSO 3 - CONTINUAÇÃO DO CÓDIGO

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("\nVocê acertou\nSua pontuação alcaçada é: {}".format(pontos))
            break
        else:
            if (maior):
                print(
                    "\nVocê errou! O número que você digitou é maior do que o número secreto")
            elif (menor):
                print(
                    "\nVocê errou! O número que você digitou é menor do que o número secreto")
            PontosPerdidos = abs(numero_secreto - chute)
            pontos = pontos - PontosPerdidos

    print("\nFim do jogo!")


if (__name__ == "__main__"):
    advinhacao()
