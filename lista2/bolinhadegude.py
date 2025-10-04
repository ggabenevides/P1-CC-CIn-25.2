# input inicial
bolas_a = int(input())
bolas_b = int(input())
bolas_c = int(input())

#definindo variaveis
erros_a = 0
erros_b = 0
erros_c = 0

eliminado_a = bolas_a <= 0 or erros_a >= 3
eliminado_b = bolas_b <= 0 or erros_b >= 3
eliminado_c = bolas_c <= 0 or erros_c >= 3

ja_estava_fora_a = False
ja_estava_fora_b = False
ja_estava_fora_c = False

num_eliminados = 0

while num_eliminados < 2:
    
    # input rodada
    # reavaliando os eliminados 
    eliminado_a = bolas_a <= 0 or erros_a >= 3
    eliminado_b = bolas_b <= 0 or erros_b >= 3
    eliminado_c = bolas_c <= 0 or erros_c >= 3
    if not eliminado_a:
        jogada_a = str(input())
        # atualizando o placar 
        if jogada_a == "acertou":
            if num_eliminados==1:
                bolas_a +=1
            else:
                bolas_a += 2
            if not eliminado_b:
                bolas_b -=1
            if not eliminado_c:
                bolas_c -=1
        else: 
            erros_a += 1
    else:
        if not ja_estava_fora_a:
            num_eliminados += 1
    # reavaliando os eliminados 
    eliminado_a = bolas_a <= 0 or erros_a >= 3
    eliminado_b = bolas_b <= 0 or erros_b >= 3
    eliminado_c = bolas_c <= 0 or erros_c >= 3
    if not eliminado_b:
        jogada_b = str(input())
        # atualizando o placar 
        if jogada_b == "acertou":
            if num_eliminados==1:
                bolas_b +=1
            else:
                bolas_b += 2
            if not eliminado_a:
                bolas_a -=1
            if not eliminado_c:
                bolas_c -=1
        else: 
            erros_b+= 1
    else:
        if not ja_estava_fora_b:
            num_eliminados += 1
    # reavaliando os eliminados 
    eliminado_a = bolas_a <= 0 or erros_a >= 3
    eliminado_b = bolas_b <= 0 or erros_b >= 3
    eliminado_c = bolas_c <= 0 or erros_c >= 3
    if not eliminado_c:
        jogada_c = str(input())
        # atualizando o placar 
        if jogada_c == "acertou":
            if num_eliminados==1:
                bolas_c +=1
            else:
                bolas_c += 2
            if not eliminado_b:
                bolas_b -=1
            if not eliminado_a:
                bolas_a -=1
        else: 
            erros_c += 1
    else:
        if not ja_estava_fora_c:
            num_eliminados += 1
        

    # reavaliando os eliminados 
    eliminado_a = bolas_a <= 0 or erros_a >= 3
    eliminado_b = bolas_b <= 0 or erros_b >= 3
    eliminado_c = bolas_c <= 0 or erros_c >= 3

    #  eliminacao
    if eliminado_a and not ja_estava_fora_a:
        if erros_a >= 3:
            print("andre perdeu feio")
        else:
            print("andre saiu do jogo")
    if eliminado_b and not ja_estava_fora_b:
        if erros_b >= 3:
            print("bruno perdeu feio")
        else:
            print("bruno saiu do jogo")
    if eliminado_c and not ja_estava_fora_c:
        if erros_c >= 3:
            print("clara perdeu feio")
        else:
            print("clara saiu do jogo")    
    
    # estado atual de eliminação
    ja_estava_fora_a = eliminado_a
    ja_estava_fora_b = eliminado_b
    ja_estava_fora_c = eliminado_c

else:

    # definindo vencedor
    vencedor = ""
    if not eliminado_a:
        vencedor = "andre"
    elif not eliminado_b:
        vencedor = "bruno"
    elif not eliminado_c:
        vencedor = "clara"

    # resultado final
    print(f"{vencedor} ganhou")
    print("a quantidade final de bolas foi:")
    print(f"andre: {bolas_a}")
    print(f"bruno: {bolas_b}")
    print(f"clara: {bolas_c}")