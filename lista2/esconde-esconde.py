print("Vai começar o esconde-esconde UFPE 2025!")

# entradas iniciais
nome1 = str(input())
nome2 = str(input())
nome3 = str(input())
pontos1 = 0
pontos2 = 0
pontos3 = 0

#entradas primeiro jogador
print()
print(f"Prontos ou não, lá vai {nome1}.")
for predio in range(3):
    if predio == 0:
        entrada10 = ""
        print(f"Agora {nome1} procurará no CFCH.")    
        while entrada10 != "Fim da busca nesse prédio.":
            entrada10 = input()
            if entrada10 == "Achou uma pessoa!":
                print(f"{nome1} achou uma pessoa!")
                pontos1+=1
    if predio == 1:
        entrada11 = ""
        print(f"Agora {nome1} procurará no CTG.")
        while entrada11 != "Fim da busca nesse prédio.":
            entrada11 = input()
            if entrada11 == "Achou uma pessoa!":
                print(f"{nome1} achou uma pessoa!")
                pontos1+=1
    if predio == 2:
        entrada12 = ""
        print(f"Agora {nome1} procurará no CIN.") 
        while entrada12 != "Fim da busca nesse prédio.":
            entrada12 = input()
            if entrada12 == "Achou uma pessoa!":
                print(f"{nome1} achou uma pessoa!")
                pontos1+=1

#entradas segundo jogador
print()
print(f"Prontos ou não, lá vai {nome2}.")
for predio in range(3):
    if predio == 0:
        entrada20 = ""
        print(f"Agora {nome2} procurará no CFCH.")    
        while entrada20 != "Fim da busca nesse prédio.":
            entrada20 = input()
            if entrada20 == "Achou uma pessoa!":
                print(f"{nome2} achou uma pessoa!")
                pontos2+=1
    if predio == 1:
        entrada21 = ""
        print(f"Agora {nome2} procurará no CTG.")
        while entrada21 != "Fim da busca nesse prédio.":
            entrada21 = input()
            if entrada21 == "Achou uma pessoa!":
                print(f"{nome2} achou uma pessoa!")
                pontos2+=1
    if predio == 2:
        entrada22 = ""
        print(f"Agora {nome2} procurará no CIN.") 
        while entrada22 != "Fim da busca nesse prédio.":
            entrada22 = input()
            if entrada22 == "Achou uma pessoa!":
                print(f"{nome2} achou uma pessoa!")
                pontos2+=1

#entradas terceiro jogador
print()
print(f"Prontos ou não, lá vai {nome3}.")
for predio in range(3):
    if predio == 0:
        entrada30 = ""
        print(f"Agora {nome3} procurará no CFCH.")    
        while entrada30 != "Fim da busca nesse prédio.":
            entrada30 = input()
            if entrada30 == "Achou uma pessoa!":
                print(f"{nome3} achou uma pessoa!")
                pontos3+=1
    if predio == 1:
        entrada31 = ""
        print(f"Agora {nome3} procurará no CTG.")
        while entrada31 != "Fim da busca nesse prédio.":
            entrada31 = input()
            if entrada31 == "Achou uma pessoa!":
                print(f"{nome3} achou uma pessoa!")
                pontos3+=1
    if predio == 2:
        entrada32 = ""
        print(f"Agora {nome3} procurará no CIN.") 
        while entrada32 != "Fim da busca nesse prédio.":
            entrada32 = input()
            if entrada32 == "Achou uma pessoa!":
                print(f"{nome3} achou uma pessoa!")
                pontos3+=1

#resultado
print()
pontos_vencedor = max(pontos3, pontos2, pontos1)
if pontos_vencedor == 0:
    print("Ninguém foi encontrado, nenhum dos buscadores ganhou a disputa.")
elif pontos_vencedor == pontos3:
    print(f"{nome3} é o(a) melhor no esconde-esconde da UFPE!")
elif pontos_vencedor == pontos2:
    print(f"{nome2} é o(a) melhor no esconde-esconde da UFPE!")
elif pontos_vencedor == pontos1:
    print(f"{nome1} é o(a) melhor no esconde-esconde da UFPE!")