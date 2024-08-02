"""
Haz depositado a tu cuenta bancaria una cantidad especifica de dinero (deposit).
Cada año tu saldo incrementa a la misma tasa de crecimeinto (rate)
Asumiendo que no haces depositos adicionales,
averigua cuanto tiempo le tomaria a tu saldo superar un umbral especifico (threshold)

Ejemplo:

Para:
deposit = 100
rate = 20
threshold = 170

la salida debe ser
depositProfet(deppsit, rate, threshold) = 3

Cada año la cantidad de dinero en tu cuenta crece 20%
asi que con los años el saldo queria de la siguiente manera:

 -- year 0: 100
 -- year 1: 120
 -- year 2: 144
 -- year 3: 172.8

 Por loq ue tomaria 3 años alcanzar el objetivo

"""


def depositProfit(deposit, rate, threshold): 
    cuentaAnos = 0
    tazaRendimiento = rate * 0.01; #Aqui salen el .2 osea 20%
    while (deposit < threshold):
        interes = deposit * tazaRendimiento #Aqui sacamos el interes que son el 20%
        deposit = deposit + interes #Aqui sumamos lo que tenemos en deposito más el interes.
        cuentaAnos += 1
    
    print(f"Los años que se necesitan para llegar son: {cuentaAnos}")



depositProfit(100,20,170)