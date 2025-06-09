import math
def area (lado) :
    a = 5*lado ** 2/(4*math.tan (math.pi/5))
    return a

lado = int(input("lado: ") )
y = area (lado)
print ("ares: ", y)