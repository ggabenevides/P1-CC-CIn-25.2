# input inicial
num_convidados = int(input())

# criando listas
lista_convidados = []
lista_comidas = []
lista_valores = []

# recebendo inputs sobre os convidados e atualizando listas
for i in range(num_convidados):

    # recebendo nome do convidado e decidindo se ele vai entrar na festa ou não
    nome_convidado = str(input())
    if nome_convidado == "Maicon Kuster":
        print("você é convidado DE GUÊÊ???, sai da minha festa seu FOFOQUEIRO!!")
    else:
        lista_convidados.append(nome_convidado)
    comida_convidado = str(input())
    valor_comida = int(input())
    if comida_convidado in lista_comidas:
        print(f"Na Festa do Calabreso não pode comida Repetida SAI FORA {nome_convidado}")
        lista_convidados.remove(nome_convidado)
    lista_comidas.append(comida_convidado)
    lista_valores.append(valor_comida)
    if not (nome_convidado in lista_convidados):
        lista_comidas.pop(-1)
        lista_valores.pop(-1)

# ordenando listas de acordo com os criterios do calabreso  
# bubble sort - organizando as listas de valores, comidas e convidados a partir da lista de valores
n = len(lista_comidas)
for i in range(n):
    for j in range(0, n-i-1):
        if lista_valores[j] > lista_valores[j+1]:
            lista_valores[j], lista_valores[j+1] = lista_valores[j+1], lista_valores[j]
            lista_comidas[j], lista_comidas[j+1] = lista_comidas[j+1], lista_comidas[j]
            lista_convidados[j], lista_convidados[j+1] = lista_convidados[j+1], lista_convidados[j]

# avaliando repeticoes de valores
num_repeticoes = 0
idx_valor_repetido = []
ja_contou = []
for valor in lista_valores:
    if lista_valores.count(valor) > 1:
        num_repeticoes += 1
        if not lista_valores.index(valor) in ja_contou:
            idx_valor_repetido.append(lista_valores.index(valor))
            ja_contou.append(lista_valores.index(valor))
for i in range(1, num_repeticoes-1):
    idx_valor_repetido.append(i)

# bubble sort alfabetico p repeticoes de valor
if num_repeticoes > 0:    
    lista_idx = []
    for nome in lista_convidados:
        lista_idx.append(lista_convidados.index(nome))
    for indice in idx_valor_repetido:
            a = lista_idx[indice]
            b = lista_idx[indice+1]
            p1 = lista_convidados[a]
            p2 = lista_convidados[b]
            c1 = lista_comidas [a]
            c2 = lista_comidas [b]
            x = min(p1,p2)
            if p2 == x:
                lista_convidados.pop(b)
                lista_convidados.insert(a, p2)
                lista_comidas.pop(b)
                lista_comidas.insert(a, c2)

# o resultado final dessa lista será o candidato mais rico no índice 0, o mais liso no índice -1
# so vai ter convidado mais liso se tiver mais de um convidado
if len(lista_convidados) > 1:
    pessoa_mais_lisa = lista_convidados[0]
    pior_comida = lista_comidas[0]
if len(lista_convidados) >= 1:
    pessoa_mais_rica = lista_convidados[lista_valores.index(max(lista_valores))]
    melhor_comida = lista_comidas[lista_valores.index(max(lista_valores))]
# relatorio final
if len(lista_convidados) == 0:
    print("Nenhum convidado marcou presença na festa do calabreso!")
else:
    print(f"Obrigado para o(a) {pessoa_mais_rica} pelo(a) excelente {melhor_comida}")
    if len(lista_convidados) > 1:
        print(f"Rapaz, {pessoa_mais_lisa} trouxe o(a) {pior_comida} que estava altamente mais ou menos!!!")
    print("Lista de convidados do Calabreso")
    for nome in lista_convidados:
        print(f"{lista_convidados.index(nome)+1}- {nome}") 
