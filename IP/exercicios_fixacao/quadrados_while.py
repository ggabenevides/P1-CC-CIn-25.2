i = 0
cubo = 0 
quadrado = 0

while i>= 0 and i <= 10:
    quadrado = i ** 2
    cubo = i ** 3
    if i == 0:
        print("Número  Quadrado  Cubo")
    print(f"{i}        {quadrado}        {cubo}")
    i += 1