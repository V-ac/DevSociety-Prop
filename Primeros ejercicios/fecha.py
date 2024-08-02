"""
* -  Crea un programa en el que el usuario ingrese la fecha y obtenga cuantos días faltan para día de muertos y navidad

"""
#Es necesario importar las depencendias necesarias
from datetime import datetime

#Declaramos los días que vamos a usar
DiaMuertos = datetime(2024, 11, 2)
Navidad = datetime(2024, 12, 25)

while True:
    fecha_introducida = input('\n Ingrese fecha "aaaa/mm/dd"...: ')  #Se le pide la fecha al usuario
    try: #vamos a validar la fecha. La misma biblioteca verifica que este correcta la fecha que se introdujo. 
        fecha = datetime.strptime(fecha_introducida, '%Y/%m/%d')

        #Restamos las fechas
        fecha_DiaMuertos = DiaMuertos - fecha 
        fecha_Navidad = Navidad - fecha

        #Mostramos los días que faltan para los días solicitados para el año 2024
        print(f"\n{fecha_DiaMuertos.days} dias para el Día de Muerto del 2024")
        print(f"{fecha_Navidad.days} dias para Navidad del 2024")

    except ValueError:
        print("\n No ha ingresado una fecha correcta...")
    else:
        break   