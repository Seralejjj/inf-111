q = int(input("Can:"))
i = 0
while i < q:
    n = int(input("Num:"))
    p = 0
    while p < 1000:
        c = n
        r = 0
        while c > 0:
            d = c % 10
            r = r * 10 + d
            c = c // 10
        if n == r:
            break
        n += r
        p += 1
    i += 1 
    print("P:", p)
    print("R:", n)
    print()