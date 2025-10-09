while True:
    num = int(input())
    while num < 0:
        print("Número inválido!")
        num = int(input()) 
    else:
        resultado = 1
        for i in range(1, num+1):
            resultado *= i
        print(resultado)
    break