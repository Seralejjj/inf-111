def contar_letras(cadena):
    conteo = {}
    for letra in cadena:
        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1
    
    for letra in sorted(conteo):
        print(f"{letra}={conteo[letra]}")

palabra = input().strip()
contar_letras(palabra)