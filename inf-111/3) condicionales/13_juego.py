import random

usuario = int(input("Ingresa piedra (0), papel (1), o tijera (2): "))

# Entrada de la computadora
computadora = random.randint(0, 2)

if usuario == computadora:
    print("Empate")
elif (usuario == 0 and computadora == 2) or (usuario == 1 and computadora == 0) or (usuario == 2 and computadora == 1):
    print("Ganaste")
else:
    print("Perdiste")
