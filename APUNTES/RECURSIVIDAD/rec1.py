def imprime2(a, b):
    for i in range(b, a-1,-1):
        print (i, end =",")

def imprimeRec2(a, b):
    if a == b:
        print (a)
    else:
        print (b, end = ",")
    imprimeRec2(a, b-1)

def imprime(a, b):
    for i in range(a,b+1,1):
        print(i, end =",")

imprime2(1,5)
print ()
imprimeRec2(1,5)
print ()
imprime (1,5)