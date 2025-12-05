entrada = ""
setlist = {"Ato 1": [],
           "Ato 2": [],
            "Ato 3": []}
generos_permitidos = {"Ato 1": ("Hyperpop", "Pop"),
                      "Ato 2": ("Sentimental", "Ballad"),
                      "Ato 3": ("Hyperpop", "Banger")}
duracoes_limite = {"Ato 1": 600,
                   "Ato 2": 480,
                   "Ato 3": 720}

def ad_musica (duracoes_limite, generos_permitidos, setlist, dados_novos, ato_atual, duracao_atual, musicas_adicionadas, musicas_descartadas):
    # tratamento de dados
    nome = dados_novos[0]
    genero = dados_novos[1]
    duracao = dados_novos[2].split(":")
    duracao = int(duracao[0])*60 + int(duracao[1])

    #avaliando dados p adicionar ou não à biblioteca do setlist
    if nome != "Actually Romantic":
        if genero in generos_permitidos[ato_atual]:
            if duracao_atual + duracao <= duracoes_limite[ato_atual]:
                duracao_atual += duracao 
                setlist[ato_atual].append((nome, genero, duracao))
                musicas_adicionadas += 1
                print(f"{nome} adicionada ao {ato_atual} ;).")
            else:
                print(f"Muito longa! O {ato_atual} já está com {duracao_atual} segundos e essa música tem {duracao} segundos.")
                musicas_descartadas += 1
        else:
            print("Gênero errado para esse ato! Cuidado, uma música deslocada mata a vibe de um show…")
            musicas_descartadas += 1
    else:
        print("Já não basta ter exposto a Charli nessa música, agora a Taylor quer que a própria cante? GOLPE BAIXÍSSIMO!!!")
        musicas_descartadas += 1
    
    return [setlist, duracao_atual, musicas_adicionadas, musicas_descartadas]

print("Don't sleep, don't eat, just do it on repeat! Keep bumpin' that!!!")
print()

# loop construcao da setlist
musicas_adicionadas = 0
musicas_descartadas = 0
while entrada != "FIM_SHOW":
    print("Iniciando montagem do Ato 1 (Hyperpop e Pop):")
    print()
    duracao_1 = 0
    while entrada != "FIM_ATO_1":
        ato = "Ato 1"
        entrada = input()
        if entrada != "FIM_ATO_1":
            dados = entrada.split(", ") # nome_música (str), genero (str), duracao_minutos_segundos (str)
            print(f"Música em análise: {dados[0]}")
            if dados[0] == "Talk Talk featuring troye sivan":
                print("A MAIOR AMIZADE DO POP NO PALCO? Talk to them in your own made-up language!")
            elif dados[0] == "Von dutch a. g. cook remix featuring addison rae":
                print("‘CAUSE THEY’RE JUST LIVING THAT LIFE! Addison Rae, a maior revelação do pop desde Britney Spears, no palco ao lado da sua amiga Charli XCX!")
            elif dados[0] == "Guess featuring billie eilish":
                print("Hey, Billie, you there?")
            resultado = ad_musica(duracoes_limite, generos_permitidos, setlist, dados, ato, duracao_1, musicas_adicionadas, musicas_descartadas)    
            setlist = resultado[0]
            duracao_1 = resultado[1]
            musicas_adicionadas = resultado[2]
            musicas_descartadas = resultado[3]

    duracao_2 = 0
    print()
    print("Iniciando montagem do Ato 2 (Sentimental e Ballad):")
    print()
    while entrada != "FIM_ATO_2":
        ato = "Ato 2"
        entrada = input()
        if entrada != "FIM_ATO_2":
            dados = entrada.split(", ") # nome_música (str), genero (str), duracao_minutos_segundos (str)
            print(f"Música em análise: {dados[0]}")
            if dados[0] == "Talk Talk featuring troye sivan":
                print("A MAIOR AMIZADE DO POP NO PALCO? Talk to them in your own made-up language!")
            elif dados[0] == "Von dutch a. g. cook remix featuring addison rae":
                print("‘CAUSE THEY’RE JUST LIVING THAT LIFE! Addison Rae, a maior revelação do pop desde Britney Spears, no palco ao lado da sua amiga Charli XCX!")
            elif dados[0] == "Guess featuring billie eilish":
                print("Hey, Billie, you there?")
            resultado = ad_musica(duracoes_limite, generos_permitidos, setlist, dados, ato, duracao_2, musicas_adicionadas, musicas_descartadas)
            setlist = resultado[0]
            duracao_2 = resultado[1]
            musicas_adicionadas = resultado[2]
            musicas_descartadas = resultado[3]

    duracao_3 = 0
    print()
    print("Iniciando montagem do Ato 3 (Hyperpop e Banger):")
    print()
    while entrada != "FIM_SHOW":
        ato = "Ato 3"
        entrada = input()
        if entrada != "FIM_SHOW":
            dados = entrada.split(", ") # nome_música (str), genero (str), duracao_minutos_segundos (str)
            print(f"Música em análise: {dados[0]}")
            if dados[0] == "Talk Talk featuring troye sivan":
                print("A MAIOR AMIZADE DO POP NO PALCO? Talk to them in your own made-up language!")
            elif dados[0] == "Von dutch a. g. cook remix featuring addison rae":
                print("‘CAUSE THEY’RE JUST LIVING THAT LIFE! Addison Rae, a maior revelação do pop desde Britney Spears, no palco ao lado da sua amiga Charli XCX!")
            elif dados[0] == "Guess featuring billie eilish":
                print("Hey, Billie, you there?")
            resultado = ad_musica(duracoes_limite, generos_permitidos, setlist, dados, ato, duracao_3, musicas_adicionadas, musicas_descartadas)
            setlist = resultado[0]
            duracao_3 = resultado[1]
            musicas_adicionadas = resultado[2]
            musicas_descartadas = resultado[3]

    print()

# relatorio final
duracoes_atos = (duracao_1, duracao_2, duracao_3)
atos = ("Ato 1", "Ato 2", "Ato 3")
vibes_atos = ("Abertura", "Sentimental", "Encerramento")
set_curto = False

for i in range(3):
    if duracoes_atos[i] < duracoes_limite[f"Ato {i+1}"] * 0.7:
        set_curto = True
if set_curto:
    print("Tem certeza que isso é um show? Rápido desse jeito, a Charli XCX deve estar pensando nos doces do backstage…")
    print()

for i in range(3):
    print(f"--- Ato {i+1} ({vibes_atos[i]}) ---")
    for valor in setlist[f"Ato {i+1}"]:
        print(f"{valor[0]} ({valor[1]})")    
    if len(setlist[atos[i]]) == 0:
                print("Nenhuma música adicionada a este Ato.")
    print(f"Duração total do ato: {duracoes_atos[i]} segundos.")               
    print()

# resumo final
print("=== RESUMO DO SHOW (BRAT APPROVED) ===")
print(f"Total de músicas na setlist: {musicas_adicionadas}")
print(f"Total de músicas barradas: {musicas_descartadas}")
