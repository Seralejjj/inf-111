def quien(cadena):
    for caracter in cadena:
        letra = caracter.lower()
        
        if letra != 'a' and letra != 'r' and letra != ' ':
            return "Han Solo"
    
    return "Chewbacca"

texto = input()
print(quien(texto))