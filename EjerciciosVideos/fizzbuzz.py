"""
Imprimir en pantalla números del número 1 a N
Si el número es divisible entre 3 imprimimos Fizz
Si el número es divisible entre 5 imprimimos Buzz
Si el número es divisible entre 3 y 5 imprimimos FizzBuzz
"""


def fizzbuz(number):
    for i in range (1, number+1):
        print(i)

fizzbuz(10)