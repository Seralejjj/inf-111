while True:
    cad = input("¿Usted quiere continuar? ")
    cad = cad.lower()
    
    if cad == "s" or cad == "si" or cad == "bien" or cad == "seguro" or cad == "por qué no":
        print("Bien")
    elif cad == "n" or cad == "no":
        print("Finalizó")
        break
    else:
        print("Mala entrada")
