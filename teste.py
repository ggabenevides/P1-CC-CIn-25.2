valores_ordenados = [20, 20, 10, 10, 4]
convidados_ordenados = ['ze felipe', 'virginia', 'jorge ben', 'kleber bambam', 'calabreso']


# checando se valores se repetem e criando uma lista p eles
valores_repetidos = [] 
num_valores_repetidos = 0
ja_contou = []
for valor in valores_ordenados:
    if valores_ordenados.count(valor) > 1:
        if not(valor in ja_contou):
            valores_repetidos.append(valor)
            ja_contou.append(valor)
            num_valores_repetidos += 1

#organizando a lista dos valores repetidos na mesma ordem que as outras listas
valores_repetidoss = valores_repetidos.sort(reverse=True)

# se os valores se repetem, é considerada p mais liso/mais rico a primeira pessoa em ordem alfabetica
lista_temp = []
idx = 0
if num_valores_repetidos > 0:
    for valor in valores_ordenados:
        if valor in valores_repetidos:
            idx = valores_ordenados.index(valor)
            for i in range (num_valores_repetidos):
                if convidados_ordenados[idx] in lista_temp:
                    idx += 1
                lista_temp.append(convidados_ordenados[idx])
            lista_temp.sort()
    pessoa_mais_rica = convidados_ordenados[0]
    pessoa_mais_lisa = lista_temp[2]

# o resultado final dessa lista será o candidato mais rico no índice 0, o mais liso no índice 1
print(lista_temp)