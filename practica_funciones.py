"""
Practica 1
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.
"""


def devolver_distintos(num1, num2, num3):
    lista_numeros = [num1, num2, num3]
    if sum(lista_numeros) > 15:
        return max(lista_numeros)
    elif sum(lista_numeros) < 10:
        return min(lista_numeros)
    elif sum(lista_numeros) >= 3 and sum(lista_numeros) <= 15:
        for n in lista_numeros:
            if n != max(lista_numeros) and n != min(lista_numeros):
                return n


"""
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
"""


def letras_unicas(palabra):
    lista_letras = set(palabra.lower())
    return sorted(lista_letras)


"""
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas
"""


def ceros_consecutivos(*args):
    consecutivo = False
    for i in range(len(args) - 1):  # Iterar hasta el penúltimo elemento
        if args[i] == 0 and args[i + 1] == 0:  # Verificar si ambos son cero
            consecutivo = True
            break
    return consecutivo


"""Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos."""


def contar_primos(size):
    lista = [n for n in range(0, size + 1) if n % 2 == 1 and n != 1]
    print(f"Lista de números primos: {lista}")
    print(f"Cantidad de números encontrados: {len(lista)}")


contar_primos(20)
