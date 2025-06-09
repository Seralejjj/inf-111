while True:
    N = int(input("N (2-79) o 0: "))
    if N == 0: break
    
    sol = False
    
    for f in range(1234, 98765//N +1):
        a = f * N
        if a > 99999: continue
        
        def a5(n):
            s = ""
            for _ in range(5):
                s = str(n%10) + s
                n = n//10
            return s
        
        sa = a5(a)
        sf = a5(f)
        sc = sa + sf
        
        uv = [0]*10
        unico = True
        for c in sc:
            d = int(c)
            if uv[d]:
                unico = False
                break
            uv[d] = 1
        
        if unico and len(sc)==10:
            print(f"{sa} / {sf} = {N}")
            sol = True
    
    if not sol:
        print(f"No hay solución para {N}.")
    print()