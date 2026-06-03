from bs4 import BeautifulSoup
import requests

# Conjunto con las valoraciones que nos interesan (4 y 5 estrellas)
ESTRELLAS_ALTAS = {"Four", "Five"}

# Prueba con la primera página; cambiar a range(1, 51) para todas las páginas
for n in range(1, 51):
    # Construimos la URL de cada página usando el número de página
    url = f"https://books.toscrape.com/catalogue/page-{n}.html"
    print(f"\n--- Página {n}: {url} ---")

    # Hacemos la petición HTTP a la página
    response = requests.get(url)

    # Parseamos el HTML de la respuesta con BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Buscamos todos los artículos del catálogo; cada uno representa un libro
    libros = soup.find_all("article", class_="product_pod")

    for libro in libros:
        # La etiqueta <p class="star-rating X"> contiene la calificación
        estrellas = libro.find("p", class_="star-rating")

        # La segunda clase del atributo class es la valoración en texto
        # Ej: class="star-rating Four" → ["star-rating", "Four"]
        # "One", "Two", "Three", "Four" o "Five"
        rating = estrellas["class"][1]

        # Filtramos solo los libros con 4 o 5 estrellas
        if rating in ESTRELLAS_ALTAS:
            # El título está en el atributo title de la etiqueta <a> dentro del <h3>
            titulo = libro.find("h3").find("a")["title"]
            print(f"  [{rating}★] {titulo}")
