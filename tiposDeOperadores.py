"""
* - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 	*   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 	*   Ten en cuenta que cada lenguaje puede poseer unos diferentes
"""

#operacion de asignación

print("Asignación: ")
numero = 50
numero += 4
print(numero)

numero -=2
print(numero)

numero *=3
print(numero)

numero /= 2
print(numero)

numero %=3
print(numero)

numero **=2 #Exponete
print(numero)

numero //=3 #division sobre 3
print(numero)

print("---------------------------------------------")

print("Lógicos: ")
#Operadores lógicos
#and, or, not

altura = 840
altura2 = 620

comparacion = altura == altura2 and altura > altura2
print(comparacion)

comparacion2 = altura == altura2 or altura > altura2
print(comparacion2)

comparacion3 = not altura2 >= altura
print(comparacion3)


print("---------------------------------------------")

print("Binarios: ")
#Operadores binarios de comparación biterwise
binario = 0b1010
# &=, |=, ^=, >>=, <<=
binario &=0b1100
print(binario)

binario |=0b1010
print(binario)

binario ^=0b1010
print(binario)

binario >>=3
print(binario)

binario <<=4
print(binario)


print("---------------------------------------------")

print("Bits: ")
#Operadores biterwise

# &, |, ^, ~, <<, >>

tamaño = 60
tamaño2 = 30

print(bin(tamaño))
print(bin(tamaño2))


#Operador & (and)
resultado = tamaño & tamaño2
print(bin(resultado))

resultado2 = tamaño | tamaño2
print(bin(resultado2))

resultado3 = tamaño ^ tamaño2
print(bin(resultado3))

resultado4 = ~ tamaño #not
print(bin(resultado4))

resultado5 = tamaño << 2
print(bin(resultado5))

resultado6 = tamaño >> 2
print(bin(resultado6))


print("---------------------------------------------")

print("Comparación: ")
#Operadores comparacion
# ==, !=, <, >, <=, >=
edad = 23
edad2 = 25

iguales = edad == edad2
print(iguales)

diferente = edad != edad2
print(diferente)

menor = edad < edad2
print(menor)

mayor = edad > edad2
print(mayor)


menor_igual = edad <= edad2
print(menor_igual)
mayor_igual = edad >= edad2
print(mayor_igual)

print("---------------------------------------------")

print("Identidad: ")
#Operadores de identidad
#is, is not

temperatura = 30
temperatura2 = 27

comparacion_is = temperatura is temperatura2
print(comparacion_is)

comparacion_isnot = temperatura is not temperatura2
print(comparacion_isnot)


print("---------------------------------------------")

print("Pertenecia: ")
#Operadores de pertenencia
#in, not in

saludo = "Hola soy Vero"

pertenencia = "Hola" in saludo
print(pertenencia)

noPertenecia = "Mundo" not in saludo
print(noPertenecia)

noPertenecia2 = "soy" not in saludo
print(noPertenecia2)

