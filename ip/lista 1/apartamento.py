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

# definir vencedor
if pontuacao_Sheldon > pontuacao_Leonard and pontuacao_Sheldon > pontuacao_Raj and pontuacao_Sheldon > pontuacao_Howard:
    nome_vencedor = "Sheldon"
    pontos_vencedor = pontuacao_Sheldon
elif pontuacao_Leonard > pontuacao_Sheldon and pontuacao_Leonard > pontuacao_Raj and pontuacao_Leonard > pontuacao_Howard:
    nome_vencedor = "Leonard"
    pontos_vencedor = pontuacao_Leonard
elif pontuacao_Raj > pontuacao_Sheldon and pontuacao_Raj > pontuacao_Leonard and pontuacao_Raj > pontuacao_Howard:
    nome_vencedor = "Raj"
    pontos_vencedor = pontuacao_Raj
elif pontuacao_Howard > pontuacao_Sheldon and pontuacao_Howard > pontuacao_Leonard and pontuacao_Howard > pontuacao_Raj:
    nome_vencedor = "Howard"
    pontos_vencedor = pontuacao_Howard

#definir empate
check = 0
if pontos_vencedor == pontuacao_Sheldon: 
    check += 9
if pontos_vencedor == pontuacao_Leonard:
    check += 4
if pontos_vencedor == pontuacao_Raj:
    check += 2
if pontos_vencedor == pontuacao_Howard:
    check += 1 

# resultado
print("Pontuação final:")
print(f"Sheldon: {pontuacao_Sheldon}")
print(f"Leonard: {pontuacao_Leonard}")
print(f"Raj: {pontuacao_Raj}")
print(f"Howard: {pontuacao_Howard}")
print(" ")
print(f"O cientista da semana é: {nome_vencedor}")
if check >= 9:
    print("Não é atoa que ele ganhou o prêmio Nobel")
elif  4 <= check <= 7:
    print("A vitória dele prova que aguentar o Sheldon já é um experimento científico por si só.")
elif 2 <= check <= 3:
    print("Ele comemora... mas ainda precisa da ajuda do cachorro para falar com mulheres.")
elif check == 1:
    print("Um pequeno passo para a ciência, um grande salto para alguém com mestrado.")
    
