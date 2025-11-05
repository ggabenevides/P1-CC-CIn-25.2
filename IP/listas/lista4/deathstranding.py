# variaveis 
hp_sam = 100
hp_neil = 100
matriz_espaco = []

# funcoes 
# Função para calcular a distância de Chebyshev - d(x,y)=max(|x2−x1|,|y2−y1|)
# Função para a ação de atirar de Sam
# Função para a mecânica de teletransporte de Neil

#programa

# inicializacao
print("Sam: Mas que lugar é esse aqui?")
print("Dollman: WASD... Num exclusivo de PS5? Ah, fala sério!")
print()

# inputs matriz
linha0 = input()
linha1 = input()
linha2 = input()
linha3 = input()
linha4 = input()
linha5 = input()

#tratando dados da matriz
linha0 = linha0.split(" ", maxsplit=5)
linha1 = linha1.split(" ", maxsplit=5)
linha2 = linha2.split(" ", maxsplit=5)
linha3 = linha3.split(" ", maxsplit=5)
linha4 = linha4.split(" ", maxsplit=5)
linha5 = linha5.split(" ", maxsplit=5)
matriz_espaco.append(linha0)
matriz_espaco.append(linha1)
matriz_espaco.append(linha2)
matriz_espaco.append(linha3)
matriz_espaco.append(linha4)
matriz_espaco.append(linha5)
print(matriz_espaco)

# loop jogadas
while hp_neil>0:
    movimento_wasd = input()
    troca_de_arma = input()
    atirar = input()