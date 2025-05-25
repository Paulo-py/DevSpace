# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 2

# import 
import random
from os import system, name

# Função para limpar a tela a cada execução

def limpaTela():
    
    #Windows
    if name == 'nt':
        system('cls')
    
    # Mac ou Linux
    else:
        system('clear')

def game():

    limpaTela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abixo:\n")

    # Lista de valores para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    #Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)

    # List comprehension
    letrasDescobertas = ['_' for letra in palavra]

    # Lista para letras erradas

    letrasErradas = []

    # Número de chances
    chances = 6

    # Loop enquanto números de chances for maior do que zero.
    while chances > 0:
    # Print
        print(" ".join(letrasDescobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letrasErradas))

        #Tentativas
        tentativa = input("\nDigite uma letra: ").lower()

        # Condicional
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letrasDescobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letrasErradas.append(tentativa)

        # Condicional
        if "_" not in letrasDescobertas:
            print("\Você venceu, a palavra era", palavra)
            break

    # Condicional
    if "_" in letrasDescobertas:
        print("\nVocê perdeu, a palavra era:", palavra)


# Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")