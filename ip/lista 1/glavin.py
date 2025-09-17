# texto inicial
print("Ativando a máquina...")

#coletar dados 
nome = str(input())
ano = int(input())

#processar dados
nome.capitalize()
contagem_letra= 0
for letra in nome:
    contagem_letra += 1
divisibilidaede = ano%contagem_letra

#relatorio final
if divisibilidaede == 0:
    previsao_confiavel = True
else 
    previsao_confiavel = False

if previsao_confiavel == True:
    if nome == "Frink":
        
