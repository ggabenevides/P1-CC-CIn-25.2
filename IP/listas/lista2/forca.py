# definindo variaveis
vidas_adivinho = 6


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
        palavra_fantasma = str(input())
    print("Palavra:", end="")
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
    while letras_ja_tentadas != palavra_secreta and vidas_adivinho>0:
        chute = input()
        if chute in letras_ja_tentadas:
            print(f"Você já tentou a letra '{chute}'. Tente outra")
        else:
            if chute in palavra_secreta:
                print(f"Boa! A letra '{chute}' está na palavra.")
            elif not(chute in palavra_secreta) and not(chute in palavra_fantasma):
                print(f"Naao! A letra '{chute}' não está na palavra. Você perdeu 1 vida.")
                vidas_adivinho -= 1
            elif not(chute in palavra_secreta) and chute in palavra_fantasma:
                print(f"CUIDADO! A letra '{chute}' é uma armadilha! Você perdeu 2 vidas.")
                vidas_adivinho -= 2
        num_vezes_letra = 0
        for letra in palavra_secreta:
            if letra == chute:
                num_vezes_letra +=1     
        posicao_letra = 0
        print("=====================")
        print("Palavra:", end="")
        # imprimindo a palavra com as lacunas preenchidas
        for j in range(1, tamanho_secreta+1):
            if num_vezes_letra == 1:
                if j == posicao_letra:
                    if i == tamanho_secreta:
                        print(chute)
                    else:
                        print(chute, end="")
                else: 
                    if i == tamanho_secreta:
                        print("_")
                    else:
                        print("_", end="")
        print(f"Vidas restantes: {vidas_adivinho}")
        if rodada_atual == 1:
            print_letras = f"Letras chutadas: {chute}"
        else:
            print_letras = print_letras + "," + chute
        print(print_letras)
        print("=====================")
        tentativas += 1
        letras_ja_tentadas += chute
    else:
        palavra_secreta = (palavra_secreta).capitalize()
        if letras_ja_tentadas == palavra_secreta:
            print(f"Parabéns, Adivinho! Você descobriu a palavra secreta: {palavra_secreta}.")
            print(f"Total de tentativas: {tentativas}")
        elif vidas_adivinho == 0:
            print(f"Fim de jogo! A forca está completa e o Adivinho perdeu. A palavra secreta era: {palavra_secreta}.")