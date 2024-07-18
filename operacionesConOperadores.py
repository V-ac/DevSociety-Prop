"""
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje:
	 *   Condicionales, iterativas, excepciones...
	 * - Debes hacer print por consola del resultado de todos los ejemplos.
"""

#Ejemplo 1. A dos edades se les hará una prueba para clasificarlas en menor de edad o mayos de edad y si son multiplo de 2.
print("Ejemplo 1: ")
edad1 = 27
edad2 = 17

print(edad1 % 2)
if(edad1 > 18):
    if(edad1 % 2 == 0): #El residuo tien que se 0 para que sea multiplo de un número
        
        print ("Es mayor y es multiplo de 2")
    else:
        print("Es mayor pero no es multiplo de 2")
else:
    print("No es mayor")

if(edad2 > 18):
    if(edad2 % 2 == 0):
        print ("Es mayor y es multiplo de 2")
    else:
        print("Es mayor pero no es multiplo de 2")
else:
    print("No es mayor")
    
print("--------------------------------------------------")
print("Ejemplo 2: ")


#Ejemplo 2. En un array de numeros se van a clasificar en mayores de 20 años o menores.

edades = [23,45,89,12,1,4,56,3,24,56,80,67,45,22,20,78,30]

for edad in edades:
    if(edad >= 20):
        print(f"La edad {edad} es mayor o igual a 20")
    else:
        print(f"La edad {edad} es menor a 20")



print("--------------------------------------------------")
print("Ejemplo 3: ")

#Ejemplo 3. En un array de articulos que se pueden encontra en la biblioteca, se van a clasificar en si pueden tener imagenes o no.
biblioteca = ["libro", "revista", "periorico", "comic", "novela", "cuento", "poesia", "cuaderno", "enciclopedia", "sopas de letras", "libro de colorear", "cuadro de pintura"] 
libros_imagenes = ["libro", "revista", "periorico", "comic", "cuento", "enciclopedia", "sopas de letras", "libro de colorear", "cuadro de pintura"] 

for item in biblioteca:
    siEsta = item in libros_imagenes
    if(siEsta == True):
        print(f"El item {item} si tiene imagenes")
    else:
        print(f"El item {item} no tiene imagenes")
    



print("--------------------------------------------------")
print("Ejemplo 4: ")

#Ejemplo 4. Mientras que un numero sea un multilo de 2 no hará nada hasta que sea diferente el multiplo


multiplos = [0, 2, 4, 6, 8, 10, 11, 12, 14, 16, 18, 20, 22, 24, 33, 44, 55, 66]
indice = 0

while (multiplos[indice] % 2) == 0:
    print(f"{multiplos[indice]} es multiplo de 2")
    indice+=1
    if(multiplos[indice] % 2 == 1):
        print(f"{multiplos[indice]} no es multiplo de 2")


print("--------------------------------------------------")
print("Ejemplo 5: ")
ano = 2024

try:
    if ano == 2021:
        print("Es el año 2021")
    else:
        print("No es el año 2021")
except Exception:
    print("Error")