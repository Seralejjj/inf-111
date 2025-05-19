import math

b = float(input("ingrese b: "))
x = float(input("ingrese x: "))

if x <=0:
    print ("debe ser positivo")
elif b <= 0 or b==1:
    print ("debe ser  positiva y diferente")
else:
     resultado = math.log(x) / math.log(b)
     print (resultado)