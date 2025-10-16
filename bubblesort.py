
lista_comidas = [3, 8, 4, 6, 5]
n = len(lista_comidas)
for i in range(n):
    for j in range(0, n-i-1):
        if lista_comidas[j] > lista_comidas[j+1]:
            lista_comidas[j], lista_comidas[j+1] = lista_comidas[j+1], lista_comidas[j]

print(lista_comidas)