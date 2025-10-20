#input incial
print("INICIANDO SIMULAÇÃO...")
jogador1 = str(input())
while jogador1 != "Arthur" and jogador1 != "Samuel":
    print("Jogador inválido! Essa competição é apenas entre Arthur e Samuel!")
    jogador1 = str(input())
else:
    print(f"{jogador1} começa na corda!")
qtde_rodadas = int(input())
if jogador1 == "Arthur":
    jogador2 = "Samuel"
else:
    jogador2 = "Arthur"

pulo_atual = 0
num_tropecos = 0
pontos1 = 0
pontos2 = 0
ja_printou_antes = False

for rodada in range(1, qtde_rodadas + 1):
    ritmo = int(input())
    aposta = int(input())

    if rodada%2 == 0:
        jogador_atual = jogador2
        jogador_espectador = jogador1
    else:
        jogador_atual = jogador1
        jogador_espectador = jogador2

    # prints da rodada
    print(f"Começa a {rodada}ª rodada!")    
    if rodada == qtde_rodadas:
        print("Última rodada! Valendo 2 pontos!")
    print(f"{jogador_espectador} aposta que {jogador_atual} não chega a {aposta} pulos! Vamos ver se é verdade! O ritmo de {jogador_atual} será {ritmo}!")
    pulo_atual = 0
    num_tropecos = 0
    while pulo_atual < aposta and num_tropecos < 3:
        x = aposta - pulo_atual
        # AJEITAR ESSA PARTE 
        # achando a soma dos algarismos
        j = str(x)
        soma = 0
        for c in j:
            soma += int(c)
        #checando se a soma dos algarismos faz parte da sequencia de fibonacci
        fibonacci = False
        for i in range(soma*3):
            if i * i == 5*soma**2 + 4 or i*i == 5*soma**2 - 4:
                fibonacci = True
        
        #acrescimo no numero de tropeços
        if fibonacci :
            num_tropecos +=1
            print(f"O número da soma é {soma}, que faz parte da sequência de Fibonacci!! {jogador_atual} tropeça!")
        else:
            if pulo_atual > 3*(aposta/4) and not ja_printou_antes:
                print(f"{jogador_atual} está quase chegando ao apostado! Falta pouco!") 
                ja_printou_antes = True
            else:
                print(f"{jogador_atual} pula com maestria! Faltam {aposta - pulo_atual} pulos!")         
        if num_tropecos == 3:
            print(f"E agora não tem jeito, {jogador_atual} cai de cara no chão!")

        #acrescimo no pulo
        pulo_atual += ritmo

    #pontuando
    if (pulo_atual == aposta and num_tropecos<3) or (pulo_atual > aposta and num_tropecos<3):
        if rodada == qtde_rodadas:
            if jogador_atual == jogador1:
                pontos1 += 2
            else:
                pontos2 += 2 
        else:
            if jogador_atual == jogador1:
                pontos1 += 1
            else:
                pontos2 += 1
    if num_tropecos<3 and pulo_atual>=aposta: #venceu  a rodada
        if pulo_atual == aposta:
            print(f"{jogador_atual} cumpriu o prometido e alcançou {aposta} pulos! Ponto merecidíssimo!")
        if pulo_atual > aposta:
            print(f"{jogador_atual} vai além, e supera a aposta em {pulo_atual - aposta} Ponto(s)! Deixou o {jogador_espectador} no chinelo!")
    if num_tropecos==3 and pulo_atual<aposta: #perdeu a rodada
        if pulo_atual < aposta//2:
            print(f"Nossa!! Parece que {jogador_atual} não chegou nem na metade do apostado! Ainda bem que não foi competir pra valer no Round 6!")
        elif aposta//2 < pulo_atual < 3*(aposta/4):
            print(f"Nem muito perto, nem muito longe do apostado. Talvez {jogador_atual} teve apenas azar!")
        elif pulo_atual > 3*(aposta/4) and pulo_atual != aposta and pulo_atual < aposta:
            print(f"Quase lá! por pouco {jogador_atual} não alcançou o apostado!")
    

#definindo vencedor
if pontos1 > pontos2:
        vencedor = jogador1
elif pontos2 > pontos1:
        vencedor = jogador2
elif pontos1 == pontos2:
    vencedor = ""

# relatorio final
print("COMPUTANDO PREVISÃO FINAL...")
if vencedor == "Arthur":
    if jogador2 == "Arthur":
        print(f"Arthur venceu a competição com {pontos2} ponto(s)! Trouxe orgulho para Maceió!")
    elif jogador1 == "Arthur":
        print(f"Arthur venceu a competição com {pontos1} ponto(s)! Trouxe orgulho para Maceió!")
elif vencedor == "Samuel":
    if jogador2 == "Samuel":
        print(f"Samuel venceu a competição com {pontos2} ponto(s)! O Messi careca em sua foto de perfil ficaria impressionado se soubesse!")
    elif jogador1 == "Samuel":
        print(f"Samuel venceu a competição com {pontos1} ponto(s)! O Messi careca em sua foto de perfil ficaria impressionado se soubesse!")
elif pontos1==pontos2 and pontos1>0:
    print(f"Houve um empate técnico! Ambos fizeram {pontos1} ponto(s)! Óbvio que os dois monitores mais rápidos iriam empatar!")
elif pontos1==pontos1 and pontos1==0:
    print(f"Ninguém pontuou! Que competição sem graça! Acho que os monitores se garantem mais nas dúvidas de IP mesmo...")


