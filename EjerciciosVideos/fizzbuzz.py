"""
Imprimir en pantalla números del número 1 a N
Si el número es divisible entre 3 imprimimos Fizz
Si el número es divisible entre 5 imprimimos Buzz
Si el número es divisible entre 3 y 5 imprimimos FizzBuzz
"""

#Esta es la primera forma que se puede solucionar
def fizzbuz(number):
    for i in range (1, number+1):
        #Va primero esta condición para que no se descarte
        #desde un principio cuando cumpla la condición.
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

#Como segunda solución:
def fizzbuzz2(number):
    for i in range (1, number+1):
        #Se va a imprimer Fizz si es divisible entre 3
        fizz = "Fizz" if i % 3 == 0 else ""
        #Se va a imprimir Buzz si es divisible entre 5
        buzz = "Buzz" if i % 5 == 0 else ""
        #En este caso, si cumple las 2, entonces se va a
        #imrimir "FizzBuzz"
        print(f"{fizz}{buzz}" or i)


fizzbuzz2(30)