import time

correctas = 0
total_preguntas = 5

tiempo_inicial = time.time()

for i in range(1, total_preguntas + 1):

    num1 = (i * 3) % 15 + 1
    num2 = (i * 7) % 15 + 1
    
    respuesta = int(input(f"¿Cuánto es {num1} + {num2}? "))
    
    if respuesta == num1 + num2:
        print("Su respuesta es correcta!")
        correctas += 1
    else:
        print(f"Su respuesta es incorrecta.\n{num1} + {num2} es {num1 + num2}")

tiempo_final = time.time()
tiempo_total = int(tiempo_final - tiempo_inicial)  

print(f"\nLa cantidad de respuestas correctas es {correctas}")
print(f"El tiempo de la prueba fue de {tiempo_total} segundos")