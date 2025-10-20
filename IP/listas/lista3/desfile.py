# listas
monitores = ["Adrieli Queiroz", "Arthur Jorge", "César Cavalcanti", 
                   "Elisson Oliveira", "Filipe Moreira", "Gabriela Alves", 
                   "Joab Henrique", "Maria Fernanda", "Miriam Gonzaga", "Sofia Remindes"]
monitores_disponiveis = ["Adrieli Queiroz", "Arthur Jorge", "César Cavalcanti", 
                   "Elisson Oliveira", "Filipe Moreira", "Gabriela Alves", 
                   "Joab Henrique", "Maria Fernanda", "Miriam Gonzaga", "Sofia Remindes"]

intrusos = []
lista_desfilantes = []

# dados iniciais
print("Senhoras e senhores, o desfile de gala do CIn vai começar!")
num_desfilantes = int(input())
marca_patrocinador = input()
if marca_patrocinador == "Tha Beauty":
    patrocinador = "Thais Linares"
elif marca_patrocinador == "DeGuê?":
    patrocinador = "Davi Brito"
elif marca_patrocinador == "Diva Depressão":
    patrocinador = "Edu e Fih"

# recebendo inputs dos desfilantes e adicionando nas listas corretas
for i in range(num_desfilantes):
    desfilante = input()
    lista_desfilantes.append(desfilante)
    if desfilante in monitores:
        monitores_disponiveis.remove(desfilante)
    if desfilante not in monitores and desfilante != patrocinador:
        intrusos.append(desfilante)

num_invasoes = 0
ja_printou_core = False
for i in range(num_desfilantes):
    if num_invasoes == 3 and not ja_printou_core:
        lista_desfilantes.insert(i, "Core")
        num_desfilantes += 1
    desfilante_atual = lista_desfilantes[i]
    
    # prints a cada desfilante
    if desfilante_atual == "Core": # caso especial
        print("Muitas invasões estão deixando a galera irritada... Chama o Core pra acalmar os ânimos!")
        print(f"Desfilante de n° {i+1}: {desfilante_atual}!") 
        ja_printou_core = True
    elif desfilante_atual in monitores: # caso normal
        print(f"Desfilante de n° {i+1}: {desfilante_atual}!")
    elif desfilante_atual == patrocinador: # invasao tolerada
        print("Invasão tolerada por motivos de patrocínio!")
        print(f"Desfilante de n° {i+1}: {desfilante_atual}!")
    else: #invasao nao tolerada
        print(f"{desfilante_atual} invadiu a passarela! Segurem ele(a), produção!")
        if len(monitores_disponiveis) > 0:
            print(f"Desfilante de n° {i+1}: {monitores_disponiveis[0]}!")
            monitores_disponiveis.remove(monitores_disponiveis[0])
        else: 
            print(f"Desfilante de n° {i+1}: {desfilante_atual}?! Pelo visto não havia como substituir...")
        num_invasoes += 1

# relatorio final
if "Tulla Luana" in intrusos or "Inês Brasil" in intrusos or "Gretchen" in intrusos:
    print("Nas arquibancadas do CIn, sussurros indignados agitam a multidão...")
    if "Gretchen" in intrusos:
        print('"Eles tem que respeitar os meus 37 anos de carreira! Eu hoje sou um ícone, se eu morrer hoje eu vou continuar sendo a Gretchen!"')
    if "Tulla Luana" in intrusos:
        print('"Ninguém ser humano está acima de mim! Mas eu estou acima de muitos... é assim que eu penso."')
    if "Inês Brasil" in intrusos:
        print('"É aquele ditado... Vamo fazer o quê?"')
    