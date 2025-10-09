# texto inicial
print("Ativando a máquina...")

#coletar dados 
nome = str(input())
ano = int(input())

#processar dados
nome = nome.capitalize()
contagem_letra= 0
contagem_letra = len(nome)
divisibilidade = ano % contagem_letra

print("Quantidade de letras:", contagem_letra)
print("Ano % Quantidade de letras =", divisibilidade)

#relatorio final
if divisibilidade == 0:
    previsao_confiavel = True
else:
    previsao_confiavel = False

if previsao_confiavel == True:
    if nome == "Frink":
        print("Professor Frink irá inventar o rebigulador?! A máquina deve estar com defeito! Glavin!")
    else:
        print(f"Previsão confiável! O rebigulador será real em {ano}!")
else:
    if nome == "Frink":
        print("Nem precisava colocar os dados! O rebigulador jamais existiria em qualquer universo!")
    else:

            print(f"Previsão instável! {nome} também deve achar que o rebigulador é ridículo...")

