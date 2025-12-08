def cifra_de_cesar(texto_criptografado, chave):
    texto_descriptografado = ""
    i = 0
    while i < len(texto_criptografado):
        char = texto_criptografado[i]
        
        # 97 = 'a', 65 = 'A'
        if 'a' <= char <= 'z':
            novo_ord = (ord(char) - 97 - chave) % 26 + 97
            texto_descriptografado += chr(novo_ord)
        elif 'A' <= char <= 'Z':
            novo_ord = (ord(char) - 65 - chave) % 26 + 65
            texto_descriptografado += chr(novo_ord)
        elif char == ' ':
            texto_descriptografado += ' '

        i += 1
    return texto_descriptografado

def obter_dados_diva(musica_dict, diva_name, eras_por_diva, musicas_por_era):

    total_streams = 0
    total_musicas = 0

    eras_da_diva = eras_por_diva.get(diva_name, ())
    
    for musica in musica_dict:
        streams = musica_dict[musica]
        era_da_musica = ""
        
        for era_nome in musicas_por_era:
            musicas = musicas_por_era[era_nome]
            
            j = 0
            encontrou_musica = False
            while j < len(musicas):
                if musica == musicas[j]:
                    encontrou_musica = True
                    j = len(musicas)
                j += 1

            if encontrou_musica:
                era_da_musica = era_nome

        k = 0
        era_pertence_a_diva = False
        while k < len(eras_da_diva):
            if era_da_musica == eras_da_diva[k]:
                era_pertence_a_diva = True
                k = len(eras_da_diva) 
            k += 1

        if era_pertence_a_diva:
            total_streams += streams
            total_musicas += 1
            
    return total_streams, total_musicas

def sort_divas_recursiva(divas_data, divas_nomes_restantes):

    if not divas_nomes_restantes:
        return {}

    melhor_diva = divas_nomes_restantes[0]
    i = 1
    while i < len(divas_nomes_restantes):
        diva = divas_nomes_restantes[i]

        data_melhor = divas_data[melhor_diva]
        data_atual = divas_data[diva]
        
        media_melhor = data_melhor['media']
        media_atual = data_atual['media']
        
        musicas_melhor = data_melhor['musicas']
        musicas_atual = data_atual['musicas']
        
        if media_atual > media_melhor:
            melhor_diva = diva
        elif media_atual == media_melhor:
            if musicas_atual > musicas_melhor:
                melhor_diva = diva
            elif musicas_atual == musicas_melhor:
                if diva < melhor_diva:
                    melhor_diva = diva
        i += 1

    novas_divas_restantes = ()
    k = 0
    while k < len(divas_nomes_restantes):
        diva_restante = divas_nomes_restantes[k]
        if diva_restante != melhor_diva:
            novas_divas_restantes += (diva_restante,)
        k += 1

    recursed_dict = sort_divas_recursiva(divas_data, novas_divas_restantes)
    
    sorted_dict = {melhor_diva: divas_data[melhor_diva]}
    sorted_dict.update(recursed_dict) 
    
    return sorted_dict

musicas_por_era = {
    "Future Nostalgia" : ("Future Nostalgia", "Don't Start Now", "Cool", "Physical", "Levitating", "Pretty Please", "Hallucinate", "Love Again", "Break My Heart", "Good in Bed", "Boys Will Be Boys", "Fever"),
    "Radical Optimism" : ("End of an Era", "Houdini", "Training Season", "These Walls", "Whatcha Doing", "French Exit", "Illusion", "Falling Forever", "Anything for Love", "Maria", "Happy for You"),
    "SOUR" : ("Brutal", "Traitor", "Drivers License", "1 Step Forward, 3 Steps Back", "Deja Vu", "Good 4 U", "Enough For You", "Happier", "Jealousy, Jealousy", "Favorite Crime", "Hope Ur Ok"),
    "GUTS" : ("All-American Bitch", "Bad Idea Right?", "Vampire", "Lacy", "Ballad Of A Homeschooled Girl", "Making The Bed", "Logical", "Get Him Back!", "Love Is Embarrassing", "The Grudge", "Pretty Isn't Pretty", "Teenage Dream"),
    "Teenage Dream" : ("Teenage Dream", "Last Friday Night (T.G.I.F.)", "California Gurls", "Firework", "Peacock", "Circle the Drain", "The One That Got Away", "E.T.", "Who Am I Living For?", "Pearl", "Hummingbird Heartbeat", "Not Like the Movies"),
    "Prism" : ("Roar", "Legendary Lovers", "Birthday", "Walking on Air", "Unconditionally", "Dark Horse", "This Is How We Do", "International Smile", "Ghost", "Love Me", "This Moment", "Double Rainbow", "By theGrace of God")
}

divas = ("Dua Lipa", "Olivia Rodrigo", "Katy Perry")
eras_nomes = ("Future Nostalgia", "Radical Optimism", "Prism", "Teenage Dream", "GUTS", "SOUR")
eras_por_diva = {
    "Dua Lipa": ("Future Nostalgia", "Radical Optimism"),
    "Olivia Rodrigo": ("GUTS", "SOUR"),
    "Katy Perry": ("Prism", "Teenage Dream")
}

print("Vai começar a disputa das DIVAS")

# parte 1
dados_musicas = {}
contagem_por_era = {"Future Nostalgia": 0, "Radical Optimism": 0, "Prism": 0, "Teenage Dream": 0, "GUTS": 0, "SOUR": 0}

entrada_fase1 = input()
while entrada_fase1 != "FIM":
    partes = entrada_fase1.split(' - ')
    
    if len(partes) == 4:
        musica = partes[0]
        diva = partes[1]
        era = partes[2]
        num_streams = int(partes[3])
        
        valido = True

        # verificacoes dos dados
        if era not in eras_nomes:
            print("Essa Era não esta na disputa, tente novamete!")
            valido = False
        elif musica not in musicas_por_era.get(era, ()):
            print('Essa musica não pertence a essa ERA, tente novamente!')
            valido = False
        elif diva not in divas or era not in eras_por_diva.get(diva, ()):
            print("Diva errada, tente novamente!")
            valido = False
        elif contagem_por_era.get(era, 0) == 3:
            print("Quantidade maxima de musicas dessa era atingida")
            valido = False
        elif musica in dados_musicas:
            print("A musica ja foi mencionada")
            valido = False
        
        # se a musica passou por todas as validacoes, guardmos os dados
        if valido:
            contagem_por_era[era] = contagem_por_era.get(era, 0) + 1
            dados_musicas[musica] = num_streams 
    
    entrada_fase1 = input()
        
if not dados_musicas:
    print("Essa batalha foi 'Houdini', sumiu! Sem músicas, sem disputa.")
else:
    # tratamento de dados pra determinar podio
    divas_data = {}
    i = 0
    while i < len(divas):
        diva_nome = divas[i]
        total_streams, total_musicas = obter_dados_diva(dados_musicas, diva_nome, eras_por_diva, musicas_por_era)
        
        media = 0
        if total_musicas > 0:
            media = total_streams // total_musicas
            
        divas_data[diva_nome] = {
            'streams': total_streams, 
            'musicas': total_musicas, 
            'media': media
        }
        i += 1
    
    # ordenacao e print do podio
    divas_ordenadas = sort_divas_recursiva(divas_data, divas)
    
    print("===== Pódio =====")
    posicao = 1
    diva_campea_fase1 = ""

    for diva_nome in divas_ordenadas:
        data = divas_ordenadas[diva_nome]
        print(f"{posicao}° {diva_nome} com {data['media']} Streams por música")
        if posicao == 1:
            diva_campea_fase1 = diva_nome
        posicao += 1

    # prints especificos de vitoria
    if diva_campea_fase1 == "Katy Perry":
        print("Katy Perry 'ruge'! Os KatyCats provam que 'Teenage Dream' e 'Prism' são eternos!")
    elif diva_campea_fase1 == "Olivia Rodrigo":
        print("É 'brutal' aqui! Os Livies mostraram a força de 'SOUR' e 'GUTS'.")
    elif diva_campea_fase1 == "Dua Lipa":
        print("Ela está 'Levitating', se voce não quer me ver ganhando, não aparece, não venha! Dua Lipa e seu 'Future Nostalgia' dominaram o pop.")

    # parte 2    
    votos_musica = {}
    musicas_validas_fase2 = 0
    
    entrada_fase2 = input()
    while entrada_fase2 != "FIM":
        partes = entrada_fase2.split(' - ')
        
        if len(partes) == 2:
            musica_voto = partes[0]
            diva_voto = partes[1]
            cantora_certa = False
            for era in eras_por_diva[diva_voto]:
                if musica_voto in musicas_por_era[era]:
                    cantora_certa = True
            
            # validacao da entrada
            if musica_voto not in dados_musicas or not cantora_certa:
                print("Essa musica não pertence ao catálogo, tente outra")
            else:
                # armazenando dados, se a entrada nao foi invalidada
                votos_musica[musica_voto] = votos_musica.get(musica_voto, 0) + 1
                musicas_validas_fase2 += 1
        
        entrada_fase2 = input()
            
    if musicas_validas_fase2 == 0:
        print('Nenhuma música foi mencionada, acho que no fim elas estão sem hype')
    else:
        # determinando musica campeã
        musica_campea = ""
        max_votos = -1
        diva_campea_musica = ""
        
        for musica in votos_musica:
            votos = votos_musica[musica]

            # encontra a diva da música
            diva_m = ""
            for d_nome in divas:
                d_eras = eras_por_diva.get(d_nome, ())
                i = 0
                while i < len(d_eras):
                    era_nome = d_eras[i]
                    musicas_era = musicas_por_era.get(era_nome, ())
                    
                    j = 0
                    encontrou_musica = False
                    while j < len(musicas_era):
                        if musica == musicas_era[j]:
                            encontrou_musica = True
                            j = len(musicas_era)
                        j += 1

                    if encontrou_musica:
                        diva_m = d_nome
                        i = len(d_eras)
                    i += 1

            # pega os dados da diva para desempate
            data_diva = divas_data.get(diva_m, {'media': 0, 'musicas': 0})
            
            # algoritmo de busca do máximo (simula ordenação com desempate)
            if votos > max_votos:
                max_votos = votos
                musica_campea = musica
                diva_campea_musica = diva_m
                
            elif votos == max_votos:
                # empate: critérios de desempate da parte 1
                data_atual = data_diva
                data_campea = divas_data[diva_campea_musica]

                # média de Streams (maior)
                if data_atual['media'] > data_campea['media']:
                    musica_campea = musica
                    diva_campea_musica = diva_m
                elif data_atual['media'] == data_campea['media']:
                    # total de Músicas (maior)
                    if data_atual['musicas'] > data_campea['musicas']:
                        musica_campea = musica
                        diva_campea_musica = diva_m
                    elif data_atual['musicas'] == data_campea['musicas']:
                        # ordem alfabética 
                        if diva_m < diva_campea_musica:
                            musica_campea = musica
                            diva_campea_musica = diva_m
                        
        print(f"E a música campeã foi {musica_campea}!")

        if diva_campea_musica == diva_campea_fase1:
            print(f"Domínio completo! {diva_campea_fase1} levou o pódio e a melhor música")
        else:
            # parte 3
            diva_nao_campea = ""
            i = 0
            while i < len(divas):
                d = divas[i]
                if d != diva_campea_fase1 and d != diva_campea_musica:
                    diva_nao_campea = d
                i += 1

            print(f"Apesar da {diva_campea_fase1} ter vencido no Pódio, a melhor música ficou com {diva_campea_musica}")
            print(f"Por isso teremos uma segunda chance para {diva_campea_musica}")
            print("A decisão será feita por votação popular, mas aparentemente faltou verba para o Spotify, pois os nomes vieram bagunçados, Quem será a Campeã?")

            votos_finais = {diva_campea_fase1: 0, diva_campea_musica: 0}
            frequent_fans = {diva_campea_fase1: {}, diva_campea_musica: {}} # {diva: {fan: count}}
            
            votos_validos_fase3 = 0

            fan_descriptografado = ""
            diva_descriptografada = ""
            while not (fan_descriptografado.upper() == diva_descriptografada.upper() == "FIM"):
                
                entrada_fase3 = input()
                partes = entrada_fase3.split(' - ')

                fan_cripto = partes[0]
                chave_fan = int(partes[1])
                diva_cripto = partes[2]
                chave_diva = int(partes[3])
                
                fan_descriptografado = cifra_de_cesar(fan_cripto, chave_fan)
                diva_descriptografada = cifra_de_cesar(diva_cripto, chave_diva)

                if not (fan_descriptografado.upper() == diva_descriptografada.upper() == "FIM"):
                    # validacao
                    if diva_descriptografada in votos_finais:
                        votos_finais[diva_descriptografada] = votos_finais.get(diva_descriptografada, 0) + 1

                        frequent_fans[diva_descriptografada][fan_descriptografado] = frequent_fans[diva_descriptografada].get(fan_descriptografado, 0) + 1
                        
                        print(f"Voto de {fan_descriptografado} computado para {diva_descriptografada}")
                        votos_validos_fase3 += 1
                
            if votos_validos_fase3 == 0:
                print("Aparentemente os Streams das duas foram comprados, a vencedora só pode ser a que não comprou nenhum voto")
                print(f"Parabéns {diva_nao_campea}, a campeã final!")
            else:
                vencedora_votos = ""
                
                votos_campea1 = votos_finais[diva_campea_fase1]
                votos_campea2 = votos_finais[diva_campea_musica]
                
                # desempate
                if votos_campea1 > votos_campea2:
                    vencedora_votos = diva_campea_fase1
                elif votos_campea2 > votos_campea1:
                    vencedora_votos = diva_campea_musica
                else:
                    # empate persistindo, usa criterios da fase 1
                    data1 = divas_data[diva_campea_fase1]
                    data2 = divas_data[diva_campea_musica]
                    
                    if data1['media'] > data2['media']:
                        vencedora_votos = diva_campea_fase1
                    elif data2['media'] > data1['media']:
                        vencedora_votos = diva_campea_musica
                    elif data1['media'] == data2['media']:
                        if data1['musicas'] > data2['musicas']:
                            vencedora_votos = diva_campea_fase1
                        elif data2['musicas'] > data1['musicas']:
                            vencedora_votos = diva_campea_musica
                        elif data1['musicas'] == data2['musicas']:
                            if diva_campea_fase1 < diva_campea_musica: # ordem alfabética
                                vencedora_votos = diva_campea_fase1
                            else:
                                vencedora_votos = diva_campea_musica
                                
                fan_data = frequent_fans[vencedora_votos]
                
                maior_fan = ""
                max_votos_fan = -1
                
                for fan_nome in fan_data:
                    fan_votos = fan_data[fan_nome]
                    if fan_votos > max_votos_fan:
                        max_votos_fan = fan_votos
                        maior_fan = fan_nome
                        
                print(f"A campeã final é {vencedora_votos}")
                print(f"E o(A) maior fã da diva {vencedora_votos} é {maior_fan}")