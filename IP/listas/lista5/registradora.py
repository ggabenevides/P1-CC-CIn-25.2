def calculo_possibilidades (valor_restante, cedulas, combinacao_atual):
    resultado_final = []
    indice_cedula = 0
    if valor_restante == 0:
        resultado_final.append(combinacao_atual) #existe uma solucao valida
    if valor_restante < 0 or indice_cedula == len(cedulas):
        return [] #todas as solucoes ja foram contadas ou nao existe nenhuma solucao
    # passo recursivo:
    else:
        nova_combinacao = [0]*len(cedulas)
        if valor_restante >= 100:
            indice_cedula = cedulas.index(100)
            combinacao_atual[indice_cedula] += 1
            nova_combinacao = calculo_possibilidades(valor_restante - 100, cedulas, combinacao_atual)
        if valor_restante >= 50:
            indice_cedula = cedulas.index(50)
            combinacao_atual[indice_cedula] += 1
            nova_combinacao = calculo_possibilidades(valor_restante - 50, cedulas, combinacao_atual)
        if valor_restante >= 20:
            indice_cedula = cedulas.index(20)
            combinacao_atual[indice_cedula] += 1
            nova_combinacao = calculo_possibilidades(valor_restante - 20, cedulas, combinacao_atual)
        if valor_restante >= 10:
            indice_cedula = cedulas.index(10)
            combinacao_atual[indice_cedula] += 1
            nova_combinacao = calculo_possibilidades(valor_restante - 10, cedulas, combinacao_atual)
        if valor_restante >= 5:
            indice_cedula = cedulas.index(5)
            combinacao_atual[indice_cedula] += 1
            nova_combinacao = calculo_possibilidades(valor_restante - 5, cedulas, combinacao_atual)
        resultado_final.append(nova_combinacao)
        # lista de listas contendo todas as combinacoes possiveis
        return resultado_final

# programa
cedulas = [5, 10, 20, 50, 100]
resultado = []
combinacao_inicial = [0] * len(cedulas)
valor_total_da_conta = int(input())
print(f"Calculando possibilidades para o valor: {valor_total_da_conta}")

# calculando combinacao_atual possiveis
if valor_total_da_conta % 5 == 0:
    # o programa segue normalmente p a funcao recursiva
    todas_as_combinacao_atual = (calculo_possibilidades(valor_total_da_conta, cedulas, combinacao_inicial))
else:
    todas_as_combinacao_atual = []
    print("\nInfelizmente, não há como pagar essa conta com as notas disponíveis.")

#tratando dados obtidos p cpnseguir numero total de cedulas usadas
qtde_combinacao_atual = len(todas_as_combinacao_atual)
uso_total_cedulas = [0] * len(cedulas)
if qtde_combinacao_atual > 0:
    for i in range(qtde_combinacao_atual):
        for j in range(len(cedulas)):
            uso_total_cedulas[j] += todas_as_combinacao_atual[i][j]

# relatorio final
if qtde_combinacao_atual == 1:
    print("\nEssa foi fácil! Só existe 1 possibilidade de pagar essa conta.")
print(f"\nTotal de possibilidades: {qtde_combinacao_atual}")
print("\nUso das notas:")
for i in range(5, 0, -1):
    print(f"R${cedulas[i-1]}: usada em {uso_total_cedulas[i-1]} combinações")
