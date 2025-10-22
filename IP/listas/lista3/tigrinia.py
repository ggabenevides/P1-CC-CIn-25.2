# definindo variaveis e listas
nivel_suspeita = 0
pessoas = []
eventos = []
inicio = []
fim = []
duracoes = []

# input inicial
print("Iniciando investigação... Zé Felipe está focado.")
numero_eventos = int(input())
for i in range(numero_eventos): # SIGLA_PERSONAGEM - EVENTO - HORA_INICIO - HORA_FIM
    elementos = []
    dados = input()
    elementos = dados.split(" - ")
    pessoas.append(elementos[0].strip())
    eventos.append(elementos[1].strip())
    horario_inicio = int(elementos[2].strip()[0:2])
    inicio.append(horario_inicio)
    horario_fim = int(elementos[3].strip()[0:2])
    fim.append(horario_fim)

# bubble sort das listas de acordo com hora de inicio (regra 0)
n = len(inicio)
for i in range(n):
    for j in range(0, n-i-1):
        if inicio[j] > inicio[j+1]:
            inicio[j], inicio[j+1] = inicio[j+1], inicio[j]
            fim[j], fim[j+1] = fim[j+1], fim[j]
            pessoas[j], pessoas[j+1] = pessoas[j+1], pessoas[j]
            eventos[j], eventos[j+1] = eventos[j+1], eventos[j]
        # comeca no mesmo horario, ordenar por hora de fim
        elif inicio[j] == inicio[j+1]:
            if fim[j] > fim[j+1]:
                inicio[j], inicio[j+1] = inicio[j+1], inicio[j]
                fim[j], fim[j+1] = fim[j+1], fim[j]
                pessoas[j], pessoas[j+1] = pessoas[j+1], pessoas[j]
                eventos[j], eventos[j+1] = eventos[j+1], eventos[j]

# regra definitiva 
if "VJM" in pessoas:
    nivel_suspeita = 100  
else: #regra definitiva nao foi acionada, analise normal
    # organizando nomes 
    for nome in pessoas:
        idx_nome = pessoas.index(nome)
        if nome == "V":
            pessoas[idx_nome] = "Virgínia"
        elif nome == "JM":
            pessoas[idx_nome] = "Jogador Misterioso"
        elif nome == "ZF":
            pessoas[idx_nome] = "Zé Felipe"  
    
    # relatorio inicial
    print()
    print("--- Linha do Tempo dos Eventos ---")
    for i in range(n):
        print(f"{inicio[i]}:00-{fim[i]}:00: {pessoas[i]} - {eventos[i]}")

    # avaliação dos eventos 
    num_alibis = 0
    num_encontros_suspeitos = 0
    for i in range(n):
        evento_atual = eventos[i]
        for j in range(n):
            evento_comparado = eventos[j]
            if i != j: # nao comparar a mesma pessoa
                # checando interseccao de horarios
                if  inicio[i] < fim[j] and inicio[i] < fim[j] and evento_atual == evento_comparado:
                    # eventos ocorreram ao mesmo tempo
                    if pessoas[i] == "Zé Felipe" and pessoas[j] == "Virgínia" or pessoas[i] == "Virgínia" and pessoas[j] == "Zé Felipe":
                        # alibi
                        num_alibis += 1
                    elif pessoas[i] == "Jogador Misterioso" and pessoas[j] == "Virgínia" or pessoas[i] == "Virgínia" and pessoas[j] == "Jogador Misterioso":
                        # encontro suspeito
                        num_encontros_suspeitos += 1

    # relatorio final 
    num_alibis = num_alibis // 2  # cada alibi contado duas vezes
    num_encontros_suspeitos = num_encontros_suspeitos // 2  # cada encontro contado duas vezes
    nivel_suspeita = (num_encontros_suspeitos * 35) - (num_alibis * 20)
    print()
    print("--- Resumo da Análise ---")
    print(f"Encontros Suspeitos: {num_encontros_suspeitos}")
    print(f"Álibis Confirmados: {num_alibis}")

# conclusao da analise 
if nivel_suspeita < 0:
    nivel_suspeita = 0

print()
if nivel_suspeita >= 100:
    print("TRAIÇÃO CONFIRMADA! Zé Felipe vai fazer uma música sobre isso.")
elif 70 <= nivel_suspeita < 100:
    print(f"Nível de Suspeita: {nivel_suspeita} - MUITO SUSPEITO! Zé Felipe vai ter uma conversa séria com a Virgínia.")
elif 30 <= nivel_suspeita < 70:
    print(f"Nível de Suspeita: {nivel_suspeita} - Hmmm, algo de estranho não está certo. Zé Felipe vai ficar de olho.")
else:
    print(f"Nível de Suspeita: {nivel_suspeita} - Não há motivo para preocupação. Zé Felipe pode respirar aliviado e voltar a brincar com a Maria Flor.")