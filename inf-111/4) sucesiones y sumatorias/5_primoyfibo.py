n = int(input("Ingrese el valor de n: "))

a = 0  
b = 1
contador_primos = 0
resultado = 0

while contador_primos < n:
    c = a + b 

    if c >= 2: 
        es_primo = True
        i = 2
        while i <= c // 2:  
            if c % i == 0:
                es_primo = False
                i = c 
            i += 1
        
        if es_primo:
            contador_primos += 1
            resultado = c
    
    a = b
    b = c  

print(resultado)