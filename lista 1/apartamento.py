# coletar dados de entrada
artigos_lidos_Sheldon = (int(input()))
artigos_lidos_Leonard = (int(input()))
artigos_lidos_Raj =  (int(input()))
artigos_lidos_Howard = (int(input()))
experimentos_realizados_por_Sheldon = (int(input()))
experimentos_realizados_por_Leonard = (int(input()))
experimentos_realizados_por_Raj = (int(input()))
experimentos_realizados_por_Howard = (int(input()))

# processar dados pontuação = artigos * 2 + experimentos * 3
pontuacao_Sheldon = artigos_lidos_Sheldon * 2 + experimentos_realizados_por_Sheldon * 3
pontuacao_Leonard = artigos_lidos_Leonard * 2 + experimentos_realizados_por_Leonard * 3
pontuacao_Raj = artigos_lidos_Raj * 2 + experimentos_realizados_por_Raj * 3
pontuacao_Howard = artigos_lidos_Howard * 2 + experimentos_realizados_por_Howard * 3
pontos_vencedor = max(pontuacao_Howard, pontuacao_Leonard, pontuacao_Raj, pontuacao_Sheldon)

# definir vencedor
if pontuacao_Sheldon > pontuacao_Leonard and pontuacao_Sheldon > pontuacao_Raj and pontuacao_Sheldon > pontuacao_Howard:
    nome_vencedor = "Sheldon"
elif pontuacao_Leonard > pontuacao_Sheldon and pontuacao_Leonard > pontuacao_Raj and pontuacao_Leonard > pontuacao_Howard:
    nome_vencedor = "Leonard"
elif pontuacao_Raj > pontuacao_Sheldon and pontuacao_Raj > pontuacao_Leonard and pontuacao_Raj > pontuacao_Howard:
    pontos_vencedor = pontuacao_Raj
    nome_vencedor = "Raj"
elif pontuacao_Howard > pontuacao_Sheldon and pontuacao_Howard > pontuacao_Leonard and pontuacao_Howard > pontuacao_Raj:
    nome_vencedor = "Howard"
else:
    #definir vencedor em caso de empate
    check = 0
    if pontos_vencedor == pontuacao_Sheldon: 
        check += 9
    if pontos_vencedor == pontuacao_Leonard:
        check += 4
    if pontos_vencedor == pontuacao_Raj:
        check += 2
    if pontos_vencedor == pontuacao_Howard:
        check += 1 
    if check >= 9:
        nome_vencedor = "Sheldon"
    elif  4 <= check <= 7:
        nome_vencedor = "Leonard"
    elif 2 <= check <= 3:
        nome_vencedor = "Raj"
    elif check == 1:
        nome_vencedor = "Howard"

# resultado
print("Pontuação final:")
print(f"Sheldon: {pontuacao_Sheldon}")
print(f"Leonard: {pontuacao_Leonard}")
print(f"Raj: {pontuacao_Raj}")
print(f"Howard: {pontuacao_Howard}")
print(" ")
print(f"O cientista da semana é: {nome_vencedor}")

# comentarios extras
if nome_vencedor == "Sheldon":
    print("Não é atoa que ele ganhou o prêmio Nobel")
elif  nome_vencedor == "Leonard":
    print("A vitória dele prova que aguentar o Sheldon já é um experimento científico por si só.")
elif nome_vencedor == "Raj":
    print("Ele comemora... mas ainda precisa da ajuda do cachorro para falar com mulheres.")
elif nome_vencedor == "Howard":
    print("Um pequeno passo para a ciência, um grande salto para alguém com mestrado.")
