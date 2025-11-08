# variaveis 
hp_sam = 100
hp_neil = 100
matriz_espaco = []
movimentos_wasd = ["W", "A", "S", "D"]
armas = ["Espingarda", "Rifle", "Metralhadora"]
arma = "Rifle"
contagem_acoes = 0
hits_fogo = 0
dano_em_neil = 0
dano_neil = 0
sem_cura = False 
hits_em_neil = 0

# funcoes 
# função para calcular a distância de Chebyshev - d(x,y)=max(|x2−x1|,|y2−y1|)
def calculo_distancia(x1, y1, x2, y2):
    distancia_chebyschev = max(abs(x1 - x2), abs(y1 - y2))
    return distancia_chebyschev

# funcao deslocamento
def deslocamento_sam(matriz, movimento, matriz_base):
    posicao_sam_coluna = 0
    posicao_sam_linha = 0
    nova_posicao_sam_linha = 0
    nova_posicao_sam_coluna = 0
    for i in range(6):
        for j in range(6):
            if matriz[i][j] == "S":
                posicao_sam_linha = int(i)
                posicao_sam_coluna = int(j)
    if movimento == "W": 
        if posicao_sam_linha < 5:
            nova_posicao_sam_linha = posicao_sam_linha-1
            nova_posicao_sam_coluna = posicao_sam_coluna
    if movimento == "S":
        if posicao_sam_linha > 0:
            nova_posicao_sam_linha = posicao_sam_linha+1
            nova_posicao_sam_coluna = posicao_sam_coluna
    if movimento == "D":
        if posicao_sam_coluna < 5:
            nova_posicao_sam_linha = posicao_sam_linha
            nova_posicao_sam_coluna = posicao_sam_coluna+1
    if movimento == "A":
        if posicao_sam_coluna > 0:
            nova_posicao_sam_linha = posicao_sam_linha
            nova_posicao_sam_coluna = posicao_sam_coluna-1
    # atualizando matriz
    matriz[nova_posicao_sam_linha][nova_posicao_sam_coluna] = "S"
    if matriz_base[posicao_sam_linha][posicao_sam_coluna] == "P":
        matriz[posicao_sam_linha][posicao_sam_coluna] = "P"
    elif matriz_base[posicao_sam_linha][posicao_sam_coluna] == "F":
        matriz[posicao_sam_linha][posicao_sam_coluna] = "F"
    return matriz

# checar se sam esta num piso incediario
def check_dano_fogo(matriz, matriz_base):
    dano = False
    posicao_sam_coluna = 0
    posicao_sam_linha = 0
    for i in range(6):
        for j in range(6):
            if matriz[i][j] == "S":
                posicao_sam_linha = int(i)
                posicao_sam_coluna = int(j)
    if matriz_base[posicao_sam_linha][posicao_sam_coluna] == "F":
        dano = True
    return dano

# função para a ação de atirar de Sam
def atirar_sam(matriz, arma):
    posicao_sam_linha = 0
    posicao_sam_coluna = 0
    posicao_neil_coluna = 0
    posicao_neil_linha = 0
    # identificando posicoes na matriz
    for i in range(6): # linha
        for j in range(6): # coluna
            if matriz[i][j] == "S":
                posicao_sam_linha = int(i)
                posicao_sam_coluna = int(j)
            if matriz[i][j] == "N":
                posicao_neil_linha = int(i)
                posicao_neil_coluna = int(j)
    distancia = calculo_distancia(posicao_sam_linha, posicao_sam_coluna, posicao_neil_linha, posicao_neil_coluna)
    if arma == "Espingarda" and distancia <= 2:
        dano = 25
    elif arma == "Rifle":
        if distancia == 3:
            dano = 15
        else: 
            dano = 5
    elif arma == "Metralhadora" and distancia >= 4:
        dano = 15
    else: 
        dano = 0
    return dano

# função para a mecânica de teletransporte de Neil
def teletransporte_neil(matriz, matriz_base):
    lista_distancias = []
    lista_posicoes = []
    posicao_sam_linha = 0
    posicao_sam_coluna = 0
    posicao_teste_linha = 0
    posicao_teste_coluna = 0
    # identificando posicoes validas na matriz
    for i in range(6): # linha
        for j in range(6): # coluna
            if matriz[i][j] == "S":
                posicao_sam_linha = int(i)
                posicao_sam_coluna = int(j)
            if matriz[i][j] == "P" or matriz[i][j] == "F":
                posicao_teste_linha = int(i)
                posicao_teste_coluna = int(j)
            distancia_teste = calculo_distancia(posicao_teste_linha, posicao_teste_coluna, posicao_sam_linha, posicao_sam_coluna)
            lista_distancias.append(distancia_teste)
            lista_posicoes.append([posicao_teste_linha, posicao_teste_coluna])
    maior_distancia = max(lista_distancias)
    if lista_distancias.count(maior_distancia) > 1:
        maior_distancia_posicoes = []
        for i in range(len(lista_distancias)):
            if lista_distancias[i] == maior_distancia:
                maior_distancia_posicoes.append(lista_posicoes[i])
        posicao = maior_distancia_posicoes[-1]
    else:
        posicao = lista_posicoes[lista_distancias.index(maior_distancia)]
    nova_linha_neil = posicao[0]
    nova_coluna_neil = posicao[1]
    for i in range(6):
        for j in range(6):
            if matriz[i][j] == "N":
                posicao_neil_linha = int(i)
                posicao_neil_coluna = int(j)
    matriz[nova_linha_neil][nova_coluna_neil] = "N" # nova posicao de neil apos o teletransporte
    # ajustando posicao que neil estava anteriormente
    if matriz_base[posicao_neil_linha][posicao_neil_coluna] == "P": 
        matriz[posicao_neil_linha][posicao_neil_coluna] = "P"
    elif matriz_base[posicao_neil_linha][posicao_neil_coluna] == "F":
        matriz[posicao_neil_linha][posicao_neil_coluna] = "F"
    return matriz

#programa
# inicializacao
print("Sam: Mas que lugar é esse aqui?")
print("Dollman: WASD... Num exclusivo de PS5? Ah, fala sério!")
print()

# inputs matriz + transformando em lista correspondente a linha da matriz
for i in range(6):
    linha = input().split(" ", maxsplit=5)
    matriz_espaco.append(linha)
# matriz sem os personagens p comparacao
matriz_base = []
for i in range(6):
    linha_nova = []
    for j in range(6):
        if matriz_espaco[i][j] in ["S", "N"]:
            linha_nova.append("P")
        else:
            linha_nova.append(matriz_espaco[i][j])
    matriz_base.append(linha_nova)
# loop jogadas
while hp_neil>0 and hp_sam>0:
    entrada = input()
    contagem_acoes += 1
    dano_fogo = check_dano_fogo(matriz_espaco, matriz_base)
    if dano_fogo:
        hp_neil -= 5
    if entrada == "Atirar": # sam vai atirar 
        dano_em_neil = atirar_sam(matriz_espaco, arma) 
        hp_neil -= dano_em_neil
        if dano_em_neil>0:
            hits_em_neil += 1    
    if contagem_acoes % 4 == 0 and hp_neil>0: # neil vai atirar 
        print(">>> Você recebe um disparo de Neil! <<<")
        hits_fogo += 1
        hp_sam -= 15
        dano_neil += 15
    elif entrada in movimentos_wasd: #deslocamento na matriz
        matriz_espaco = deslocamento_sam(matriz_espaco, entrada, matriz_base)
    elif entrada in armas:
        arma = entrada
        print(f"Arma trocada para {arma}.")
    if hp_sam<=40 and not sem_cura:
        print("Dollman: A Fragile comeu todos os criptobiontes da DHV Magalhães... Se curar não é uma opção. Tome cuidado, Sam.")
        sem_cura = True
    if hits_em_neil == 3:
        hits_em_neil = 0
        matriz_espaco = teletransporte_neil(matriz_espaco, matriz_base)
        for i in range (6):
            for j in range(6):
                if j < 5:
                    print(f"{matriz_espaco[i][j]} ", end="")
                else: 
                    print(matriz_espaco[i][j])
else: 
    likes = 1000 - (dano_neil * 8) - (hits_fogo * 10)
    if hp_neil == 0:
        print()
        print("MISSÃO COMPLETA! - Investigue a Anomalia")
        print("========================================")
        print(f"Likes recebidos: 👍 {likes}")
    elif hp_sam == 0:
        print()
        print("MISSÃO FALHOU")
        print("==============")
        print("Sam foi derrotado.")
        print("[Sua alma vaga pela Emenda, buscando reencontrar seu corpo perdido...]")