"""
JUEGO DEL AHORCADO
-se elige una palabra secreta y solo se muestran la cantidad de lineas que tiene la palabra
-El jugador elige una letra
-Si la letra se encuentra en la palabra, mostrar en que posicion se encuentra
-si no se encuentra se pierde una vida
-se tiene un total de 6 vidas
"""

from random import *


def choose_a_word(palabras):
    shuffle(palabras)
    selected_word = choice(palabras)
    return selected_word


def verify_letter(letter, selected_word):
    word_as_list = list(selected_word)
    l_position = []
    # enumerate() devuelve el índice real de cada iteración
    # .index() siempre devuelve la primera aparición, no funciona para letras repetidas
    for index, l in enumerate(word_as_list):
        if l.lower() == letter.lower():
            l_position.append(index)
    return l_position


def verify_word(chosen_word, game_word):
    user_word = "".join(game_word)
    if chosen_word.lower() == user_word.lower():
        return True
    else:
        return False


def main_game():
    palabras = [
        "python",
        "programacion",
        "computadora",
        "teclado",
        "monitor",
        "javascript",
        "desarrollo",
        "algoritmo",
        "variable",
        "funcion",
        "diccionario",
        "lista"
    ]
    remaining_lifes = 6
    word = choose_a_word(palabras)
    word_length = len(word)
    list_word = ['__'] * word_length
    print("""
          BIENVENIDO AL JUEGO DEL AHORCADO
          - Tienes 6 intentos
          - Adivina la palabra para ganar
          =================================\n
          """)

    while remaining_lifes > 0:
        print(f"Intentos restantes:{remaining_lifes}\n")
        print(f"{list_word}\n")
        user_letter = input("Ingresa una letra A-Z: ")
        print("\n")
        indexes = verify_letter(user_letter, word)
        if len(indexes) > 0:
            for i in indexes:
                list_word[i] = user_letter.upper()
        else:
            remaining_lifes -= 1

        win = verify_word(word, list_word)

        if win == True:
            print(f"{list_word}\n")
            print("¡Felicidades! Ganaste el juego")
            break

    if win == False:
        print("\n")
        print(f"¡Lo siento! la palabra correcta es: {word}")


main_game()
