def cantConsonantes(cad):
    n = len(cad)
    c = 0
    for i in range(n):
        a = ord(cad[i])
        if (97 <= a <= 122) and not (cad[i] in "aeiou"):
            c = c + 1
    return c

cad = input("Ingrese una cadena: ")
cad = cad.lower()
cc = cantConsonantes(cad)
print("El número de consonantes es", cc)
