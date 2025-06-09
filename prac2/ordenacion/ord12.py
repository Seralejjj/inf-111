def leer_casos():
    return int(input())

def ordenar_cadena(cadena):

    cadena = list(cadena)
    for i in range(1, len(cadena)):
        key = cadena[i]
        j = i-1
        while j >= 0 and key < cadena[j]:
            cadena[j+1] = cadena[j]
            j -= 1
        cadena[j+1] = key
    return ''.join(cadena)

def buscar_ordenado(principal, subcadena):
    principal_ord = ordenar_cadena(principal)
    sub_ord = ordenar_cadena(subcadena)
    
    n = len(sub_ord)
    for i in range(len(principal_ord) - n + 1):
        if principal_ord[i:i+n] == sub_ord:
            return True
    return False

def main():
    casos = leer_casos()
    for _ in range(casos):
        principal = input().strip()
        sub = input().strip()

        normal = sub in principal

        ordenado = buscar_ordenado(principal, sub)
        print("si" if normal else "no")

main()