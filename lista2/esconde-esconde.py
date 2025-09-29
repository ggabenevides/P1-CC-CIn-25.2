print("Vai começar o esconde-esconde UFPE 2025!")

for jogador in range(1,4):
    nome = str(input())
    pontos = 0
    print()
    print(f"Prontos ou não, lá vai {nome}.")
    for predio in range(2):
        if predio == 0:
            print(f"Agora {nome} procurará no CFCH.")
        if predio == 1:
            print(f"Agora {nome} procurará no CTG.")
        if predio == 2:
            print(f"Agora {nome} procurará no CIN.") 
    while entrada != "Fim da busca nesse prédio.":
        entrada = input()
        pontos+=1



