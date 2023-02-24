# Base 2 
def base2(x):
    if x < 2:
        return [x]
    else:
        return [x % 2] + base2(x // 2)

def residuo(base, exponente, residuo1): 
    l = []
    a = base2(exponente)
    n = len(a)

    for i in range(n):
        c = b % residuo1 
        l = l + [c]
        b = c * c
    s = 1

    if 


