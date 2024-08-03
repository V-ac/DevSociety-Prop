"""
Se pide hacer el algotimo de Distacia de levenshtein
En este ejemplo voy a usar las palabras "amor" y "amar"

"""

def distancia_Levenshtein(cadena1, cadena2):
    #Le sumamos 1 para ignorar el 0 del inicio
    long_cadena1 = len(cadena1) + 1
    long_cadena2 = len(cadena2) + 1

    #vamos a hacer y rellenar la matriz
    #Aqui llenamos la matriz con puros 0
    matriz = [[0 for n in range(long_cadena2)] for m in range(long_cadena1)]

#    print(matriz)

    #vamos a iniciar los valores de la primera fila y columna
    #con los numeros correspondientes al tamaño de la palabra
    for i in range(long_cadena1):
        matriz[i][0] = i
        #print(matriz[i][0])
    for j in range(long_cadena2):
        matriz[0][j] = j
        #print(matriz[0][j])


    for i in range(1, long_cadena1):
        for j in range (1, long_cadena2):
            #Valor para sacar el cadrito de sustitucón
            cost = 0 if cadena1[i - 1] == cadena2[j - 1] else 1
            matriz[i][j] = min(
                #Aqui se llenan los demás cuadritos
                matriz[i - 1][j] + 1, # Insersion
                matriz [i][j - 1] + 1, #Eliminación
                matriz[i - 1][j - 1] + cost #Sustitución
            )

    return matriz[long_cadena1 - 1][long_cadena2 - 1]


cadena1 = "amor"
cadena2 = "amar"
distancia = distancia_Levenshtein(cadena1, cadena2)

print(f"La distancia de Levenshtein entre '{cadena1}' y '{cadena2}' es: {distancia}")