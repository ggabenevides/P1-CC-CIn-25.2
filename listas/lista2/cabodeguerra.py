#input inicial
print("Começa agora o treinamento para grande final mundial de cabo de guerra!")
qtde_partidas = int(input())

# definindo variaveis
vencedor = ""
vitorias_joao = 0
vitorias_arthur = 0
numero_primo = True

# input quantidade de partidas tem que ser par
while qtde_partidas%2 == 0:
    print("Não deverá haver empates! O número de partidas deverá ser ímpar.")    
    qtde_partidas = int(input())
else:
    print(f"Eles batalharão em {qtde_partidas} longas partidas.")
    # inputs partida
    forca_arthur = int(input())
    forca_joao = int(input())
    resistencia = int(input())
    resistencia_arthur = resistencia
    resistencia_joao = resistencia
    # inicio da partida
    for partida in range(1, qtde_partidas+1):
        # A competição como um todo também pode encerrar antes do fim, caso não haja mais chance de virada
        virada_impossivel = (vitorias_arthur > qtde_partidas//2) or (vitorias_joao > qtde_partidas//2)
        while resistencia_arthur > 0 or resistencia_joao > 0 or not virada_impossivel:
            print(f"Começa a {partida}ª partida!")
            print(f"Placar geral: {vitorias_arthur} X {vitorias_joao}")
            numero = int(input())
            # atribuindo vencedor da rodada
            # AJEITAR ESSA PARTE AQUI
            for i in range(2, numero//2 +1):
                    if numero % i == 0:
                        numero_primo = False      
            if type(numero**0.5) == int:
                vencedor = "arthur"
                perdedor = "joao"
                resistencia_arthur += 1
                resistencia_joao -= 1
                vitorias_arthur += 1
                print("O número é um quadrado perfeito! Arthur consegue puxar mais forte.")
            elif numero_primo:
                vencedor = "joao"
                perdedor = "arthur"
                resistencia_joao += 1
                resistencia_arthur -= 1
                vitorias_joao += 1
                print("O primo do primo é primo do primo? João puxa mais forte!")
            else:
                if forca_arthur > forca_joao:
                    vencedor = "arthur"
                    perdedor = "joao"
                    resistencia_arthur += 1
                    resistencia_joao -= 1
                    vitorias_arthur += 1
                    print("Arthur dá orgulho para Maceió e ganha a partida!")
                elif forca_joao < forca_arthur:
                    vencedor = "joao"
                    perdedor = "arthur"
                    resistencia_joao += 1
                    resistencia_arthur -= 1
                    vitorias_joao += 1
                    print("João usa seus talentos de mangueboy e leva essa para casa!")
            virada_impossivel = (resistencia_arthur > qtde_partidas//2) or (resistencia_joao > qtde_partidas//2)    
    else:
        print("Agora eles estão prontos para o mundial!")
        print(f"Placar final: {vitorias_arthur} X {vitorias_joao}")
        if vitorias_arthur == 0 or vitorias_joao == 0:
            print(f"{perdedor} não teve chance! {vencedor} venceu todas as partidas.")
        else:
            if vencedor == "joao":
                print(f"O ganhador foi {vencedor} com uma diferença de {vitorias_joao - vitorias_arthur} partidas.")
            elif vencedor == "arthur":
                print(f"O ganhador foi {vencedor} com uma diferença de {vitorias_arthur - vitorias_joao} partidas.")