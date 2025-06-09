numero = input("Ingrese número: ")
resultado = ""

for digito in numero:
    if digito == '-':
        resultado += digito
    elif digito not in resultado:  
        resultado += digito

print("Resultado:", resultado)