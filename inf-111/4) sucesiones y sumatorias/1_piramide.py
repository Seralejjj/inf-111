n = int(input("Ingrese el número de filas (1-10): "))  

for i in range(n):  
    print(" " * (n - i - 1), end="")  

    coeficiente = 1  
    for j in range(i + 1):  
        print(coeficiente, end=" ")  
        coeficiente = coeficiente * (i - j) // (j + 1) 
         
    print()