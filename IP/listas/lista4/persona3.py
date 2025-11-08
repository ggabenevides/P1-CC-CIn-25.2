# funcoes 
# calculo de dano
def calculo_dano(nome_atk, poder_atk):
    poder_base_3 = ["Zio", "Garu", "Agi", "Bufu"]
    poder_base_4 = ["Corte", "Perfuração", "Pancada"]
    poder_base_5 = ["Zionga", "Garula", "Agilao", "Bufula"]
    if nome_atk in poder_base_3:
        poder_base = 3
    elif nome_atk in poder_base_4:
        poder_base = 4
    elif nome_atk in poder_base_5:
        poder_base = 5
    dano = int(((poder_base * 15) ** 0.5) * (poder_atk / 2))
    return dano

# bubblesort
def bubblesort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
# turno makoto
def turno_makoto(lista_persona):
    acao = input()
    atk = 0
    if acao == "persona":
        atk = lista_persona[1]
        custo = lista_persona[3]


# turno sombra
# combate

# variaveis
sombras = []
hp_makoto = 300
mana_makoto = 70

# exploracao comecou 
print("Mitsuru: Vamos iniciar nossa exploração, tomem cuidado.")
while hp_makoto > 0:
    # inputs andar antes do combate
    atributos_persona = input().split(" - ", maxsplit=3)
    print(f"{atributos_persona[0]}: Eu sou tu e tu és eu...")
    num_sombras = int(input())
    for i in range(num_sombras):
        sombra = input().split(" - ", maxsplit=3)
        sombras.append(sombra)
    print("Mitsuru: Inimigos detectados, se preparem!")
    # combate
        # turno makoto
        # turno sombra

