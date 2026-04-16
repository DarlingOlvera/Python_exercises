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
def devolver_distintos(num1,num2,num3):
    lista_numeros = [num1,num2,num3]
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
    #pendiente
    cero_count = 0
    for val in args:
        print(f"{val}")

ceros_consecutivos(1,0,2,0,0,3)
        
        
