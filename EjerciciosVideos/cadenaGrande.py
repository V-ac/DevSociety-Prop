"""
Dado un arreglo de cadenas regresar otro arreglo que 
contenga solo las cadenas mas largas

Ejemplo:
para:
inputArray = ["aba", "as", "ad", "vcd", "aba"]

la salida debe ser:
allLongestStrings(inputArray) = ["aba", "vcd", "aba"]
"""



def ArregloLargo(inputArray):
    largoCadena = -1
    tamanoCadena = len(inputArray)
    resultado = []
    for i in range (0, tamanoCadena):
        #comparamos el tamaño de la cadena
        if(len(inputArray[i]) > largoCadena):
            largoCadena = len(inputArray[i]) #Aqui guarda 
            #el valor mas grande de la palabra mientras itera

    #Ahora vamos a guardar las palabras
    for i in range (0, tamanoCadena):
        #aqui indicamos que si la subcadena tiene el mismo
        #tamaño que la variable "largocadena" entonces
        #va a guardarla en el arreglo reusltado
        if (len(inputArray[i]) == largoCadena):
            resultado.append(inputArray[i])

    print(resultado)

arreglo = ["aba", "aa", "ad", "vcd", "aba"]
arreglo2 = ["aba", "apppaa", "ada", "vcd", "ababa"]
ArregloLargo(arreglo)
ArregloLargo(arreglo2)

