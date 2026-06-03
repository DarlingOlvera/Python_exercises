from bs4 import BeautifulSoup
import requests


resultado = requests.get('https://fede-garay.vercel.app/')

# Convierte el objeto string devuelto en un objeto de html, en este caso con motor de conversion lxml
soup = BeautifulSoup(resultado.text, 'lxml')

for t in soup.select('#videos h3'):
    print(t.get_text())

for label in soup.select('#videos a'):
    print(label['href'])

imagen = soup.select('img')[0]

url_imagen = 'https://fede-garay.vercel.app/' + imagen['src']

image_response = requests.get(url_imagen).content

# Descargar la imagen recuperada en el pc
foto = open('mi_foto.png', 'wb')
foto.write(image_response)
foto.close()
