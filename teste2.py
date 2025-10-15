valores_repetidos = [] 
num_valores_repetidos = 0
lista_temp = []
ja_contou = []
for valor in valores_ordenados:
    if valores_ordenados.count(valor) > 1:
        lista_temp =[]
        num_valores_repetidos += 1
        if not(valor in ja_contou):
            for i in range(valores_ordenados.count(valor)):
                lista_temp.append(valor)
            valores_repetidos.append(lista_temp)
            ja_contou.append(valor)
    
valores_repetidoss = valores_repetidos.sort(reverse=True)