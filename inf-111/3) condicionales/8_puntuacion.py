import math

puntuacion = float(input("Ingrese la puntuación (entre 0.0 y 1.0): "))

if puntuacion < 0.0 or puntuacion > 1.0:
    print("Puntuación incorrecta")
elif puntuacion >= 0.9:
    print("Sobresaliente")
elif puntuacion >= 0.8:
    print("Aceptable")
elif puntuacion >= 0.7:
    print("Bien")
elif puntuacion >= 0.6:
    print("Suficiente")
else:
    print("Insuficiente")
