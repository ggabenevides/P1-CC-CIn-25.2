# inciiando a maquina
print("Ativando a máquina...")

#coletar dados 
nome = str(input())
ano = int(input())

#processar dados
nome.capitalize()
contagem_letra= 0
for letra in nome:
    contagem_letra += 1

if ano%contagem_letra == 0:
    print(f"Previsão confiável! O rebigulador será real em {ano}!")
    if nome == "Frink":
        print("Professor Frink irá inventar o rebigulador?! A máquina deve estar com defeito! Glavin!")
elif ano%contagem_letra != 0:
    print(f"Previsão instável! {nome} também deve achar que o rebigulador é ridículo...")
    if nome == "Frink":
        print("Nem precisava colocar os dados! O rebigulador jamais existiria em qualquer universo!")