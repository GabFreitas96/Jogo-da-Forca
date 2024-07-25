import random
import os

# Função para desenhar o boneco
def desenhar_boneco(tentativas_restantes):
    desenhos = [
        "  +---+\n  |   |\n      \n      \n      \n      \n      ",  # Sem partes
        "  +---+\n  |   |\n  O   \n      \n      \n      \n      ",  # Cabeça
        "  +---+\n  |   |\n  O   \n  |   \n      \n      \n      ",  # Corpo
        "  +---+\n  |   |\n  O   \n /|   \n      \n      \n      ",  # Braço esquerdo
        "  +---+\n  |   |\n  O   \n /|\\ \n      \n      \n      ",  # Braços
        "  +---+\n  |   |\n  O   \n /|\\ \n /    \n      \n      ",  # Perna direita
        "  +---+\n  |   |\n  O   \n /|\\ \n / \\ \n      \n      ",  # Ambas as pernas
        "  +---+\n  |   |\n  >->-O "  # Cordão no pescoço (última tentativa)
    ]
    print(desenhos[7 - tentativas_restantes])

def jogar_forca():
    # Lista de palavras para o jogo
    word_list = [  
        "burpee", 
        "deadlift", 
        "kettlebell", 
        "squat", 
        "pullup", 
        "boxjump", 
        "snatch", 
        "clean", 
        "muscleup", 
        "wod"
    ]

    # Escolher uma palavra aleatória da lista
    word_to_guess = random.choice(word_list).upper()
    guessed_word = ['_' for _ in word_to_guess]
    attempts_left = 7
    used_letters = []

    os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela do terminal
    print(">>>>> JOGO DA FORCA <<<<<")
    print(f"A palavra tem {len(word_to_guess)} letras.")
    print("Vamos começar! Tente adivinhar a palavra letra por letra. O tema é: CROSSFIT")

    while attempts_left > 0 and '_' in guessed_word:
        desenhar_boneco(attempts_left)
        print(f"\nPalavra: {' '.join(guessed_word)}")
        print(f"Letras já usadas: {', '.join(used_letters)}")
        print(f"Tentativas restantes: {attempts_left}")

        guess = input("Digite uma letra: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Por favor, insira apenas uma letra.")
            continue

        if guess in used_letters:
            print("Você já usou essa letra. Tente outra.")
            continue

        used_letters.append(guess)

        if guess in word_to_guess:
            for index, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            attempts_left -= 1
            print(f"A letra '{guess}' não está na palavra.")

    desenhar_boneco(attempts_left)
    if '_' not in guessed_word:
        print("\nParabéns! Você adivinhou a palavra:", ''.join(guessed_word))
    else:
        print("\nVocê perdeu! A palavra era:", word_to_guess)

def main():
    while True:
        jogar_forca()
        resposta = input("\nDeseja jogar novamente? (s/n): ").lower()
        if resposta != 's':
            print("Obrigado por jogar!")
            break

if __name__ == "__main__":
    main()
