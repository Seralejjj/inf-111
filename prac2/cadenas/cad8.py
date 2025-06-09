def encontrar_posicion():
    while True:
        entrada = input().strip()
        if entrada.lower() == 'end':
            break
        
        if len(entrada.split()) != 2:
            print(-1)
            continue
            
        cadena, caracter = entrada.split()
        posicion = -1
        
        for i in range(len(cadena)):
            if cadena[i] == caracter:
                posicion = i
                break
                
        print(posicion)

encontrar_posicion()