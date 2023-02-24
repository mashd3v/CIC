def horner(a, x):
    n = len(a)
    p = 0

    for i in range(n):
        k = n - 1 - i
        p = p * x + a[k]
    return p

def convb(n, b):
    if n < b:
        return [n]
    else: 
        return [n % b] + convb(n // b, b)

if __name__ == '__main__':
    a = int(input('Valor a convertir: '))
    b = int(input('Base a convertir: '))
    convb_res = convb(a, b)
    print(f'Convertir en base {b} el valor {a}:', convb_res)
    print('Horner: ', horner(convb_res, 2))