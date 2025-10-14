# input inicial
num_convidados = int(input())

# criando listas
lista_convidados = []
lista_comidas = []
valores_comidas = []

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
    valores_comidas.append(valor_comida)
    if not (nome_convidado in lista_convidados):
        lista_comidas.remove(comida_convidado)
        valores_comidas.remove(valor_comida)
# ordenando listas de acordo com os criterios do calabreso
# primeiro, a lista de preços 
valores_ordenados = valores_comidas.copy()
valores_ordenadoss = valores_ordenados.sort(reverse=True)

# checando se valores se repetem
# FAZER ESSA PARTE
# se os valores se repetem, é considerada p mais liso/mais rico a primeira pessoa em ordem alfabetica
# na hora do print da lista de convidados, pessoas com valores repetidos sao ordenadas em ordem alfabetica

# convidado com comida mais barata e mais cara
if len(lista_convidados) > 1:
    menor_valor = min(valores_ordenados)
    index_menor_valor = valores_comidas.index(menor_valor)
    convidado_mais_liso = lista_convidados[index_menor_valor]
    pior_comida = lista_comidas[index_menor_valor]

if len(lista_convidados) >= 1:
    maior_valor = max(valores_ordenados)
    index_maior_valor = valores_comidas.index(maior_valor)
    convidado_mais_rico = lista_convidados[index_maior_valor]
    melhor_comida = lista_comidas[index_maior_valor]

# ordenando lista de convidados de acordo com a ordem de preço
convidados_ordenada = []
contagem= 0
for valor in valores_ordenados:
    convidados_ordenada.insert(contagem+1, lista_convidados[contagem])
    contagem += 1

# relatorio final
if len(lista_convidados) == 0:
    print("Nenhum convidado marcou presença na festa do calabreso!")
else:
    print(f"Obrigado para o(a) {convidado_mais_rico} pelo(a) excelente {melhor_comida}")
    if len(lista_convidados) > 1:
        print(f"Rapaz, {convidado_mais_liso} trouxe o(a) {pior_comida} que estava altamente mais ou menos!!!")
    print("Lista de convidados do Calabreso")
    for nome in convidados_ordenada:
        print(f"{convidados_ordenada.index(nome)+1}- {nome}")   