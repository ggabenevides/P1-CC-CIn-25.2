quantidade_cedulas = [0,0,0,0,0,0]
combinacaoAtual = [0,0,0,0,0]
def calculo_possibilidades (combinacaoAtual,quantidade_cedulas,valor_restante, cedulas, combinacao_atual, cem:bool, cinquenta:bool, vinte:bool,dez:bool,cinco:bool):
    resultado_final = []
    indice_cedula = 0
    if valor_restante == 0:
        quantidade_cedulas[5] += 1
        for i in range(5):
            quantidade_cedulas[i] += combinacaoAtual[i]
        return [combinacao_atual] #existe uma solucao valida
    if valor_restante < 0 or indice_cedula == len(cedulas):
        return [] #todas as solucoes ja foram contadas ou nao existe nenhuma solucao
    # passo recursivo:
    else:
        if valor_restante >= 100 and not cem:
            indice_cedula = cedulas.index(100)
            combinacao_atual[indice_cedula] += 1
            combinacao_atual[0] +=1
            nova_combinacao = calculo_possibilidades(combinacaoAtual,quantidade_cedulas,valor_restante - 100, cedulas, combinacao_atual,cem,cinquenta,vinte,dez,cinco)
            combinacaoAtual[0] -=1
        cem = True
        if valor_restante >= 50 and not cinquenta:
            indice_cedula = cedulas.index(50)
            combinacao_atual[indice_cedula] += 1
            combinacaoAtual[1] +=1
            nova_combinacao = calculo_possibilidades(combinacaoAtual,quantidade_cedulas,valor_restante - 50, cedulas, combinacao_atual,cem,cinquenta,vinte,dez,cinco)
            combinacaoAtual[1] -= 1
        cinquenta = True
        if valor_restante >= 20 and not vinte:
            indice_cedula = cedulas.index(20)
            combinacao_atual[indice_cedula] += 1
            combinacaoAtual[2] +=1
            nova_combinacao = calculo_possibilidades(combinacaoAtual,quantidade_cedulas,valor_restante - 20, cedulas, combinacao_atual,cem,cinquenta,vinte,dez,cinco)
            combinacaoAtual[2] -= 1
        vinte = True
        if valor_restante >= 10 and not dez:
            indice_cedula = cedulas.index(10)
            combinacao_atual[indice_cedula] += 1
            combinacaoAtual[3] +=1
            nova_combinacao = calculo_possibilidades(combinacaoAtual,quantidade_cedulas,valor_restante - 10, cedulas, combinacao_atual,cem,cinquenta,vinte,dez,cinco)
            combinacaoAtual[3] -=1
        dez = True
        if valor_restante >= 5 and not cinco:
            indice_cedula = cedulas.index(5)
            combinacao_atual[indice_cedula] += 1
            combinacaoAtual[4] +=1
            nova_combinacao = calculo_possibilidades(combinacaoAtual,quantidade_cedulas,valor_restante - 5, cedulas, combinacao_atual,cem,cinquenta,vinte,dez,cinco)
            combinacaoAtual[4] -= 1
        cinco = True
        resultado_final += nova_combinacao
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
    todas_as_combinacao_atual = (calculo_possibilidades(combinacaoAtual,quantidade_cedulas,valor_total_da_conta, cedulas, combinacao_inicial,False,False,False,False,False))
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
if quantidade_cedulas[5] == 1:
    print("\nEssa foi fácil! Só existe 1 possibilidade de pagar essa conta.")
print(f"\nTotal de possibilidades: {quantidade_cedulas[5]}")
print("\nUso das notas:")
for i in range(5, 0, -1):
    print(f"R${cedulas[i-1]}: usada em {quantidade_cedulas[5-i]} combinações")
