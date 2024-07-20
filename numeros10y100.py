"""
* Crea un programa que imprima por consola todos los números comprendidos entre 10 y 100 (incluidos), pares, y que no son ni el 66 ni múltiplos de 3.

"""

# TODO Vamos a usar un condicional para evaluar si los numeros son exclusivos pares y que no son multiplos de 3.

numero = 10 #Esta variable va ir incrementando en el ciclo.

while(numero <= 100):
    if(numero%2 == 0 and numero%3 == 1): 
        print(f"{numero}")
    numero+=1 #va a ir aumentando

"""
Explicación: como los pares son multiplos de 2, al momento de sacar modulo de un número, en este caso con el número 2. El resultado solo oscila entre 0 y 1, dado que 0 indica que el residuo de la operación
es 0, en este caso indica que "n" numero se puede dividir entre el 2 y que no genera residuo destinto al 0.
Ya teniendo los numeros que son pares, ahora se tenía que separar los pares que son multiplos de 3 como lo son el 12, 18, 24 ....
En este caso, si el modulo nos daba el 0, nos muestra los pares que son multiplos de 3, así que la declaración es inversa para que solo se muestren los números pares no multiplos de 3 como el numero 66.

Estas dos condicionales se declaran con un and para que sólo muestre los números pares no multplos de 3.

"""