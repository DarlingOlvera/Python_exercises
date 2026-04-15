"""
    JUEGO DE ADIVINAR EL NUMERO
    -Se le pide al usuario su nombre
    -Se le pide que adivine un numero entre 1 y 100 
    -Solo tiene 8 intentos
    -Si el numero es menor a 1 o mayor a 100 decir que eligio un numero no permitido
    -Si el numero es menor al elegido por el prograda decir Algo de error y que eligio un numero menor al pensado,
    lo mismo con un numero mayor
    -Si acertó se le informa que ganó y cuantos intentos tomó
"""

from random import *

print("""
      ¡ADIVINA EL NÚMERO!
      ================================
      -Adivina un número del 1 al 100 y gana el juego
      -Tienes  8 intentos para adivinar
      -Para salir del juego escribe 's'
      ================================\n
      """)

intento = 0
nombre = input("Ingresa tu nombre:")
numero_aleatorio = randint(1, 100)

while intento < 8:
    print(f"Jugador: {nombre} =========== Intento No. {intento + 1} \n")
    num = input("Ingresa un número del 1 al 100:")
    intento += 1

    if num == 's':
        break
    elif int(num) not in range(1, 101):
        print("El número ingresado se sale del rango permitido")
        continue
    elif int(num) < numero_aleatorio:
        print("El valor ingresado es menor al número esperado")
    elif int(num) > numero_aleatorio:
        print("El valor ingresado es mayor al número esperado")
    elif int(num) == numero_aleatorio:
        print("¡Adivinaste! El número esperado era: {}".format(numero_aleatorio))
        intentos_tomados = 8 - intento
        print("Te tomó {} intentos\n".format(intentos_tomados))
        break

if int(num) != numero_aleatorio:
    print("Lo siento. El número era {}\n".format(nombre, numero_aleatorio))

print("GRACIAS POR JUGAR")
