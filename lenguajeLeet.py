"""
 * -  Crea un programa que reciba del usuario una palabra o frase y la transforme a lenguaje leet, puedes revisar esta guía https://www.gamehouse.com/blog/leet-speak-cheat-sheet/

"""

"""
Este programa lo voy a manejar en Básico Leet e Intermedio Leet
"""

palabra = input("\n Ingrese la palabra a convertir: ")


basicoLeet = ""
intermedioLeet = ""
avanzadoLeet = ""

for letra in palabra:
    if letra == 'a' or letra == 'A':
        basicoLeet = (basicoLeet + '4')
        intermedioLeet = (intermedioLeet + '@')
        avanzadoLeet = (avanzadoLeet + " /\ ")

    elif letra == 'b' or letra == 'B':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + "|3")
        avanzadoLeet = (avanzadoLeet + "!3")

    elif letra == 'c' or letra == 'C':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + '[')
        avanzadoLeet = (avanzadoLeet + '{')


    elif letra == 'd' or letra == 'D':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + "|)")
        avanzadoLeet = (avanzadoLeet + "[)")


    elif letra == 'e' or letra == 'E':
        basicoLeet = (basicoLeet + '3')
        intermedioLeet = (intermedioLeet + '3')
        avanzadoLeet = (avanzadoLeet + '&')


    elif letra == 'f' or letra == 'F':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + "ph")
        avanzadoLeet = (avanzadoLeet + "|=_")


    elif letra == 'g' or letra == 'G':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + '6')
        avanzadoLeet = (avanzadoLeet + "{,")


    elif letra == 'h' or letra == 'H':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + '#')
        avanzadoLeet = (avanzadoLeet + "(-)")


    elif letra == 'i' or letra == 'I':
        basicoLeet = (basicoLeet + '1')
        intermedioLeet = (intermedioLeet + '1')
        avanzadoLeet = (avanzadoLeet + "][")


    elif letra == 'j' or letra == 'J':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + ']')
        avanzadoLeet = (avanzadoLeet + ",_|")


    elif letra == 'k' or letra == 'K':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + "|<")
        avanzadoLeet = (avanzadoLeet + "|{")


    elif letra == 'l' or letra == 'L':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + "|_")
        avanzadoLeet = (avanzadoLeet + "|")


    elif letra == 'm' or letra == 'M':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + "/\/\ ")
        avanzadoLeet = (avanzadoLeet + "]\/[")


    elif letra == 'n' or letra == 'N':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + "|\|")
        avanzadoLeet = (avanzadoLeet + "<\>")


    elif letra == 'ñ' or letra == 'Ñ':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + letra)
        avanzadoLeet = (avanzadoLeet + letra)


    elif letra == 'o' or letra == 'O':
        basicoLeet = (basicoLeet + '0')
        intermedioLeet = (intermedioLeet + '0')
        avanzadoLeet = (avanzadoLeet + "[]")


    elif letra == 'p' or letra == 'P':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + "|>")
        avanzadoLeet = (avanzadoLeet + "|°")


    elif letra == 'q' or letra == 'Q':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + "0_")
        avanzadoLeet = (avanzadoLeet + "<|")


    elif letra == 'r' or letra == 'R':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + "|2")
        avanzadoLeet = (avanzadoLeet + "|`")


    elif letra == 's' or letra == 'S':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + '5')
        avanzadoLeet = (avanzadoLeet + '$')


    elif letra == 't' or letra == 'T':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + '7')
        avanzadoLeet = (avanzadoLeet + "~|~")


    elif letra == 'u' or letra == 'U':
        basicoLeet = (basicoLeet + "(_)")
        intermedioLeet = (intermedioLeet + "(_)")
        avanzadoLeet = (avanzadoLeet + 'V')


    elif letra == 'v' or letra == 'V':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + "\/")
        avanzadoLeet = (avanzadoLeet + "\|")


    elif letra == 'w' or letra == 'W':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + "\/\/")
        avanzadoLeet = (avanzadoLeet + "\^/")


    elif letra == 'x' or letra == 'X':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + "><")
        avanzadoLeet = (avanzadoLeet + ")(")


    elif letra == 'y' or letra == 'Y':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + 'j')
        avanzadoLeet = (avanzadoLeet + "V/")


    elif letra == 'z' or letra == 'Z':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + '2')
        avanzadoLeet = (avanzadoLeet + "7_")

    elif letra == ' ':
        basicoLeet = (basicoLeet + letra)
        intermedioLeet = (intermedioLeet + letra)
        avanzadoLeet = (avanzadoLeet + letra)

print(f"\nLa palabra {palabra} convertida en sus tres dificultades: ")

print(f"\n En básico: {basicoLeet}")
print(f"\n En intermedio: {intermedioLeet}")
print(f"\n En avanzado: {avanzadoLeet}")
