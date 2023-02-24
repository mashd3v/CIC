import requests
from bs4 import BeautifulSoup

def buscarTexto(tema):
    # enlace para acceder al contenido de la Wikipedia
    response = requests.get(f'http://es.wikipedia.org/wiki/{tema}')

    # transformar el sitio web a texto plano
    soup = BeautifulSoup(response.text, features='html.parser')

    # obtener el texto por párrafos
    parrafos = soup.find_all('p')

    # obtener solo el primer parrafo
    texto = parrafos[0].text

    # imprimir el texto
    return texto