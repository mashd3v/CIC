import math

# Numero n es primo
def primo():
    pass

# Determinar si es primo o no por ensayo de division
def primo_division(a):
    contador = 0

    for numero in range(1, a + 1):
        if a % numero == 0:
            # print(f'{a} / {numero} = {a / numero}')
            contador += 1

    if contador == 2:
        print(f'{a} es primo')
    else:
        print(f'{a}')


# Numeros primos en una serie numerica
def primos_serie(n):
    for numero in range(1, n + 1):
        primo_division(numero)


# Considerar el numero 5293


if __name__ == '__main__':

    print('1. Numero primo')
    print('2. Numero primo por division')
    print('3. Numeros primos de una serie')

    option = int(input('Opcion: '))
    numero = int(input('Numero: '))

    if option == 1:
        primo()
    elif option == 2:
        primo_division(numero)
    elif option == 3:
        primos_serie(numero)
    else: 
        print('Numero no valido')

    # Intento de switch
    # switcher = {
    #     1: primo(),
    #     2: primo_division(numero), 
    #     3: primos_serie(numero)
    # }.get(option, 'error') # Metodo get funciona solo si no tiene parametros la funcion
    


    