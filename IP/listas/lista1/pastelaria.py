# coletar dados
nome_competidor1 = str(input())
pasteis_competidor1 = int(input())
nome_competidor2 = str(input())
pasteis_competidor2 = int(input())
nome_competidor3 = str(input())
pasteis_competidor3 = int(input())

# definir campeao
if pasteis_competidor1 > (pasteis_competidor2 and pasteis_competidor3):
    nome_campeao = nome_competidor1
    pasteis_campeao = pasteis_competidor1
elif pasteis_competidor2 > (pasteis_competidor1 and pasteis_competidor3):
    nome_campeao = nome_competidor2
    pasteis_campeao = pasteis_competidor2
elif pasteis_competidor3 > (pasteis_competidor1 and pasteis_competidor2):
    nome_campeao = nome_competidor3
    pasteis_campeao = pasteis_competidor3

# relatorio final
if (nome_competidor1 or nome_competidor2 or nome_competidor3) == "Lineu":
    print("Lineu comeu um pastel com gosto estranho e usou sua autoridade na vigilancia sanitaria para acabar com a competição, Beiçola tá desolado!")
else:
    print(f"A(O) campeã(o) é {nome_campeao}, com {pasteis_campeao} pastéis consumidos!")
    
if ((nome_competidor1 or nome_competidor2 or nome_competidor3) == "Floriano") and (nome_campeao != "Floriano"):
    print(f"Anos comendo pastel e perdeu justo para {nome_campeao}, lastimável, Sr. Flor!")

if (nome_campeao == "Agostinho"): 
    if (pasteis_campeao > 100):
        print("Acho que o Agostinho deve ter escondido alguns pastéis na calça, pilantra!")
    elif (50 < pasteis_campeao < 100):
        print("Agostinho madrugou no taxi e veio cheio de fome para a competição!")