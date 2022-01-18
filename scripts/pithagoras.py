from math import sqrt

print("Bienvenido al calculador de pitágoras!")
i = input("Vas a introducir los dos catetos o un cateto y la hipotenusa? (catetos/hipotenusa): ")
if i.lower() == "catetos":
    c1 = input("Introduce el primer cateto: ")
    c2 = input("Introduce el segundo cateto: ")
    h = sqrt(pow(float(c1), 2) + pow(float(c2), 2))
    print("La hipotenusa del triángulo es", h)


elif i.lower() == "hipotenusa":
    h = input("Introduce la hipotenusa: ")
    c1 = input("Introduce un cateto: ")
    c2 = sqrt(abs(pow(float(c1), 2) - pow(float(h), 2)))
    print("El otro cateto es", c2)

else:
    print("???")