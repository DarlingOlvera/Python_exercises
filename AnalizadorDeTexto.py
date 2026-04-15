"""
Programa que recibe cualquier texto y tres tipos de letras a analizar.
Devuelve:
-Cantidad de veces que aparecen las letras elegidas
-Cuantas palabras hay en total
-primera y ultima letra del texto
-palabras en orden inverso
-Aparece la palabra "python"?
"""

input_text = input("Ingrese un texto: ")
letter1 = input("Ingrese la primera letra a analizar: ")
letter2 = input("Ingrese la segunda letra a analizar: ")
letter3 = input("Ingrese la tercera letra a analizar: ")


# Contar la cantidad de veces que aparecen las letras elegidas
count_letter1 = input_text.lower().count(letter1.lower())
count_letter2 = input_text.lower().count(letter2.lower())
count_letter3 = input_text.lower().count(letter3.lower())

print(f"La letra '{letter1}' aparece {count_letter1} veces.")
print(f"La letra '{letter2}' aparece {count_letter2} veces.")
print(f"La letra '{letter3}' aparece {count_letter3} veces.")

# Contar la cantidad de palabras en total
words = input_text.split()
total_words = len(words)
print(f"El texto tiene un total de {total_words} palabras.")
print(f"La primera palabra del texto es {words[0]}")
print(f"La ultima palabra del texto es {words[-1]}")

# texto al reves

reverse_phrase = " ".join(words[::-1])
print(f"El texto al revés se lee como: {reverse_phrase}")

if "python" in input_text:
    exist = 'Si'
else:
    exist = 'No'

print("Existe python en el texto?: {}".format(exist))
