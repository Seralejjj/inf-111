def transformar_cadena(cadena):
    vocales = "aeiouAEIOU "
    resultado = ""
    for letra in cadena:
        if letra not in vocales:
            resultado += letra * 2
        else:
            resultado += letra
    return resultado

texto = input("Ingresa una cadena: ")
print(transformar_cadena(texto))