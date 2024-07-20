"""
* -  Crea un programa que reciba del usuario un año y le responda si es o no bisiesto

"""

"""
Para identificar si un año es bisiesto, el año tiene que ser divisible entre 4. 
La operación consiste en agarrar las dos ultimas cifras y dividirlas entre 4, si es divisible entonces es bisiesto. Ejemplo 2008 -> 08/4 = 2. Entonces si es bisiesto
Cuando tenemos un año que termina en 00, como por ejemplo 2000 entonces se divide entre 400 y tiene que dar un valor entero la division. Ejemplo 2000 -> 2000/400 = 5. Si es bisiesto.
Ejemplo de un no bisiesto -> 2100/400 = 5.25. Este no es bisiestoi porque su división no da como resulado un entero
"""

#Es necesario importar las depencendias necesarias
from datetime import datetime

while True:
    ano_in = input("\n Ingrese el año a consultar: ")
    try:
        
        ano = datetime.strptime(ano_in, '%Y')

        #Variables auxiliares:
        ano_aux = ano.year #Solo agarra el año
        ano_string = str(ano_aux) #Lo convierte en string para manipular los ultimos dos digitos
        ano_dos_digitos = ano_string[2] + ano_string[3] #Solo contiene los dos números ultmos
        ano_entero = int(ano_dos_digitos)
        ano_completo_entero = int (ano_aux)
        ceros = 00


        #Operaciones para año 
        if(ano_entero != ceros):  #Aqui solo son los dos ultimos

            if(ano_entero%4 == 0):
                print(f"El año {ano_aux} es bisiesto.")
            else:
                print(f"El año {ano_aux} no es bisiesto.")

        else:
            if(ano_completo_entero%400 == 0): #Aqui se agarra la cifra del año
                
                print(f"El año {ano_aux} es bisiesto.")
            else:
                print(f"El año {ano_aux} no es bisiesto.")


    except ValueError:
        print("\n No ha ingresado un año correcto.")
    
    else:
        break
