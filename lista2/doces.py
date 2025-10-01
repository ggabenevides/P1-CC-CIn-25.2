doces = int(input())

jogador1 = str(input())
jogador2 = str(input())
vidas1 = 10
vidas2 = 10
jogada1 = ""
jogada2 = ""
vencedor_rodada = ""

if doces < 10:
    num_rodadas = 1
    doces_rodada1 = doces_rodadas = doces
else:
    if doces%10 != 0:
        doces_rodada1 = doces%10
        doces_rodadas = 10
        num_rodadas = doces//10 + 1
    else:
        num_rodadas = doces//10
        doces_rodadas = doces_rodada1 = 10

if jogador1 != "Arthur" and jogador2 != "Arthur":
    print("Epa!!! E cadê o dono dos doces??")
else: 
    print("A batalha vai começar!")
    for i in range(1,num_rodadas+1):
        if i == 1 and doces%10!=0:
            print(f"Pra aquecer, essa primeira vale menos, só {doces_rodada1} doces!")
        else: 
            print(f"Batalha número {i}!")
        while vidas1 != 0 and vidas2 != 0:
            jogada1 = input()
            jogada2 = input()
            if jogada1 == jogada2:
                print("Eita, jogaram a mesma coisa dessa vez.")
            else:
                if jogada1 == "papel" and jogada2 == "tesoura":
                    vidas1-=3
                    vidas2+=1
                elif jogada2 == "papel" and jogada1 == "tesoura":
                    vidas2-=3
                    vidas1+=1
                elif jogada1 == "papel" and jogada2 == "pedra" :
                    vidas2-=2
                    vidas1+=2
                elif jogada2 == "papel" and jogada1 == "pedra" :
                    vidas1-=2
                    vidas2+=2
                elif jogada1 == "pedra" and jogada2 == "tesoura":
                    vidas2-=4
                elif jogada2 == "pedra" and jogada1 == "tesoura":
                    vidas1-=4
                if vidas1 < 0:
                    vidas1 = 0
                if vidas2 < 0:
                    vidas2 = 0
                print(f"Esse turno terminou com {jogador1} tendo {vidas1} de vida e {jogador2} tendo {vidas2}!")
        else:    
            if vidas1 == 0:
                vencedor_rodada = jogador2
            elif vidas2 == 0:
                vencedor_rodada = jogador1
            print(f"A rodada {i} vai para {vencedor_rodada}, que garante seus doces!")
        vidas1 = 10
        vidas2 = 10