monto = float(input("Monto del préstamo: "))
anios = int(input("Cantidad de años: "))

print("\n| Tasa de interés | Pago mensual | Pago total |")
print("|---|---|---|")

tasa_inicial = 5.0
tasa_final = 8.0
incremento = 1.0 / 8.0  

tasa_actual = tasa_inicial
while tasa_actual <= tasa_final:

    tasa_mensual = (tasa_actual / 100) / 12
    meses = anios * 12

    pago_mensual = (monto * tasa_mensual) / (1 - (1 / (1 + tasa_mensual) ** meses))
    
    pago_total = pago_mensual * meses

    print(f"| {tasa_actual:.3f}% | {pago_mensual:.2f} | {pago_total:.2f} |")
    
    tasa_actual += incremento