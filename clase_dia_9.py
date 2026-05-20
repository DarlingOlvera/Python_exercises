# Uso del modulo collections
import re
from datetime import datetime, date, timedelta
import os
import shutil
from collections import Counter, defaultdict, namedtuple

numeros = [8, 2, 5, 4, 5, 6, 6, 8, 9, 1, 5, 5, 7]

print(Counter(numeros))

frase = 'Al pan, pan, y al vino, vino'

print(Counter(frase.split()))

mi_dic = {"uno": "verde", "dos": "azul", "tres": "rojo"}

mi_dic = defaultdict(lambda: "nada", mi_dic)

Persona = namedtuple('Persona', ['nombre', 'edad', 'peso'])

ariel = Persona('Ariel', 40, 80)

# ─────────────────────────────────────────
# Uso del módulo shutil
# shutil (shell utilities) permite realizar operaciones de alto nivel
# sobre archivos y directorios: copiar, mover, renombrar y eliminar.
# ─────────────────────────────────────────

# --- Preparar archivos de prueba ---
# Creamos un archivo de origen con algo de contenido
with open("origen.txt", "w") as f:
    f.write("Hola, este es el archivo de origen.\n")

# 1. Copiar un archivo (origen → destino)
#    shutil.copy() copia el contenido Y los permisos del archivo
shutil.copy("origen.txt", "copia.txt")
print("Archivo copiado: copia.txt")

# 2. Mover (o renombrar) un archivo
#    shutil.move() funciona entre distintos directorios también
shutil.move("copia.txt", "movido.txt")
print("Archivo movido a: movido.txt")

# 3. Copiar un directorio completo (con todo su contenido)
#    shutil.copytree() requiere que el destino NO exista aún
os.mkdir("carpeta_origen")
with open("carpeta_origen/archivo.txt", "w") as f:
    f.write("Archivo dentro de la carpeta.\n")

shutil.copytree("carpeta_origen", "carpeta_copia")
print("Directorio copiado: carpeta_copia/")

# 4. Eliminar un directorio completo (¡irreversible!)
#    shutil.rmtree() borra la carpeta y todo su contenido
shutil.rmtree("carpeta_origen")
shutil.rmtree("carpeta_copia")
print("Directorios eliminados.")

# 5. Limpiar archivos sueltos de prueba
os.remove("origen.txt")
os.remove("movido.txt")
print("Archivos de prueba eliminados. ¡Ejemplo finalizado!")

# ─────────────────────────────────────────
# Uso del módulo datetime
# datetime permite trabajar con fechas y horas: crearlas, compararlas,
# calcular diferencias y darles formato legible.
# ─────────────────────────────────────────

# 1. Fecha y hora actual
ahora = datetime.now()
print("Ahora:", ahora)                          # 2026-05-19 14:30:00.123456

# 2. Solo la fecha de hoy
hoy = date.today()
print("Hoy:", hoy)                              # 2026-05-19

# 3. Crear una fecha específica
cumple = date(1990, 8, 15)                      # 15 de agosto de 1990
print("Cumpleaños:", cumple)

# 4. Calcular diferencia entre fechas (devuelve un timedelta)
diferencia = hoy - cumple
print("Días vividos:", diferencia.days)

# 5. Sumar o restar tiempo con timedelta
en_una_semana = hoy + timedelta(weeks=1)
ayer = hoy - timedelta(days=1)
print("En una semana:", en_una_semana)
print("Ayer fue:", ayer)

# 6. Dar formato legible a una fecha con strftime
#    %d = día, %m = mes, %Y = año con 4 dígitos, %H:%M = hora:minuto
formato_legible = ahora.strftime("%d/%m/%Y %H:%M")
print("Fecha formateada:", formato_legible)     # ej: 19/05/2026 14:30

# 7. Convertir un string a fecha con strptime (el inverso de strftime)
texto = "25/12/2026"
navidad = datetime.strptime(texto, "%d/%m/%Y")
print("Navidad:", navidad.date())

# ─────────────────────────────────────────
# Expresiones regulares (módulo re) — Validar un email
# re permite buscar, validar y extraer texto usando patrones.
# ─────────────────────────────────────────

# Patrón para validar un email:
#   ^                  → inicio de la cadena
#   [a-zA-Z0-9._%+-]+ → usuario: letras, números y caracteres permitidos (. _ % + -)
#   @                  → arroba literal
#   [a-zA-Z0-9.-]+    → dominio: letras, números, puntos y guiones
#   \.                 → punto literal que separa dominio de TLD
#   [a-zA-Z]{2,}      → TLD: mínimo 2 letras (com, mx, org, ...)
# .  (\.[a-zA-Z])* -> Caso de que contenga o no un dominio extra
#   $                  → fin de la cadena
patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\.[a-zA-Z])*$'


def validar_email(email):
    return bool(re.match(patron_email, email))


# Pruebas
print(validar_email("usuario@gmail.com"))     # True
print(validar_email("user.name+tag@co.mx"))   # True
print(validar_email("sin_arroba.com"))         # False
print(validar_email("@dominio.com"))           # False


def verificar_cp(cp):
    patron = r'^([a-zA-Z0-9]{2})[0-9]{4}$'

    resultado = bool(re.search(patron, cp))

    if resultado:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")
