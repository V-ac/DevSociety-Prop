"""
* -  Crea un programa que reciba del usuario una frase y te diga si es o no palíndromo.
"""

palabra_usuario = input("\n Intruce la palabra o frase: ")

palabra_usuario_aux = palabra_usuario  #Declaré la variable para hacer una copia para que al momento de imprimir, el usuario pueda ver lo que introdujo.

palabra_usuario = palabra_usuario.lower() #Hacemos la palabra en minusculas para que no distinga en mayusculas y minusculas

palabra_usuario = palabra_usuario.replace(' ', '') #Aqui quito los espacios entre palabras. Esta opción es para cuando se introducen palabras palindromas y no dé error.

if(palabra_usuario == palabra_usuario[::-1]): #Aqui recorremos la palabra de final a principio y validamos si coinciden las palabras.
    print(f" '{palabra_usuario_aux}' es un palindromo")
else:
    print(f" '{palabra_usuario_aux}' no es un palindromo")