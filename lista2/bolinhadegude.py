bolas_a = int(input())
bolas_b = int(input())
bolas_c = int(input())
erros_a = 0
erros_b = 0
erros_c = 0

while (b_andre>0 or erros_a<3) and (b_bruno>0 or erros_b<3) and (b_clara>0 or erros_c<3):
    jogada_a = str(input())
    jogada_b = str(input())
    jogada_c = str(input())
    if jogada_a == "acertou":
        b_andre +=2
        b_bruno -=1
        b_clara -=1
    if jogada_b == "acertou":
        b_bruno +=2
        b_andre -=1
        b_clara -=1
    if jogada_c == "acertou":
        b_clara +=2
        b_bruno -=1
        b_andre -=1
    if jogada_a == "errou":
        erros_a +=1
    if jogada_b == "errou":
        erros_b +=1
    if jogada_c == "errou":
        erros_c +=1
    if erros_a == 3:
        print("andre perdeu feio")
    if erros_b == 3:
        print("bruno perdeu feio")
    if erros_c == 3:
        print("clara perdeu feio")
    if b_bruno == 0:
        print("bruna saiu do jogo")
    if b_andre == 0:
        print("andre saiu do jogo")
    if b_clara == 0:
        print("clara saiu do jogo")
while (b_andre>0 or erros_a<3) and (b_bruno>0 or erros_b<3) and (b_clara == 0 or erros_c==3):
    jogada_a = str(input())
    jogada_b = str(input())
    if jogada_a == "acertou":
        b_andre +=2
        b_bruno -=1
    if jogada_b == "acertou":
        b_bruno +=2
        b_andre -=1
    if jogada_a == "errou":
        erros_a +=1
    if jogada_b == "errou":
        erros_b +=1
    if erros_a == 3:
        print("andre perdeu feio")
    if erros_b == 3:
        print("bruno perdeu feio")
    if b_bruno == 0:
        print("bruno saiu do jogo")
    if b_andre == 0:
        print("andre saiu do jogo")
while (b_andre>0 or erros_a<3) and (b_clara>0 or erros_c<3) and (b_bruno == 0 or erros_b==3):
    jogada_a = str(input())
    jogada_c = str(input())
    if jogada_a == "acertou":
        b_andre +=2
        b_clara -=1
    if jogada_c == "acertou":
        b_clara +=2
        b_andre -=1
    if jogada_a == "errou":
        erros_a +=1
    if jogada_c == "errou":
        erros_c +=1
    if erros_a == 3:
        print("andre perdeu feio")
    if erros_c == 3:
        print("clara perdeu feio")
    if b_andre == 0:
        print("andre saiu do jogo")
    if b_clara == 0:
        print("clara saiu do jogo")
while (b_bruno>0 or erros_b<3) and (b_clara>0 or erros_c<3) and (b_andre == 0 or erros_a==3):
    jogada_b = str(input())
    jogada_c = str(input())
    if jogada_b == "acertou":
        b_bruno +=2
        b_clara -=1
    if jogada_c == "acertou":
        b_clara +=2
        b_bruno -=1
    if jogada_b == "errou":
        erros_b +=1
    if jogada_c == "errou":
        erros_c +=1
    if erros_b == 3:
        print("bruno perdeu feio")
    if erros_c == 3:
        print("clara perdeu feio")
    if b_bruno == 0:
        print("bruno saiu do jogo")
    if b_clara == 0:
        print("clara saiu do jogo")
else: 
    if (b_bruno==0 or erros_b==3) and (b_clara==0 or erros_c==3):
        vencedor = "andre"
    if (b_andre==0 or erros_a== 3) and (b_clara==0 or erros_c==3):
        vencedor = "bruno"
    if (b_bruno==0 or erros_b==3) and (b_andre==0 or erros_a== 3):
        vencedor = "clara"
    print(f"{vencedor} ganhou")
    print("a quantidade final de bolas foi:")
    print(f"andre: {b_andre}")
    print(f"bruno: {b_bruno}")
    print(f"clara: {b_clara}")