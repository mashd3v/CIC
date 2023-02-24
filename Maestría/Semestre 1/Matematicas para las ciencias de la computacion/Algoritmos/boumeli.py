import math

def fc(a, r, n):
    if n == 1:
        return r / (2 * a)
    else:
        return r / (2 * a + fc(a, r, n-1))

def fracc(a, r, n):
    return a + fc(a, r, n)


if __name__ == '__main__':
    a= int(input('a = ' ))
    r= int(input('r = ' ))
    n= int(input('n = ' ))

    print(f'Raiz con sqrt: {math.sqrt((a**2)+r)}')
    print(f'Funcion: {fracc(a,r,n)}')