def contar(c, x):
    return 0 if not c else (1 if c[0]==x else 0) + contar(c[1:], x)

def prom(c, x):
    t = contar(c, x)
    l = len(c.replace(" ", ""))
    return round(t/l, 2) if l>0 else 0

texto = input().strip()
letra = input().strip()
print(f"{prom(texto, letra):.2f}")