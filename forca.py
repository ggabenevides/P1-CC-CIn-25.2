# definindo variaveis
vidas_adivinho = 6
acertou = False

# inicialização
print("Que comece o jogo! Adivinhe a palavra, mas cuidado para não cair na armadilha.")
numero_rodadas =  int(input())

for rodada_atual in range (1, numero_rodadas + 1):
    print(f"Rodada {rodada_atual}/{numero_rodadas}:")
    palavra_secreta = (str(input())).lower()
    palavra_fantasma = (str(input())).lower()

    # checando se a palavra fantasma é válida
    tamanho_secreta = len(palavra_secreta)
    tamanho_fantasma = len(palavra_fantasma)
    letras_em_comum = 0
    letra_ja_contada = ""
    for letra in palavra_secreta:
        if letra in palavra_fantasma and not(letra in letra_ja_contada):
            letras_em_comum += 1
            letra_ja_contada += letra
        
    
    # antes de começar os chutes
    while letras_em_comum >= 3:
        print(f"A palavra fantasma possui {letras_em_comum} letras presentes na palavra secreta. Tente uma com menos de 3 letras iguais.")
        palavra_fantasma = str(input()).lower()
        letras_em_comum = 0
        letra_ja_contada = ""
        for letra in palavra_secreta:
            if letra in palavra_fantasma and not(letra in letra_ja_contada):
                letras_em_comum += 1
                letra_ja_contada += letra

    print("Palavra: ", end="")
    for i in range(1, tamanho_secreta+1):
        if i == tamanho_secreta:
            print("_")
        else:
            print("_ ", end="")

    # chutes
    tentativas = 0 
    letras_ja_tentadas = ""
    print_letras = ""
    tentativas = 0
    acertou = False
    vidas_adivinho = 6
    while not acertou and vidas_adivinho>0:
        chute = (input()).lower()
        num = 0 
        for letra in chute:
            num += 1 
        while num > 1:
            chute = (input()).lower()
            num = 0 
            for letra in chute:
                num += 1 
        if chute in letras_ja_tentadas:
            print(f"Você já tentou a letra '{chute}'. Tente outra.")
        else:
            if chute in palavra_secreta:
                print(f"Boa! A letra '{chute}' está na palavra.")
            elif not(chute in palavra_secreta) and not(chute in palavra_fantasma):
                print(f"Naao! A letra '{chute}' não está na palavra. Você perdeu 1 vida.")
                vidas_adivinho -= 1
            elif not(chute in palavra_secreta) and chute in palavra_fantasma:
                print(f"CUIDADO! A letra '{chute}' é uma armadilha! Você perdeu 2 vidas.")
                vidas_adivinho -= 2        
            tentativas += 1
            letras_ja_tentadas += chute
            print_letras = ""
            nova_palavra_com_lacunas = ""
            posicao_letra = 0
            for letra_secreta in palavra_secreta:
                if letra_secreta in letras_ja_tentadas:
                    if posicao_letra == tamanho_secreta - 1: #ultima letra
                        nova_palavra_com_lacunas += letra_secreta                
                    else: 
                        nova_palavra_com_lacunas += letra_secreta + " "
                else:
                    if posicao_letra == tamanho_secreta - 1: #ultima letra
                        nova_palavra_com_lacunas += "_"                
                    else: 
                        nova_palavra_com_lacunas += "_" + " "
                posicao_letra += 1
            palavra_com_lacunas = nova_palavra_com_lacunas

            qtde_letras_tentadas = len(letras_ja_tentadas)
            novo_print_letras = ""
            reg = 0
            for letra in letras_ja_tentadas:
                novo_print_letras += letra
                if reg < qtde_letras_tentadas - 1:
                    novo_print_letras += ", "
                reg += 1
            print_letras = novo_print_letras

            if "_" not in palavra_com_lacunas:
                acertou = True

            if not acertou and vidas_adivinho>0:
                print("=====================")
                print(f"Palavra: {palavra_com_lacunas}")
                print(f"Vidas restantes: {vidas_adivinho}")
                print(f"Letras chutadas: {print_letras}")
                print("=====================") 
    palavra_maiuscula = (palavra_secreta).capitalize()
    if acertou == True:
        print(f"Parabéns, Adivinho! Você descobriu a palavra secreta: {palavra_maiuscula}.")
        print(f"Total de tentativas: {tentativas}")
    elif vidas_adivinho <= 0:
        print(f"Fim de jogo! A forca está completa e o Adivinho perdeu. A palavra secreta era: {palavra_maiuscula}.")