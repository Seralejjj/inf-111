def leeVector (V,n) :
    for i in range(n): # i:0 .. n-1
        V[i] = int (input ("x: "))

def maximo (V, n) :
    aux = -1
    for i in range(n): # i:0 .. n-1
        if V[i] > aux:
            aux = V[i]
    return aux

n = int (input ("n: "))
A = [0]*n
leeVector (A, n)
max = maximo (A, n)
print ("Maximo =", max)