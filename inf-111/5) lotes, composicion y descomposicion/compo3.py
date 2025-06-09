x = int(input("x: "))

max_num = 0  
cuenta = 0

if x != 0:
    max_num = x
    cuenta = 1

    while True:
        x = int(input("x: "))
        if x == 0:
            break
        
        if x > max_num:
            max_num = x
            cuenta = 1
        elif x == max_num:
            cuenta += 1

print(f"El número mayor es {max_num}")
print(f"Y su cantidad de ocurrencias es {cuenta}")