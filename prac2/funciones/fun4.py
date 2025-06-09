def codigoxd():
    N, X = input().split()
    X = int(X)
    k = int(input())
    
    cont = 0
    for d in N:
        if int(d) == X:
            cont += 1
    print(cont)
    
    nuevo_num = ""
    for d in N:
        nuevo_num += str(k) if int(d) == X else d
    print(nuevo_num)
    
    print(''.join(sorted(nuevo_num)))

codigoxd()