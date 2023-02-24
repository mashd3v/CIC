def invertir_lista(lista):
    lista_invertida = []
    for numero in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[numero])
    return lista_invertida

if __name__ == '__main__':

    lista = [2,1,6,10,30]
    print(f'Lista original: {lista}')
    print(f'Lista invertida: {invertir_lista(lista)}')
