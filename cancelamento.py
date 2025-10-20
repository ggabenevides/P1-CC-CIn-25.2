qtde_famosos = int(input())

lista_nomes = []
lista_seguidores = []
lista_acontecimentos = []

# recebendo dados e guardando eles em listas
for i in range(qtde_famosos):
    elementos = []
    dados = input()
    elementos = dados.split(' - ')
    lista_nomes.append(elementos[0])
    lista_seguidores.append(int(elementos[1]))
for i in range(qtde_famosos):
    acontecimento = int(input())
    lista_acontecimentos.append(acontecimento)

print("--- Simulador de Cancelamento ---")
print()

for nome in lista_nomes:
    print(f"A subcelebridade da vez é: {nome}")
    if lista_acontecimentos[lista_nomes.index(nome)] == 1:
        print(f"{nome} perdeu 10% dos seguidores!")
        lista_seguidores[lista_nomes.index(nome)] -= int(lista_seguidores[lista_nomes.index(nome)])*0.1
    elif lista_acontecimentos[lista_nomes.index(nome)] == 2:
        print(f"{nome} ganhou 5% de seguidores!")
        lista_seguidores[lista_nomes.index(nome)] += int(lista_seguidores[lista_nomes.index(nome)])*0.05      
    elif lista_acontecimentos[lista_nomes.index(nome)] == 3:
        print(f"{nome} perdeu 15% dos seguidores!")
        lista_seguidores[lista_nomes.index(nome)] -= int(lista_seguidores[lista_nomes.index(nome)])*0.15
    else:
        print("Nenhum evento relevante. Seguidores continuam os mesmos.")

# bubble sort das listas de acordo com o numero de seguidores, em ordem decrescente
n = len(lista_seguidores)
for i in range(n):
    for j in range(0, n-i-1):
        if lista_seguidores[j] < lista_seguidores[j+1]:
            lista_seguidores[j], lista_seguidores[j+1] = lista_seguidores[j+1], lista_seguidores[j]
            lista_nomes[j], lista_nomes[j+1] = lista_nomes[j+1], lista_nomes[j]

print()
print("--- RANKING FINAL DE SEGUIDORES ---")
if qtde_famosos >= 3:
    print(f"1º Lugar: {lista_nomes[0]} com {int(lista_seguidores[0])} seguidores.")
    print(f"2º Lugar: {lista_nomes[1]} com {int(lista_seguidores[1])} seguidores.")
    print(f"3º Lugar: {lista_nomes[2]} com {int(lista_seguidores[2])} seguidores.")
elif qtde_famosos == 2:
    print(f"1º Lugar: {lista_nomes[0]} com {int(lista_seguidores[0])} seguidores.")
    print(f"2º Lugar: {lista_nomes[1]} com {int(lista_seguidores[1])} seguidores.")
elif qtde_famosos == 1:
    print(f"1º Lugar: {lista_nomes[0]} com {int(lista_seguidores[0])} seguidores.")