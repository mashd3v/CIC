'''
    NOTA: para ejecutar el código es necesario tener instalado el paquete requests, si no lo tiene, favor de instalarlo desde la consola con:
        
        pip install requests
'''

#  Importaciones necesarias
import string
import re
import random
import time 
from os import system

# Importaciones de archivos python
import funciones_extra as func
import estructuras as est

class eliza:
    def __init__(self):
        self.keys = list(map(lambda x: re.compile(
            x[0], re.IGNORECASE), est.estructuras_generales))
        self.values = list(map(lambda x: x[1], est.estructuras_generales))

    '''
        traducir: toma un string, reemplaza cualquier palabra encontrada en dict.keys()
            con el correspondiente valor dict.values()
    '''

    def traducir(self, str, dict):
        palabras = str.lower().split()
        keys = dict.keys()

        for i in range(0, len(palabras)):
            if palabras[i] in keys:
                palabras[i] = dict[palabras[i]]

        return ' '.join(palabras)

    '''
        responder: toma un string, un conjunto de expresiones regulares y su correspondiente conjunto de listas;
            encuentra una pareja y regresa una respuesta random de la lista
    '''

    def responder(self, str):
        # Busqueda en internet
        if str.startswith('busca') | str.startswith('Busca'):        
            # Organizando el texto recibido
            tema = re.split(' ', str)
            tema.pop(0)
            tema = ' '.join(tema)    

            print(f'Eliza> Buscando {tema}, por favor espera...')
            return func.buscarTexto(tema)
        # Si no coincide con los parametros de busqueda en internet, entonces
        else:
            # encuentra una pareja entre las keys
            for i in range(0, len(self.keys)):
                match = self.keys[i].match(str)

                if match:
                    # encuentra una pareja con el correspondiente valor, elegido aleatoriamente de todas las opciones disponibles
                    respuesta = random.choice(self.values[i])
                    # tenemos una respuesta
                    pos = respuesta.find('%')

                    while pos > -1:
                        num = int(respuesta[pos+1:pos+2])
                        respuesta = respuesta[:pos] + self.traducir(
                            match.group(num), respuestas_espejo) + respuesta[pos + 2:]
                        pos = respuesta.find('%')

                    # arreglar la puntuación errónea al final
                    if respuesta[-2:] == '?.':
                        respuesta = respuesta[:-2] + '.'

                    if respuesta[-2:] == '??':
                        respuesta = respuesta[:-2] + '?'

                    return respuesta


'''
    respuestas_espejo: una diccionario usado para convertir cosas que tu dices a cosas que la computadora dirá.
        Ejemplo: Yo soy --> Tu eres
'''
respuestas_espejo = {
    "soy": "eres",
    "estaba": "estuviste",
    "yo": "tu",
    "me gustaria": "te gustaria",
    "he estado": "has estado",
    "lo hare": "lo haras",
    "mi": "tu",
    "eres": "soy",
    "has estado": "he estado",
    "lo haras": "lo hare",
    "tu": "mi",
    "tuyo": "mio",
    "tu": "yo",
    "mis": "tus",
    "tus": "mis",
    "estoy": "estas",
    "estas": "estoy",
}


def interfaz_de_comando():
    print('=' * 50)
    print('Bienvenido a Eliza')
    print('Habla con el asistente en Español.')
    print('Escribe "salir" para finalizar el programa')
    print('=' * 50)

    nombre = input('\nPara una experiencia personalizada, te pediré que escribas debajo tu nombre o como quieras ser llamado en nuestra plática\n')
    print('Comencemos...')
    time.sleep(1)
    system("cls")

    print(f'Eliza> Hola {nombre}, !bienvenido!')
    time.sleep(.8)
    print('Eliza> Mi nombre es Eliza y seré tu asistente por hoy.')
    time.sleep(.8)
    print('Eliza> Dime, ¿en qué te puedo ayudar el día de hoy?')

    s = ''

    eliza_bot = eliza()

    while s != 'salir':
        try:
            s = input(f'{nombre}> ')

            if s.lower() == 'bye':
                s = 'salir'

        except EOFError:
            s = 'salir'

        while s[-1] in '!.':
            s = s[:-1]

        print(f'Eliza> {eliza_bot.responder(s)}')


if __name__ == "__main__":
    system("cls")
    interfaz_de_comando()
