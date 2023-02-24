'''
    Asignatura: Teoría de la Computación
    Objetivo principal del programa: Convertir de un pushdown automaton a su context free language correspondiente.
    Objetivo secundario: Determinar si una cadena de texto es admitida por el pushdown automaton a partir de sus reglas.
    Alumno: Miguel Angel Soto Hernandez
'''

####################################################################################################
########################### Procesamiento del PDA y asignación de reglas ###########################
####################################################################################################

# Esta función limpia y convierte a un arreglo de arreglos el PDA
def limpiar_pda(pda):
    pda_limpio = []
    for i in range(len(pda)):
        for j in range(len(pda[i])):
            sin_comas = pda[i][j].split(',')
            pda_limpio.append(sin_comas)

    punto_y_coma = []
    for i in range(len(pda_limpio)):
        bandera = 2
        for j in range(len(pda_limpio[i])):
            if len(pda_limpio[i][j]) > 1:
                punto_y_coma = pda_limpio[i][j].split(';')
        
        pda_limpio[i].pop(2)
        for j in range(len(punto_y_coma)):
            pda_limpio[i].insert(bandera, punto_y_coma[j])
            bandera += 1
                
    return pda_limpio


# Obtener alfabeto
def alfabeto_principal(pda):
    alfabeto = []

    for i in range(len(pda)):
        bandera = 1
        for j in range(len(pda[i])):
            alfabeto.append(pda[i][bandera])

    alfabeto = list(set(alfabeto))
    alfabeto.sort()

    return alfabeto


# Obtener alfabto obligatorio
def obligatorio(pda):
    alfabeto_obligatorio = []

    for i in range(len(pda)):
        if pda[i][0] != pda[i][3]:
            alfabeto_obligatorio.append(pda[i][1])
       

    alfabeto_obligatorio = list(set(alfabeto_obligatorio))
    alfabeto_obligatorio.sort()

    return alfabeto_obligatorio


# Obtener regla 1 del PDA 
def regla_1(pda):
    estado_inicial = pda[0][0]
    estado_final = pda[len(pda) - 1][3]
    regla1 = [estado_inicial, '/', estado_final]
    print('Regla 1:')
    print(f'S -> <{estado_inicial}, /, {estado_final}>')
    return regla1


# Obtener regla 2 del PDA 
def regla_2(pda):
    estados = []
    for i in range(len(pda)):
        bandera = 0
        for j in range(2):
            estados.append(pda[i][bandera])
            bandera = 3

    estados = list(set(estados))
    estados.sort()
    
    regla2 = []
    print('\nRegla 2')
    for i in range(len(estados)):
        regla2.append([estados[i], '/', estados[i]])
        print(f'<{regla2[i][0]}, {regla2[i][1]}, {regla2[i][2]}> -> /')

    return regla2, estados


# Obtener regla 3 y estados del PDA 
def regla_3(pda, estados):
    regla3 = []
    print('\nRegla 3')
    for i in range(len(pda)):
        if pda[i][2] != '/':
            for j in range(len(estados)):
                regla3.append([[pda[i][0], pda[i][1], estados[j]], [pda[i][2],[pda[i][3], '/', estados[j]]]])
                print(f'<{pda[i][0]}, {pda[i][1]}, {estados[j]}> -> {pda[i][2]}<{pda[i][3]}, /, {estados[j]}>')
    
    return regla3


# Obtener regla 4 del PDA 
def regla_4(pda, estados):
    regla4 = []
    w = []
    bandera = 2

    for i in range(len(pda)):
        w.append(pda[i][bandera])
        w = list(set(w))
        w.sort()
        
    print('\nRegla 4')
    for i in range(len(pda)):
        if pda[i][2] == '/':
            for j in range(len(w)):
                for k in range(len(estados)):
                    for l in range(len(estados)):
                        regla4.append([[pda[i][0], w[j], estados[k]], [pda[i][1], [pda[i][3], pda[i][4], estados[l]], [estados[l], w[j], estados[k]]]])
                        print(f'<{pda[i][0]}, {w[j]}, {estados[k]}> -> {pda[i][1]}<{pda[i][3]}, {pda[i][4]}, {estados[l]}><{estados[l]}, {w[j]}, {estados[k]}>')

    return regla4


####################################################################################################
############################ Determinación de aceptación de una cadena ############################
####################################################################################################
def procesar_cadena_texto(string):
    string = list(string)
    return string

def agregar_regla_2(string, opcion):
    opciones = []
    ultima_opcion = []
    
    for i in range(len(regla2)):
        ultima_opcion = string[len(string) - 1]
        if opcion == 1:
            opciones.append([ultima_opcion, regla2[i]])
        elif opcion == 2:
            opciones.append([ultima_opcion[0], regla2[i], ultima_opcion[1]])
            opciones.append([ultima_opcion[0], ultima_opcion[1], regla2[i]])
        else:
            break
    
    return opciones 


def coincidencia_regla_3_4(opciones, regla):
    coincidencia = []
    opcion_correcta = []
    validacion = False

    for i in range(len(opciones)):
        if validacion == False:
            for j in range(len(regla)):
                if opciones[i] == regla[j][1]:
                    coincidencia = regla[j][0]
                    opcion_correcta = regla[j][1]
                    validacion = True                
                    break
                else:
                    validacion = False
        else:
            break

    return coincidencia, opcion_correcta, validacion 


def obtener_cadena_actualizada(string, valor_a_insertar):
    string.pop()
    string.append([string[len(string) - 1], valor_a_insertar])
    string.pop(len(string) - 2)
    print(f'Ahora tenemos una nueva cadena: {string}\n')
    return string


def imprimir_coincidencia(opcion_correcta, arreglo_coincidencia):
    if arreglo_coincidencia:
        print(f'Hubo coincidencia, ahora sustituiremos nuestra opcion que coincidió, en este caso {opcion_correcta} y la sustituimos por {arreglo_coincidencia}\n')
    else:
        print('No se encontro coincidencia')


def imprimir_proceso_regla_3_4(string):
    print(f'Con esta nueva cadena {string[len(string) - 1]} compararemos si hay alguna coincidencia con la regla 3')
    coincidencia_r3, opcion_correcta, validacion = coincidencia_regla_3_4(string[len(string) - 1], regla3)
    print(f'Coincidencia en regla 3: {validacion}')
    print('Dado que no hubo coincidencia, ahora agregaremos otro lambda de la regla 2, y buscaremos una coincidencia nuevamente con la regla 4\n')

    if validacion == False:
        opciones1 = agregar_regla_2(string, 2)
        print(f'Ahora las opciones a comparar con la regla 4 son las siguientes: {opciones1}')
        nueva_coincidencia_r4, opcion_correcta1, validacion1 = coincidencia_regla_3_4(opciones1, regla4)
        imprimir_coincidencia(opcion_correcta1, nueva_coincidencia_r4)
    else:
        nueva_coincidencia_r4 = coincidencia_r3
        validacion1 = validacion
        
    return string, nueva_coincidencia_r4, validacion1



def procesamiento_principal(string):
    alfabeto_cadena = list(set(string))
    alfabeto_cadena.sort()

    if len(string) < 2:
        print('Error: Cadena no aceptada por la gramática')
    elif alfabeto_cadena == alfabeto or alfabeto_cadena == alfabeto_obligatorio:
        print(f'\nCadena ingresada: {string}')
        print(f'Tomamos el ultimo valor, en este caso "{string[len(string) - 1]}" y probamos con todas los valores de la regla 2\n')

        opciones = agregar_regla_2(string, 1)
        print(f'Opciones con nuestra regla 2: {opciones}\n')

        print('Ahora comparamos nuestras opciones con nuetras regla 3')
        coincidencia_r3, opcion_correcta, validacion = coincidencia_regla_3_4(opciones, regla3)
        imprimir_coincidencia(opcion_correcta, coincidencia_r3)

        string = obtener_cadena_actualizada(string, coincidencia_r3)

        for i in range(len(string) - 1):
            string, nueva_coincidencia_r4, validacion1 = imprimir_proceso_regla_3_4(string)
            string = obtener_cadena_actualizada(string, nueva_coincidencia_r4)
            
            if validacion1 == False:
                print('Error: La cadena no es aceptada')
                break

        if len(string) == 1:
            string, nueva_coincidencia_r4, validacion1 = imprimir_proceso_regla_3_4(string)

            if nueva_coincidencia_r4 == regla1:
                print(f'El regla final {nueva_coincidencia_r4} es igual a la regla 1 {regla1}, por lo tanto la cadena es aceptada por el PDA')
            else:
                print(f'El regla final {nueva_coincidencia_r4} es diferente a la regla 1 {regla1}, por lo tanto la cadena NO es aceptada por el PDA')
    else:
        print('Error: Error: La cadena no es aceptada')


####################################################################################################
################################# Ejecución principal del programa #################################
####################################################################################################
if __name__ == '__main__':
    import sys

    pda = []
    argumentos = sys.argv

    if '.txt' in argumentos[1]:
        with open(argumentos[1]) as pushdown:
            for lineas in pushdown:
                pda.append(lineas.split())
        
        if len(argumentos) >= 2:
            # Limpieza del PDA y obtención de los alfabetos ndecesarios para el procesamiento
            pda_limpio = limpiar_pda(pda)
            alfabeto = alfabeto_principal(pda_limpio)
            alfabeto_obligatorio = obligatorio(pda_limpio)

            # Obtención de reglas del PDA
            regla1 = regla_1(pda_limpio)
            regla2, estados = regla_2(pda_limpio)
            regla3 = regla_3(pda_limpio, estados)
            regla4 = regla_4(pda_limpio, estados)
        
        if len(argumentos) == 3:
            string = argumentos[2]
            string = procesar_cadena_texto(string)
            aceptado = procesamiento_principal(string)
    else: 
        print('Por favor verifique los parámetros de entrada')
        print('Es necesario ejecutar el programa desde línea de comandos mandando como parámetros:')
        print('- Un archivo .txt el cual contenga el PDA (tiene que estar en el mismo directorio que el programa)')
        print('- Cadena a revisar\n')
        print('Ejemplo:')
        print('python pda_a_cfg.py pda.txt cbbc')
    



