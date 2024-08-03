"""
Dado un arreglo a que contiene solo números en el rango de 1 a una longitud,
encuentre el primer número duplicado para el que la segunda aparción tiene el índice mínimo.
En otras palabras, si hay más de 1 número duplicado, devuelva el número para el que la segunda
aparación tiene un índice más pequeño que la segunda aparición del otro número.
Si no hay tales elementos, devuelve -1.

Ejemplo:
a = [2, 1, 3, 5, 3, 2]

La salida debe ser:
firsDuplicate(a) = 3

Hay dos duplicados: los números 2 y 3.
La segunda aparición de 3 tiene un índice más pequeño que
la segunda aparición de 2, por lo que la respuesta es 3.

Para a = [2, 2], la salida debe ser firsDuplicate(a) = 2
Para a = [2, 4, 3, 5, 1] la salida de firstDuplicate(a) = -1

"""

def firstDuplicate(a):
    """Vamos hacer un diccionario para hacer un tipo de check list
    Se va a ir agregando al diccionario el número clave que se acaba
    de visitar y como valor el true 
    De tal forma que al momento que no se encuentre en la lista lo va agregar
    si se encuentra duplicado ya no lo agrega y manda el indice del númeor duplicado
    """
    dic = {}
    result = -1

    for i in range (0, len(a)):
        element = a[i]
        #print(element)
        if element not in dic.keys():
            #print(element)
            dic[element] = True
        else:
            #print(element)
            #Si ya lo encontró quiebra el for y el elemento se guarda en result
            result = element
            break
    return result

result1 = firstDuplicate([2,1,3,5,3,2])
print(f"Primer result: {result1}")

result2 = firstDuplicate([2,2])
print(f"Segundo result: {result2}")

result3 = firstDuplicate([2,4,3, 5, 1])
print(f"Tercer result: {result3}")













