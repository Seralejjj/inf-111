def imprimir (cad):
    n = len(cad)
    for i in range(0,n,2):
        print(cad[i], end=" ")

cad = input("cadena: ")
imprimir(cad)