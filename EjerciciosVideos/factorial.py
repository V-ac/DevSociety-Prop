"""
Primero de forma iterativa para sacra el factorial de un número

"""
def factorialIterativo(num):
    if num < 0: #Numero negativo
        print ("Factorial of negative num does no exit")
    elif num == 0: #Aqui se cubre el factorial de 0
        return 1
    else: #Aqui ya entran para las multiplicaciones
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        
        return fact
    
def factorial (num):
    return 1 if (num == 1 or num == 0) else num * factorial(num - 1)

#Asi funciona:
# 5 * factorial (5-1) y baja
# 4 * factorial (4-1) y baja
# 3 * factorial (3-1) y baja
# 2 * factorial (2 -1) y baja
# 1

#Al momento que llega a 1 retorna uno y ba subiendo para resolver las icognitas de la funcion factorial
# 5 * factorial (5-1) -> 5 * 24 = 120
# 4 * factorial (4-1) -> 4 * 6 = 24 y sube
# 3 * factorial (3-1) -> 3 * 2 = 6 y sube
# 2 * factorial (2 -1) -> 2 * 1 = 2 y sube
# 1  y sube



num = 5
#print("El factorial de ", num, " is ", factorialIterativo(num))
print("El factorial de ", num, " is ", factorial(num))
