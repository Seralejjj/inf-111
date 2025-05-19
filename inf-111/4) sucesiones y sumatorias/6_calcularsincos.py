import math

x = float(input("Ingrese el valor de x: "))

decimales = 11
max_n = 10

print("n    sin({0:.1f})      cos({0:.1f})      e^{0:.1f}".format(x))
print("---  ------------    ------------    ------------")

sin_aprox = 0.0
cos_aprox = 0.0
exp_aprox = 0.0

for n in range(max_n + 1):

    fact_sin = math.factorial(2 * n + 1)
    fact_cos = math.factorial(2 * n)
    fact_exp = math.factorial(n)
    
    term_sin = ((-1) ** n) * (x ** (2 * n + 1)) / fact_sin
    term_cos = ((-1) ** n) * (x ** (2 * n)) / fact_cos
    term_exp = (x ** n) / fact_exp
    
    sin_aprox += term_sin
    cos_aprox += term_cos
    exp_aprox += term_exp
    
    print("{:02d}  {:.11f}  {:.11f}  {:.11f}".format(
        n, sin_aprox, cos_aprox, exp_aprox))