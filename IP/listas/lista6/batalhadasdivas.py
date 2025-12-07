# não pode usar lista nem comandos de acesso a biblioteca(keys, values, items) !

divas_estadunidenses = (
    'Olivia Rodrigo',
    'Sabrina Carpenter',
    'Beyoncé', 
    'Taylor Swift',   
    'Lady Gaga', 
    'Azealia Banks', 
    'Katy Perry', 
    'Madonna',
    'Ariana Grande',
    'Mariah Carey',
    'Whitney Houston',
    'Britney Spears',
    'Christina Aguilera',
    'Janet Jackson',
    'Cher',
    'Nicki Minaj',
    'Cardi B',
    'Doja Cat',
    'Billie Eilish')

conflitos = {
    'Katy Perry': ('Taylor Swift',),
    'Taylor Swift': ('Katy Perry', 'Ariana Grande', 'Olivia Rodrigo', 'Dua Lipa'),
    'Madonna': ('Lady Gaga',),
    'Lady Gaga': ('Madonna',),
    'Mariah Carey': ('Jennifer Lopez',),
    'Jennifer Lopez': ('Mariah Carey',),
    'Christina Aguilera': ('Britney Spears',),
    'Britney Spears': ('Christina Aguilera',),
    'Nicki Minaj': ('Doja Cat'),
    'Anitta': ('Ludmilla',),
    'Ludmilla': ('Anitta',),
    'Ariana Grande': ('Taylor Swift', 'Cynthia Erivo'),
    'Sabrina Carpenter': ('Camila Cabello', 'Olivia Rodrigo', 'Doja Cat'),
    'Camila Cabello': ('Sabrina Carpenter',),
    'Olivia Rodrigo': ('Taylor Swift', 'Sabrina Carpenter'),
    'Dua Lipa': ('Taylor Swift',),
    'Doja Cat': ('Nicki Minaj', 'Sabrina Carpenter'),}

def encontrar_posicao_chave(dicionario, chave_procurada):
    for indice, chave in enumerate(dicionario):
        if chave == chave_procurada:
            return indice

def sort_dict_recursiva(dicionario):
    # caso base
    if not dicionario:
        return {}
    
    dicionario_temp = dicionario.copy() 
    
    # encontra a chave com o maior valor
    max_key = max(dicionario_temp, key=lambda chave: dicionario_temp[chave]["pontuacao"])
    
    max_value = dicionario_temp.pop(max_key)
    
    # passo recursivo
    recursed_dict = sort_dict_recursiva(dicionario_temp)
    
    sorted_dict = {max_key: max_value}
    sorted_dict.update(recursed_dict) 
    
    return sorted_dict

def print_placar_ordenado(divas, fase):
    divas = sort_dict_recursiva(divas)
    if len(divas) > 0:
        print()
        print(f"=== PLACAR DA {fase}ª FASE ===")
        for diva in divas:
            print(f"{diva} --- {int(divas[diva]['pontuacao'])}")


def sao_permutacoes(str1, str2):

    if len(str1) != len(str2):
        return False

    contador1 = {}
    contador2 = {}

    
    for char in str1:
        
        contador1[char] = contador1.get(char, 0) + 1

    for char in str2:
        contador2[char] = contador2.get(char, 0) + 1

    return contador1 == contador2

def identificando_nome_verdadeiro (divas_estadunidenses, diva):
    permutou = False 
    ja_identificou = False
    for i in range(len(divas_estadunidenses)):
        if not ja_identificou:
            permutou = sao_permutacoes(divas_estadunidenses[i], diva)
            # se o ultimo nome da diva for o primeiro nome de alguma das divas americanas, então a diva permutou o nome, e seu nome real tá na tupla
            if permutou:
                nome_real = divas_estadunidenses[i]
                ja_identificou = True
            
    if not permutou: # se ela não permutou, então o nome fornecido já é o real
        nome_real = diva
    return nome_real

# fase 1
divas = {}
entrada = ""
print("A BATALHA DAS DIVAS começa... AGORA!")
print()
while entrada != "FIM DAS INSCRIÇÕES":
    entrada = input() 
    informacoes = {}
    if entrada != "FIM DAS INSCRIÇÕES":
        dados = entrada.split(" - ") #{nome_candidata} - {país} - {grammys} - {popularidade} - {shows_no_brasil}
        pontuacao = (int(dados[2])*15) + (int(dados[3])*10) + (int(dados[4])*5)  

        # flags dos prints após a fase de pontos
        acesso_negado = False
        diva_americana_trapaceando = False
        diva_apenas_americana = False
        diva_brasileira = False
        # identificar e corrigir nomes permutados 
        dados[0] = identificando_nome_verdadeiro(divas_estadunidenses, dados[0]) #sempre vai retornar o nome real da diva 

        # assinalar flags e candidatos que não vão poder se inscrever
        if dados[0] in divas_estadunidenses:
            pontuacao -= 50 # só por ser americana ela ja perde 50 pontos
            diva_apenas_americana = True
            # pode ser que ela tenha tentado se disfarçar como brasileira, perde 50 pontos além dos obrigatórios por ser americana
            if dados[1] != "EUA":
                pontuacao -= 50
                diva_americana_trapaceando = True
                dados[1] = "EUA"
            # ou que ela seja a azealia banks tentando passar; não sendo a azealia, ela pode entrar
            if dados[0] == "Azealia Banks":
                print(f"Eita, climão! Parece que o histórico de polêmicas de {dados[0]} falou mais alto. A produção barrou a entrada e aqui no Brasil ela não canta!")
                acesso_negado = True
        else:
            if dados[1] == "Brasil":
                pontuacao += 50
                diva_brasileira = True

        for chave in divas:
            if chave == dados[0]: # nome duplicado
                acesso_negado = True
                print(f"Só pode ter uma {dados[0]} na arena. Inscrição duplicada negada!")

        # apos todas as verificacoes, efetuando inscricao 
        if not acesso_negado:
            informacoes["informacoes gerais"] = dados[1], dados[2], dados[3], dados[4]
            informacoes["pontuacao"] = pontuacao 
            divas[dados[0]] = informacoes # cada diva tem uma biblioteca interna na biblioteca geral, pra que seja possivel alterar a pontuacao sem usar listas

            # prints
            print(f"{dados[0]} acaba de entrar na Batalha das Divas!")
            if diva_apenas_americana and not diva_americana_trapaceando:
                print(f'Por excesso de "estrelas e listras", {dados[0]} recebe uma penalidade de 50 pontos.')
            elif diva_brasileira:
                print(f"ESSA TEM O TEMPERO BRASILEIRO! Por jogar em casa, {dados[0]} já larga com 50 pontos de vantagem.")
            elif diva_americana_trapaceando:
                print(f"A CASA CAIU! A produção pegou {dados[0]} no pulo do gato tentando se livrar da penalidade! Por essa tentativa de malandragem, o preço veio dobrado.")
else:
    print_placar_ordenado(divas, 1)
    print()

# fase 2
divas = sort_dict_recursiva(divas)
if len(divas)>0:
    divas_remanescentes = divas.copy() # essa biblioteca vai garantir que o mesmo duelo não aconteça duas vezes
    duelos = {}
    duelo_aconteceu = False
    for diva in divas:
        diva_eliminada = False
        del divas_remanescentes[diva] # para que, caso a rival esteja na competição, o duelo não aconteca de novo
        pontuacao_diva = divas[diva]['pontuacao']
        rivais = conflitos.get(diva, "diva não tem rivais")
        if rivais != "diva não tem rivais":
            for rival in rivais:
                #checar se a rival tá jogando
                if not diva_eliminada:
                    info_rival = divas_remanescentes.get(rival, "rival não está participando")
                    if info_rival != "rival não está participando":
                        pontuacao_rival = divas[rival]['pontuacao']
                        duelo_aconteceu = True
                        # comparacao das pontuacoes 
                        if pontuacao_diva == pontuacao_rival:
                            duelos[(diva, rival)] = (diva, rival) # chave = duelo, valor = eliminada(s)
                            diva_eliminada = True
                        if pontuacao_diva > pontuacao_rival:
                            duelos[(diva, rival)] = (rival,)
                        elif pontuacao_diva < pontuacao_rival:
                            duelos[(diva, rival)] = (diva,)
                            diva_eliminada = True
                            
    # prints da fase 2
    if not duelo_aconteceu:
        print("O palco estava montado. Os holofotes, ligados. Mas o conflito não apareceu. Fase 2 cancelada: as divas escolheram reinar em paz.")
        print()
    else:
        print("SALTO ALTO NO TABLADO! HORA DO DUELO!")
        for duelo in duelos:
            diva = duelo[0]
            rival = duelo[1]
            print(f"DRAMA! A rivalidade entre {diva} e {rival} vai ser resolvida no palco, AGORA!")
            if len(duelos[duelo]) == 1:
                print(f"Eliminada(s): {duelos[duelo][0]}")
                del divas[duelos[duelo][0]]
            else:
                print(f"Eliminada(s): {duelos[duelo][0]} e {duelos[duelo][1]}")
                del divas[duelos[duelo][0]]
                del divas[duelos[duelo][1]]            
        print_placar_ordenado(divas, 2)
        print()

# fase 3
divas = sort_dict_recursiva(divas)
if len(divas) > 0:
    gaga_presente = False
    bey_presente = False
    anitta_presente = False

    gaga_condicao = False
    bey_condicao = False
    anitta_condicao = False

    for diva in divas:
        if diva == 'Lady Gaga':
            gaga_presente = True
        elif diva == 'Beyoncé':
            bey_presente = True
        elif diva == 'Anitta':
            anitta_presente = True

    if gaga_presente:
        if encontrar_posicao_chave(divas, 'Lady Gaga') not in (0, 1, 2): # condicao p habilidade ser ativada
            gaga_condicao = True
            menor_pontuacao = min(divas, key=lambda chave: divas[chave]["pontuacao"])
            if menor_pontuacao != 'Lady Gaga' and (int(divas[menor_pontuacao]['pontuacao']) <= int(divas['Lady Gaga']['pontuacao'])*1.25):
                # sucesso
                divas['Lady Gaga']['pontuacao'] += int(divas[menor_pontuacao]['pontuacao'])
                del divas[menor_pontuacao]
                resultado_gaga =  f'ARRASOU! O blefe de Lady Gaga funcionou! Ela enganou os jurados com seu "Poker Face" e roubou a cena de {menor_pontuacao}!'
            else:
                # falha
                del divas['Lady Gaga']
                resultado_gaga = 'QUE REVIRAVOLTA! O público não caiu no "Poker Face" de Lady Gaga! A farsa foi descoberta e ela está eliminada!'

    if bey_presente:
        if len(divas) >= 3:
            bey_condicao = True
            divas_temp = divas.copy()
            menor_pontuacao1 = min(divas_temp, key=lambda chave: divas[chave]["pontuacao"])
            del divas_temp[menor_pontuacao1]
            menor_pontuacao2 = min(divas_temp, key=lambda chave: divas[chave]["pontuacao"])
            if divas[menor_pontuacao1]['pontuacao'] + divas[menor_pontuacao2]['pontuacao'] <= divas['Beyoncé']['pontuacao']:
                acrescimo1 = divas[menor_pontuacao1]['pontuacao']*0.1
                acrescimo2 = divas[menor_pontuacao2]['pontuacao']*0.1
                divas[menor_pontuacao1]['pontuacao'] += acrescimo1
                divas[menor_pontuacao2]['pontuacao'] += acrescimo2
                divas['Beyoncé']['pontuacao'] += acrescimo1 + acrescimo1
                resultado_bey = 'PAREM TUDO! Queen Bey ativou a "Formation"! Ela reorganizou o jogo, elevou as novatas e saiu ainda mais forte!'
            else:
                del divas['Beyoncé']
                resultado_bey = 'CHOQUE! A estratégia de Beyoncé foi ousada demais! A "Formation" não convenceu e ela foi desclassificada por manipulação!'

    if anitta_presente:
        if encontrar_posicao_chave(divas, 'Anitta') != 0:
            maior_pontuacao = max(divas, key=lambda chave: divas[chave]["pontuacao"])
            anitta_condicao = True
            if int(divas['Anitta']['informacoes gerais'][2]) >= int(divas[maior_pontuacao]['informacoes gerais'][2])*0.9:
                acrescimo = (divas[maior_pontuacao]['pontuacao'] - divas['Anitta']['pontuacao'])*0.25
                divas[maior_pontuacao]['pontuacao'] -= acrescimo
                divas['Anitta']['pontuacao'] += acrescimo
                resultado_anitta = f'A PATROA TÁ ON! Anitta usou "Envolver" e fez {maior_pontuacao} dançar conforme sua música, virando o placar a seu favor!'
            else:
                divas['Anitta']['pontuacao'] -= 75
                resultado_anitta = 'DEU RUIM! A tentativa de "Envolver" de Anitta não funcionou! A jogada foi arriscada e o público não comprou a ideia.'

    # prints fase 3
    if not gaga_condicao and not bey_condicao and not anitta_condicao:
        print("Silêncio no palco... Nenhuma habilidade especial foi ativada.")
        print()
    else:
        print("O PALCO VAI TREMER! HORA DAS JOGADAS ESPECIAIS!")
        if gaga_presente and gaga_condicao:
            print(resultado_gaga)
        if bey_condicao and bey_condicao:
            print(resultado_bey)
        if anitta_presente and anitta_condicao:
            print(resultado_anitta)
        print_placar_ordenado(divas, 3)
        print()

# resultado final
taylor_presente = False
if len(divas) > 0:
    vencedora = max(divas, key=lambda chave: divas[chave]["pontuacao"])
    # checando empates e desempatando
    for diva in divas:
        if diva != vencedora and divas[diva]['pontuacao'] == divas[vencedora]['pontuacao']:
            if divas[diva]['informacoes gerais'][2] > divas[vencedora]['informacoes gerais'][2]:
                vencedora = diva
            elif divas[diva]['informacoes gerais'][2] == divas[vencedora]['informacoes gerais'][2]:
                if diva < vencedora:
                    vencedora = diva
    # prints vencedora
    print('=== HABEMUS DIVAM! ===')
    print('A GUERRA ACABOU! A nova dona do palco, a chefe do Réveillon, a única... é ELA!')
    for diva in divas:
        if diva == 'Taylor Swift':
            taylor_presente = True
    if taylor_presente and encontrar_posicao_chave(divas, 'Taylor Swift') in (1, 2): # se a taylor está no top 3 mas não é a vencedora
        print(f'PARABÉNS, {vencedora[0:3].upper()}... TAYLOR SWIFT!!!')
        print('MAS O QUE É ISSO?! Uma reviravolta de última hora! O conselheiro Filipe Moreira acaba de invadir a sala de controle! Alegando fazer parte de uma "comissão cinterna" de Swifties, ele anulou o resultado final e declarou que a verdadeira Era do Réveillon pertence à Taylor Swift! O show está garantido... e a rainha dele também!')
    else:
        print(f'PARABÉNS, {vencedora.upper()}!!! O Rei pode descansar em paz (no gelo), pois o show está garantido!')
        
else:
    print('INACREDITÁVEL! A Batalha das Divas terminou em caos, sem nenhuma vencedora! O palco está vazio... MAS O CALOR DA BRIGA FEZ O IMPOSSÍVEL! O Rei descongelou, subiu ao palco, olhou para a confusão e disse:')
    print('Obrigado pela ajuda, meninas, mas o show já tem atração... e Esse Cara Sou Eu.')
    print('O RÉVEILLON ESTÁ SALVO!')
