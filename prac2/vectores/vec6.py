def repetir_elementos():
    numeros = input().split()
    
    repeticiones = int(input())
    
    resultado_final = []
    
    for num in numeros:

        numero_repetido = num * repeticiones
        
        resultado_final.append(numero_repetido)
    
    print(''.join(resultado_final))

repetir_elementos()