"""
Administrador de Recetas
========================
Programa que gestiona recetas organizadas en categorías (carpetas) dentro
del directorio 'Recetas' ubicado en el Escritorio del usuario.

Funcionalidades:
    1. Leer una receta
    2. Crear una receta
    3. Crear una categoría
    4. Eliminar una receta
    5. Eliminar una categoría
    6. Salir del programa
"""

import os                    # Para limpiar la consola de forma multiplataforma
from pathlib import Path     # Para manejar rutas de archivos de forma multiplataforma


# ---------------------------------------------------------------------------
# CONFIGURACIÓN: Ruta base al directorio 'Recetas' en el Escritorio
# Path.home() devuelve el directorio del usuario (ej: /Users/nombre en Mac,
# C:/Users/nombre en Windows). "Desktop" funciona en ambos sistemas.
# ---------------------------------------------------------------------------
RECETAS_DIR = Path.home() / "Desktop" / "Recetas"


# ---------------------------------------------------------------------------
# UTILIDADES
# ---------------------------------------------------------------------------

def limpiar_consola():
    """Limpia la terminal. Usa 'cls' en Windows y 'clear' en Mac/Linux."""
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_menu():
    """Muestra el menú principal con las opciones disponibles."""
    print("=" * 45)
    print("       ADMINISTRADOR DE RECETAS")
    print("=" * 45)
    print(f"  Directorio: {RECETAS_DIR}")
    print("-" * 45)
    print("  1. Leer una receta")
    print("  2. Crear una receta")
    print("  3. Crear una categoría")
    print("  4. Eliminar una receta")
    print("  5. Eliminar una categoría")
    print("  6. Salir")
    print("=" * 45)


def listar_categorias():
    """
    Muestra todas las subcarpetas (categorías) dentro de RECETAS_DIR.
    Retorna una lista de objetos Path de las carpetas encontradas.
    """
    # iterdir() itera sobre el contenido del directorio
    # is_dir() filtra solo las carpetas (categorías)
    categorias = [item for item in RECETAS_DIR.iterdir() if item.is_dir()]

    if not categorias:
        print("  No hay categorías disponibles.")
        return []

    print("\n  Categorías disponibles:")
    for i, cat in enumerate(categorias, start=1):
        print(f"    {i}. {cat.name}")

    return categorias


def listar_recetas(categoria_path):
    """
    Muestra todos los archivos .txt (recetas) dentro de una carpeta de categoría.
    Retorna una lista de objetos Path de los archivos encontrados.
    """
    # glob("*.txt") busca todos los archivos con extensión .txt
    recetas = list(categoria_path.glob("*.txt"))

    if not recetas:
        print(f"  No hay recetas en '{categoria_path.name}'.")
        return []

    print(f"\n  Recetas en '{categoria_path.name}':")
    for i, receta in enumerate(recetas, start=1):
        # .stem devuelve el nombre del archivo sin la extensión
        print(f"    {i}. {receta.stem}")

    return recetas


def pedir_categoria():
    """
    Solicita al usuario que ingrese el nombre de una categoría existente.
    Retorna el objeto Path de la categoría o None si no existe.
    """
    categorias = listar_categorias()
    if not categorias:
        return None

    nombre = input("\n  Ingresa el nombre de la categoría: ").strip()
    categoria_path = RECETAS_DIR / nombre

    if not categoria_path.is_dir():
        print(f"\n  ✖ La categoría '{nombre}' no existe.")
        return None

    return categoria_path


def pedir_receta(categoria_path):
    """
    Solicita al usuario que ingrese el nombre de una receta existente
    dentro de la categoría dada.
    Retorna el objeto Path del archivo .txt o None si no existe.
    """
    recetas = listar_recetas(categoria_path)
    if not recetas:
        return None

    nombre = input("\n  Ingresa el nombre de la receta (sin .txt): ").strip()
    receta_path = categoria_path / f"{nombre}.txt"

    if not receta_path.is_file():
        print(
            f"\n  ✖ La receta '{nombre}' no existe en '{categoria_path.name}'.")
        return None

    return receta_path


# ---------------------------------------------------------------------------
# OPCIONES DEL MENÚ
# ---------------------------------------------------------------------------

def leer_receta():
    """
    Opción 1: Pide categoría y receta, luego muestra el contenido del archivo .txt.
    """
    print("\n--- LEER RECETA ---")
    categoria_path = pedir_categoria()
    if not categoria_path:
        return

    receta_path = pedir_receta(categoria_path)
    if not receta_path:
        return

    # read_text() lee todo el contenido del archivo como string
    # encoding="utf-8" asegura compatibilidad con caracteres especiales (tildes, ñ)
    print(f"\n{'=' * 45}")
    print(f"  {receta_path.stem.upper()}")
    print(f"{'=' * 45}")
    print(receta_path.read_text(encoding="utf-8"))
    input("\n  Presiona ENTER para continuar...")


def crear_receta():
    """
    Opción 2: Pide categoría, nombre de nueva receta y contenido, luego crea el archivo.
    Verifica que el archivo no exista antes de crearlo.
    """
    print("\n--- CREAR RECETA ---")
    categoria_path = pedir_categoria()
    if not categoria_path:
        return

    # Pedir nombre hasta que sea válido (que no exista)
    while True:
        nombre = input("\n  Nombre de la nueva receta (sin .txt): ").strip()
        if not nombre:
            print("  ✖ El nombre no puede estar vacío.")
            continue

        receta_path = categoria_path / f"{nombre}.txt"

        if receta_path.exists():
            print(
                f"  ✖ Ya existe una receta llamada '{nombre}'. Elige otro nombre.")
        else:
            break

    print("  Escribe el contenido de la receta.")
    print("  (Escribe 'FIN' en una línea nueva para terminar)\n")

    lineas = []
    while True:
        linea = input()
        if linea.strip().upper() == "FIN":
            break
        lineas.append(linea)

    contenido = "\n".join(lineas)

    # write_text() escribe el contenido en el archivo, creándolo si no existe
    receta_path.write_text(contenido, encoding="utf-8")
    print(
        f"\n  ✔ Receta '{nombre}' creada en la categoría '{categoria_path.name}'.")
    input("  Presiona ENTER para continuar...")


def crear_categoria():
    """
    Opción 3: Pide nombre de nueva categoría, verifica que no exista y crea la carpeta.
    """
    print("\n--- CREAR CATEGORÍA ---")

    # Mostrar categorías actuales para referencia del usuario
    listar_categorias()

    nombre = input("\n  Nombre de la nueva categoría: ").strip()

    if not nombre:
        print("  ✖ El nombre no puede estar vacío.")
        input("  Presiona ENTER para continuar...")
        return

    nueva_cat = RECETAS_DIR / nombre

    if nueva_cat.exists():
        print(f"  ✖ Ya existe una categoría llamada '{nombre}'.")
        input("  Presiona ENTER para continuar...")
        return

    # mkdir() crea el directorio. parents=True crea directorios intermedios si hacen falta
    nueva_cat.mkdir(parents=True)
    print(f"\n  ✔ Categoría '{nombre}' creada correctamente.")
    input("  Presiona ENTER para continuar...")


def eliminar_receta():
    """
    Opción 4: Pide categoría y receta, luego elimina el archivo .txt.
    """
    print("\n--- ELIMINAR RECETA ---")
    categoria_path = pedir_categoria()
    if not categoria_path:
        return

    receta_path = pedir_receta(categoria_path)
    if not receta_path:
        return

    confirmacion = input(
        f"\n  ¿Seguro que quieres eliminar '{receta_path.stem}'? (s/n): "
    ).strip().lower()

    if confirmacion == "s":
        # unlink() elimina un archivo
        receta_path.unlink()
        print(f"\n  ✔ Receta '{receta_path.stem}' eliminada.")
    else:
        print("  Operación cancelada.")

    input("  Presiona ENTER para continuar...")


def eliminar_categoria():
    """
    Opción 5: Pide nombre de categoría y la elimina.
    Si tiene archivos dentro, avisa al usuario y pide confirmación extra.
    """
    print("\n--- ELIMINAR CATEGORÍA ---")
    categoria_path = pedir_categoria()
    if not categoria_path:
        return

    # Obtener archivos dentro de la carpeta
    archivos = list(categoria_path.iterdir())

    if archivos:
        print(
            f"\n  ⚠ La categoría '{categoria_path.name}' contiene {len(archivos)} archivo(s):")
        for archivo in archivos:
            print(f"    - {archivo.name}")
        confirmacion = input(
            "\n  ¿Estás SEGURO de que quieres eliminar la categoría y TODO su contenido? (s/n): "
        ).strip().lower()
        if confirmacion != "s":
            print("  Operación cancelada.")
            input("  Presiona ENTER para continuar...")
            return

        # Eliminar todos los archivos dentro antes de borrar la carpeta
        for archivo in archivos:
            archivo.unlink()
    else:
        confirmacion = input(
            f"\n  ¿Seguro que quieres eliminar la categoría '{categoria_path.name}'? (s/n): "
        ).strip().lower()
        if confirmacion != "s":
            print("  Operación cancelada.")
            input("  Presiona ENTER para continuar...")
            return

    # rmdir() elimina una carpeta vacía
    categoria_path.rmdir()
    print(f"\n  ✔ Categoría '{categoria_path.name}' eliminada correctamente.")
    input("  Presiona ENTER para continuar...")


# ---------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------------------

def main():
    """
    Función principal que controla el flujo del programa.
    Verifica que el directorio 'Recetas' exista y muestra el menú en bucle.
    """
    # Verificar que el directorio base 'Recetas' exista en el Escritorio
    if not RECETAS_DIR.exists():
        print(f"\n  ⚠ No se encontró el directorio:\n  {RECETAS_DIR}")
        crear = input("\n  ¿Deseas crearlo ahora? (s/n): ").strip().lower()
        if crear == "s":
            RECETAS_DIR.mkdir(parents=True)
            print(f"  ✔ Directorio '{RECETAS_DIR}' creado.")
        else:
            print("  El programa no puede continuar sin el directorio. Adiós.")
            return

    limpiar_consola()

    # Diccionario que mapea cada opción con su función correspondiente
    opciones = {
        "1": leer_receta,
        "2": crear_receta,
        "3": crear_categoria,
        "4": eliminar_receta,
        "5": eliminar_categoria,
    }

    # Bucle principal: el programa corre hasta que el usuario elija salir
    while True:
        mostrar_menu()
        eleccion = input("\n  Elige una opción (1-6): ").strip()

        if eleccion == "6":
            limpiar_consola()
            print("\n  ¡Hasta pronto! 👋\n")
            break
        elif eleccion in opciones:
            # Llamar a la función asociada a la opción elegida
            opciones[eleccion]()
            limpiar_consola()
        else:
            print("\n  ✖ Opción no válida. Introduce un número del 1 al 6.")
            input("  Presiona ENTER para continuar...")
            limpiar_consola()


# Punto de entrada: solo ejecuta main() si se corre este archivo directamente
if __name__ == "__main__":
    main()
