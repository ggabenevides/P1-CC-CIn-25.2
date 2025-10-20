print("RECEBA! É hoje que eu me torno o melhor dos melhores.")
num_treinos = int(input())
habilidade_luva_inicial = int(input())
sequencia_treinos_raw = str(input())
elementos_treino = sequencia_treinos_raw.split('-')

habilidade_luva = habilidade_luva_inicial
partida_atual = 1
pontos = 0  

# prints iniciais 
if 0 <= habilidade_luva <= 5:
    print("A gente tem que começar de algum lugar, né? RECEBA!")
elif 6 <= habilidade_luva <= 16:
    print("Não tem jeito, vou ser o melhor do mundo!")
elif habilidade_luva > 16: 
    print("O Pai tá estourado! RECEBA!")

#calculando meta de habilidade 
meta = (100 - habilidade_luva) / num_treinos 
print(f"Meta por Partida: {meta}")

idx_tipo_lista = []

while habilidade_luva <= 100 and partida_atual <= num_treinos:

    # indices para buscar o tipo e o goleiro na lista de elementos_treino
    if partida_atual == 1:
        idx_tipo = 0
        idx_tipo_lista.append(idx_tipo)
    else: 
        idx_tipo = idx_tipo_lista[partida_atual-2] + 2
        idx_tipo_lista.append(idx_tipo)

    idx_goleiro = (partida_atual*2)-1
    
    tipo_partida = ""
    goleiro = ""
    habilidade_goleiro = 0
    pontos = 0
    
    # determinando treino
    if idx_tipo < len(elementos_treino):
        tipo_partida = elementos_treino[idx_tipo]
    if idx_goleiro < len(elementos_treino):
        goleiro = elementos_treino[idx_goleiro]

    if goleiro not in ["Gabriel Vasconcelos", "Neymar Jr", "Sérgio Soares", "IShowSpeed", "Rokenedy"]:
        habilidade_goleiro = int(input())

    # inputs da partida        
    matriz_input = input()
    matriz = eval(matriz_input)

    x = int(input())
    y = int(input())

    # relatorio da partida
    print(f"TIPO DE PARTIDA: {tipo_partida}")
    print(f"Nome do Goleiro: {goleiro}")

    # resultados de acordo com o goleiro
    if goleiro == "Rokenedy": # nunca vai ser gol 
        print("Aí não dá, impossível de fazer gol no maior do mundo.")
        print("A jornada ainda não acabou!")
    if goleiro == "IShowSpeed": # n tem nenhuma condicao especial
        print("REBECA? Is that you?")
        print("Ispidi mai friand, recieve!")
        if matriz[x][y] == 1:
            print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")
            pontos += meta*1.5
        else:
            print("A jornada ainda não acabou!")
    elif goleiro == "Gabriel Vasconcelos": # n tem nenhuma condicao especial
        print("HAHAHA! Eu pedi um desafio, não uma barra sem goleiro…")
        if matriz[x][y] == 1:
            print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")
            pontos += meta*2
        else:
            print("A jornada ainda não acabou!")
    elif goleiro == "Sérgio Soares": # so nao defende se for penalti
        print("DALE DALE, PROFESSOR! Quero ver se esse tal de Python é bom mesmo…")
        if tipo_partida == "Batida de Pênalti":
            if matriz[x][y] == 1:
                print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")
                pontos += meta  
            else:
                print("A jornada ainda não acabou!")
        else :  
            print("A jornada ainda não acabou!")
    elif goleiro == "Neymar Jr":
        print("Ele nem sabe agarrar! A arma dele é a sua fragilidade…")
        if matriz[x][y] == 1:
            print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")
            pontos += meta*0.5   
        else:
            print("A jornada ainda não acabou!")
    elif goleiro not in ["Gabriel Vasconcelos", "Neymar Jr", "Sérgio Soares", "IShowSpeed", "Rokenedy"]: # goleiro n/ especial, so pontua se a habilidade do luva for maior que a do goleiro
        if matriz[x][y] == 1:
            print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")
            if habilidade_luva > habilidade_goleiro:
                pontos += habilidade_luva - habilidade_goleiro  
        else:
            print("A jornada ainda não acabou!")

    # atualizacao de habilidade
    if pontos >= meta: 
        habilidade_luva += pontos
        if habilidade_luva<=100: 
            print(f"VAMO! PARTIDA {partida_atual} DE {num_treinos}!")
    else:
        if pontos<=100: 
            print("Dá pra recuperar depois! Vamo seguindo!")

    # atualizando num do treino
    partida_atual += 1

# relatorio final
if habilidade_luva > 100: 
    print("NÃO TEM JEITO! EU SEMPRE SOUBE QUE IA SER O MELHOR DO MUNDO! RECEBA!")
elif habilidade_luva == 100: 
    print("O trono do futebol hoje tem dois reis. Eu e Pelé! Não podia estar com alguém melhor!")
else:
    print("Ano que vem tem InterCIn de novo! É só eu treinar mais…")
