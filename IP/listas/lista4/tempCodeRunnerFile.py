# variaveis e listas
time_jogador = []
oponentes = ["lorelei", "bruno", "agatha", "lance"]
times = [[["Lapras", "agua", 220, 50, "Raio de Gelo", 60, "agua", 60],
                ["Blastoise", "agua", 180, 55, "Hidro Bomba", 65, "agua", 78],
                ["Victreebel", "grama", 160, 40, "Folha Navalha", 55, "grama", 70],
                ["Ninetales", "fogo", 170, 45, "Lança-chamas", 60, "fogo", 100]] #lorelei

            [["Charizard", "fogo", 190, 40, "Presa de Fogo", 70, "fogo", 100],
             ["Arcanine", "fogo", 180, 50, "Velocidade Extrema", 60, "fogo", 95],
             ["Kingler", "agua", 170, 60, "Caranguejo Martelo", 65, "agua", 75],
             ["Jolteon", "eletrico", 150, 35, "Choque do Trovão", 55, "eletrico", 130]] #bruno

            [["Venusaur", "grama", 180, 50, "Raio Solar", 70, "grama", 80],
                ["Vileplume", "grama", 160, 45, "Pó do Sono", 50, "grama", 50],
                ["Raichu", "eletrico", 160, 40, "Investida Trovão", 65, "eletrico", 110],
                ["Poliwrath", "agua", 190, 55, "Soco Dinâmico", 60, "agua", 70]] #agatha

            [["Electabuzz", "eletrico", 180, 45, "Soco de Trovão", 75, "eletrico", 105],
                ["Jolteon", "eletrico", 170, 35, "Onda de Trovão", 60, "eletrico", 130],
                ["Exeggutor", "grama", 160, 40, "Bomba de Semente", 65, "grama", 55],
                ["Magmar", "fogo", 175, 40, "Giro de Fogo", 55, "fogo", 93]]] #lance

# funcoes 
# calcular o dano que um pokemon irá causar em outro baseado tanto no tipo como poder de ataque e defesa do oponente
def calculo_dano (tipo_ataque, poder_ataque, tipo_defesa, poder_defesa):
    multiplicador_tipo = 1
    dano_final = 0
    if tipo_ataque == "fogo":
        if tipo_defesa == "grama":
            multiplicador_tipo = 2
        elif tipo_defesa == "água":
            multiplicador_tipo = 0.5
    elif tipo_ataque == "grama":
        if tipo_defesa == "água":
            multiplicador_tipo = 2
        elif tipo_defesa == "fogo":
            multiplicador_tipo = 0.5
    elif tipo_ataque == "água":
        if tipo_defesa == "fogo":
            multiplicador_tipo = 2
        elif tipo_defesa == "grama":
            multiplicador_tipo = 0.5
    elif tipo_ataque == "elétrico":
        if tipo_defesa == "água":
            multiplicador_tipo = 2
    dano_final = (poder_ataque - ( poder_defesa / 2)) * multiplicador_tipo
    if dano_final < 1:
        dano_final = 1
    return dano_final, multiplicador_tipo
    
# decidir quem começa o combate entre dois pokemons em cada turno
def decisao_turno (pokemon_jogador, velocidade_jogador, pokemon_oponente, velocidade_oponente):
    pokemon_que_começa = ""
    if velocidade_jogador > velocidade_oponente:
        pokemon_que_começa = pokemon_jogador
    elif velocidade_jogador < velocidade_oponente:
        pokemon_que_começa = pokemon_oponente
    elif velocidade_jogador == velocidade_oponente:
        pokemon_que_começa = pokemon_jogador
    return pokemon_que_começa

# função principal em que as batalhas de turnos entre os pokemons irão ocorrer
# batalha - rodada - turno
def rodada (lista_pokemon_jogador, lista_pokemon_oponente, numero_rodada):
    turno = 1
    primeiro_pokemon = decisao_turno(lista_pokemon_jogador[0], lista_pokemon_jogador[7], lista_pokemon_oponente[0], lista_pokemon_oponente[7])
    if primeiro_pokemon == lista_pokemon_jogador[0]:
        segundo_pokemon = lista_pokemon_oponente[0]
        lista_primeiro_pokemon = lista_pokemon_jogador.copy()
        lista_segundo_pokemon = lista_pokemon_oponente.copy()
        print_inicio_turno1 = f"{primeiro_pokemon} usa {lista_primeiro_pokemon[5]}!"
        print_inicio_turno2 = f"{segundo_pokemon} do oponente usa {lista_segundo_pokemon[5]}!"
    else: 
        segundo_pokemon = lista_pokemon_jogador[0]
        lista_primeiro_pokemon = lista_pokemon_oponente.copy()
        lista_segundo_pokemon = lista_pokemon_jogador.copy()
        print_inicio_turno1 = f"{segundo_pokemon} usa {lista_segundo_pokemon[5]}!"
        print_inicio_turno2 = f"{primeiro_pokemon} do oponente usa {lista_primeiro_pokemon[5]}!"
    print(f"--- Rodada {numero_rodada} ---")
    print(f"{lista_pokemon_jogador[0]}, eu escolho você!")
    print(f"{lista_pokemon_oponente[0]}, vai!")
    print("--------------------")
    print()
    hp_atual_pokemon1 = lista_primeiro_pokemon[2]
    hp_atual_pokemon2 = lista_segundo_pokemon[2]
    while hp_atual_pokemon1 > 0 and hp_atual_pokemon2 > 0:
        print(f"-- Turno {turno} --")
        print()
        # ataque do primeiro pokemon
        dano = calculo_dano(lista_primeiro_pokemon[1], lista_primeiro_pokemon[6], lista_segundo_pokemon[1], lista_segundo_pokemon[6])
        print(print_inicio_turno1)
        if dano[1] == 2:
            print(f"{lista_primeiro_pokemon[5]} é super efetivo!")
        elif dano[1] == 0.5:
            print(f"{lista_primeiro_pokemon[5]} não é muito efetivo...")
        hp_atual_pokemon2 -= dano[0]
        print(f"Causou {dano[0]} de dano. HP de {segundo_pokemon} agora é {hp_atual_pokemon2}/{lista_segundo_pokemon[2]}.")
        print()

        # ataque do segundo pokemon
        dano = calculo_dano(lista_segundo_pokemon[1], lista_segundo_pokemon[6], lista_primeiro_pokemon[1], lista_primeiro_pokemon[6])
        print(print_inicio_turno2)
        if dano[1] == 2:
            print(f"{lista_segundo_pokemon[5]} é super efetivo!")
        elif dano[1] == 0.5:
            print(f"{lista_segundo_pokemon[5]} não é muito efetivo...")
        hp_atual_pokemon1 -= dano[0]
        print(f"Causou {dano[0]} de dano. HP de {primeiro_pokemon} agora é {hp_atual_pokemon1}/{lista_primeiro_pokemon[2]}.")
        print()
        turno += 1
    else: # atribuindo pokemon derrotado
        if hp_atual_pokemon1 == 0:
            pokemon_derrotado = primeiro_pokemon
        elif hp_atual_pokemon2 == 0:
            pokemon_derrotado = segundo_pokemon
    return pokemon_derrotado

# função da batalha 

# programa 
print("Hora de montar seu time Pokémon!")
for i in range(4):
    entrada = input()
    dados = entrada.split(" - ", maxsplit=7)
    time_jogador.append(dados)
print()
print("Qual membro da Elite Four você deseja enfrentar?")
nome_do_oponente = input()
for i in range(4):
    if nome_do_oponente == oponentes[i]:
        time_oponente = times[i].copy()
print()
print("====================")
print("A BATALHA VAI COMEÇAR!")
print("====================")
print()
while len(time_jogador)>0 and len(time_oponente)>0:
    num_rodada = 1
    pontos_jogador = 0
    pontos_oponente = 0
    pokemons_derotados_jogador = []
    pokemons_derrotados_oponente = []
    pokemon_derrotado = rodada(time_jogador[0], time_oponente[0], num_rodada)
    print()
    if pokemon_derrotado == time_oponente[0][0]:
        pontos_jogador += 1
        pokemons_derrotados_oponente.append(time_oponente[0][0])
        time_oponente.pop(0)
        print(f"{pokemon_derrotado} do oponente foi derrotado!")
    elif pokemon_derrotado == time_jogador[0][0]:
        pontos_oponente += 1
        pokemons_derotados_jogador.append(time_jogador[0][0])
        time_jogador.pop(0)
        print(f"{pokemon_derrotado} foi derrotado!")
    print()
    print("--------------------")
    print()
    print(f"Placar: {pontos_jogador} X {pontos_oponente}")
    print()
else:
    print("========================================")
    if len(time_jogador)==0:
        print("Que pena! Você foi derrotado.")
    else:
        print("Parabéns! Você venceu a batalha Pokémon!")
    print("========================================")
