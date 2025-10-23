print("Sejam bem-vindos à Big Sub Brasil, onde a fama é temporária, os barracos são eternos, e só um vai conquistar o título de maior subcelebridade do país!")
entrada = input()
participantes = entrada.split(", ")
print(f"{participantes[0].capitalize()} e {participantes[1].capitalize()} disputarão entre si.")

matrizes = []
desempate = []
for i in range(len(participantes)):
    numeros = input()
    lista_numeros = numeros.split(" ")
    n = len(lista_numeros)
    for i in range(n):
        for j in range(0, n-i-1):
            if int(lista_numeros[j]) > int(lista_numeros[j+1]):
                lista_numeros[j], lista_numeros[j+1] = lista_numeros[j+1], lista_numeros[j]
    linha1 = [int(lista_numeros[-3]), int(lista_numeros[-2]), int(lista_numeros[-1])]
    linha2 = [int(lista_numeros[0]), int(lista_numeros[1]), int(lista_numeros[2])]
    linha3 = [int(lista_numeros[3])+1, int(lista_numeros[4])+1, int(lista_numeros[5])+1]
    matriz = [linha1, linha2, linha3]
    num_desempate = int(lista_numeros[6])
    desempate.append(num_desempate)
    matrizes.append(matriz)

# calculando o determinante
determinantes = []
for i in range(len(matrizes)):
    p1 = (matrizes[i][0][0]*matrizes[i][1][1]*matrizes[i][2][2])+(matrizes[i][0][1]*matrizes[i][1][2]*matrizes[i][2][0])+(matrizes[i][0][2]*matrizes[i][1][0]*matrizes[i][2][1])
    p2 = (matrizes[i][0][2]*matrizes[i][1][1]*matrizes[i][2][0])+(matrizes[i][0][0]*matrizes[i][1][2]*matrizes[i][2][1])+(matrizes[i][0][1]*matrizes[i][1][0]*matrizes[i][2][2])
    det = p1 - p2
    determinantes.append(det)

# printando relatorio 
for i in range(len(participantes)):
    for j in range(len(matrizes[i])):
        for x in range(len(matrizes[i][j])): # printando matriz 
            if x == 2:
                print(matrizes[i][j][x])
            else:
                print(f"{matrizes[i][j][x]} ", end="")
    print(f"{participantes[i].capitalize()} está com pontuação {determinantes[i]} pontos.")

# revelando o vencedor 
vencedor = ""
if determinantes[0] > determinantes[1]:
    vencedor = participantes[0]
elif determinantes[0] < determinantes[1]:
    vencedor = participantes[1]
elif determinantes[0] == determinantes[1]:
    # desempate 
    print("RODADA DESEMPATE!!")
    if desempate[0] > desempate[1]:
        vencedor = participantes[0]
        print(f"Contra todas as expectativas (inclusive as nossas), {participantes[0].capitalize()} venceu a rodada!")
        print(f"Seu momento de brilhar virou eclipse {participantes[1].capitalize()}. Melhor sorte no próximo flop!")
    elif desempate[0] < desempate[1]:
        vencedor = participantes[1]
        print(f"Contra todas as expectativas (inclusive as nossas), {participantes[1].capitalize()} venceu a rodada!")
        print(f"Seu momento de brilhar virou eclipse {participantes[0].capitalize()}. Melhor sorte no próximo flop!")      
    
if vencedor != "":
    print(f"Com talento duvidoso e esforço máximo, a vitória é de {vencedor.capitalize()}!")
else: 
    print("Como isso é possível?? Os participantes empataram até na rodada desempate! EU DESISTO!!!")