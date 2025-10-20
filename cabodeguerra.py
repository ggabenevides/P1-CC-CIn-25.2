#input inicial
print("Começa agora o treinamento para grande final mundial de cabo de guerra!")
qtde_partidas = int(input())

# definindo variaveis
vencedor = ""
perdedor = ""
vitorias_joao = 0
vitorias_arthur = 0

# input quantidade de partidas tem que ser par
while qtde_partidas%2 == 0:
    print("Não deverá haver empates! O número de partidas deverá ser ímpar.")    
    qtde_partidas = int(input())

else:

    # inputs partida
    forca_arthur = int(input())
    forca_joao = int(input())
    resistencia = int(input())
    resistencia_arthur = resistencia
    resistencia_joao = resistencia
    pontos_arthur = 0
    pontos_joao = 0
    virada_impossivel = (vitorias_arthur > qtde_partidas//2) or (vitorias_joao > qtde_partidas//2)
    partida = partida = vitorias_arthur + vitorias_joao + 1
    print(f"Eles batalharão em {qtde_partidas} longas partidas.")

    while not virada_impossivel and partida <= qtde_partidas:
    # PARTIDAS 
        print(f"Começa a {partida}ª partida!")
        print(f"Placar geral: {vitorias_arthur} X {vitorias_joao}")
        
        # resetando variaveis
        resistencia_arthur = resistencia
        resistencia_joao = resistencia
        pontos_arthur = 0
        pontos_joao = 0

        #RODADAS
        while resistencia_arthur > 0 and resistencia_joao > 0:
            numero = int(input())
            # verificando se o numero é primo
            if numero < 2:
                primo = False
            else:
                primo = True
                i = 2
                while i < numero:
                    if numero % i == 0:
                        primo = False
                    i += 1

            # verificando se o numero é um quadrado perfeito
            quadrado = False
            for i in range(numero + 1):
                if i * i == numero:
                    quadrado = True
                
            # definindo vencedor da rodada
            if quadrado:
                resistencia_arthur += 1
                resistencia_joao -= 1
                pontos_arthur += 1
                print("O número é um quadrado perfeito! Arthur consegue puxar mais forte.")
            elif primo:
                resistencia_joao += 1
                resistencia_arthur -= 1
                pontos_joao += 1
                print("O primo do primo é primo do primo? João puxa mais forte!")
            else:
                if forca_arthur > forca_joao:
                    resistencia_arthur += 1
                    resistencia_joao -= 1   
                    pontos_arthur += 1
                    print("Arthur é o mais forte! João não consegue segurar.")
                elif forca_joao > forca_arthur:
                    resistencia_joao += 1
                    resistencia_arthur -= 1
                    pontos_joao += 1
                    print("João é o mais forte! Arthur não consegue segurar.")
                
                # ajustando resistencia
                if resistencia_arthur < 0:
                    resistencia_arthur = 0
                if resistencia_joao < 0:
                    resistencia_joao = 0

        # definindo vencedor da partida
        if pontos_arthur > pontos_joao:
            vitorias_arthur += 1
            vencedor = "Arthur"
            perdedor = "João"
            print("Arthur dá orgulho para Maceió e ganha a partida!")
        elif pontos_joao > pontos_arthur:
            vitorias_joao += 1
            vencedor = "João"
            perdedor = "Arthur"
            print("João usa seus talentos de mangueboy e leva essa para casa!")
        partida += 1
        # se a virada for impossivel o loop para // reavaliando ao final de cada partida
        virada_impossivel = (vitorias_arthur > qtde_partidas//2) or (vitorias_joao > qtde_partidas//2) 
    else:

        # relatorio final
        print()
        print("Agora eles estão prontos para o mundial!")
        print(f"Placar final: {vitorias_arthur} X {vitorias_joao}")
        if vitorias_arthur == 0 or vitorias_joao == 0:

            print(f"{perdedor} não teve chance! {vencedor} venceu todas as partidas.")
        else:
            if vencedor == "João":
                print(f"O ganhador foi {vencedor} com uma diferença de {vitorias_joao - vitorias_arthur} partidas.")
            elif vencedor == "Arthur":
                print(f"O ganhador foi {vencedor} com uma diferença de {vitorias_arthur - vitorias_joao} partidas.")