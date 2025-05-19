import math 

p = float(input("Ingrese p: "))
k = float(input("Ingrese k: "))

if k <= 2:
    subtotal = p * k
    t = subtotal  
elif k <= 5:
    subtotal = p * k
    t = subtotal * 0.90  
elif k <= 10:
    subtotal = p * k
    t = subtotal * 0.80  
else: 
    subtotal = p * k
    t = subtotal * 0.70 

print("Total a pagar:", t)
