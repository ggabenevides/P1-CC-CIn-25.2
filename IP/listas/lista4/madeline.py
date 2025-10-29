# funçoes
def analise_ataque(entrada):
    alteracao_pontos = 0
    if entrada == "Você não tem o que é necessário para escalar.":
        alteracao_pontos -= 20
        print("Eu nunca vou conseguir chegar ao topo :(")
    elif entrada == "NÓS NUNCA DEVERÍAMOS TER SAÍDO DE CASA! VAMOS MORRER NESSA MONTANHA!":
        alteracao_pontos -= 50
        print("NAAÃO EU NUNCA DEVERIA TER INVENTADO DE ESCALAR ESSA MONTANHA!")
    return alteracao_pontos

def analise_reacao(entrada, respiracao=0):
    alteracao_pontos = 0 
    if entrada == "Calma Badeline, nós vamos conseguir.":
        alteracao_pontos += 25
    elif entrada == "Eu sei que somos capazes! Vamos em frente!":
        alteracao_pontos += 10*respiracao
    elif entrada == "Madeline, nós estamos com você. Continue!":
        alteracao_pontos += 60
    return alteracao_pontos

# variaveis
pontos = 100

# programa
while 0 < pontos < 150:
    ataque_badeline = input()
    alteracao_pontos = analise_ataque(ataque_badeline)
    pontos += alteracao_pontos
    if pontos > 0:
        reacao_madeline = input()
        if reacao_madeline == "Eu sei que somos capazes! Vamos em frente!":
            respiracao = int(input())
            alteracao_pontos = analise_reacao(reacao_madeline, respiracao)
        else:
            alteracao_pontos = analise_reacao(reacao_madeline)
        pontos += alteracao_pontos

if pontos <= 0:
    print("Madeline e Badeline não conseguiram se entender... parece que elas nunca vão ver a cidade de cima.")
else:
    print("Madeline chegou ao topo! Ela se senta em um banco para descansar e apreciar a vista.")