# Definicion de funciones base
def incremento(var):
    return var + 1


def decremento(var):
    return var - 1


def borrar(var):
    while (var != 0):
        var = decremento(var)
    return var


def asignacion(var1, var2, aux=0):
    aux = borrar(aux)
    var1 = borrar(var1)
    while (var2 != 0):
        aux = incremento(aux)
        var2 = decremento(var2)
    while (aux != 0):
        var1 = incremento(var1)
        var2 = incremento(var2)
        aux = decremento(aux)
    return var1, var2


def suma(var1, var2):
    z1 = asignacion(0, var1)


if __name__ == '__main__':
    print(incremento(2))
    print(decremento(2))
    print(borrar(2))
    print(asignacion(2, 4))
