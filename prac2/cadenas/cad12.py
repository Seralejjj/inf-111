def es_completa(cadena1, cadena2):
    combinada = cadena1.lower() + cadena2.lower()
    letras_unicas = set(combinada)
    return len(letras_unicas) == 26

def main():
    print("Ingresa las cadenas (escribe 'fin' para terminar):")
    while True:
        a = input("Cadena a: ").strip()
        if a.lower() == 'fin':
            break
        b = input("Cadena b: ").strip()
        
        if es_completa(a, b):
            print("Completa")
        else:
            print("Incompleta")
        print() 

if __name__ == "__main__":
    main()