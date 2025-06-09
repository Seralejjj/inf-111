def cantidad (cad, x):
    n = len (cad)
    c = 0
    for i in range (n) :
        if cad [i] == x:
           c=c + 1
    return c

cad = input ("Cadena: ")
x = input ("Caracter: ")
cad = cad.upper ()
x = x.upper ()
c = cantidad (cad, x)
print ("Hay",c)
print ("Hay",cad.count(x))