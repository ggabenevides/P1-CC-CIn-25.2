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
            print(f"{diva} --- {divas[diva]['pontuacao']}")


def criando_nome (string, index_inicial):
    
    # se a string estiver vazia, retorna vazio
    if not string:
        return ""
    
    if index_inicial == 0:
        # primeiro nome
        index_espaco = string.find(' ')
        if index_espaco == -1: 
            # se não houver espaço (nome único), retorna a string inteira
            return string
        # retorna a substring do início (índice 0) até o primeiro espaço
        return string[:index_espaco]
    else:
        # último nome
        index_ultimo_espaco = string.rfind(' ')
        if index_ultimo_espaco == -1: 
            return string
        # retorna a substring do índice após o último espaço (+1) até o final
        return string[index_ultimo_espaco + 1:]


def identificando_nome_verdadeiro (divas_estadunidenses, diva):
    ultimo_nome = criando_nome(diva, -1)
    permutou = False
    for i in range(len(divas_estadunidenses)):
        # criando substring do nome sem usar split :(
        primeiro_nome = criando_nome(divas_estadunidenses[i], 0)
        # se o ultimo nome da diva for o primeiro nome de alguma das divas americanas, então a diva permutou o nome, e seu nome real tá na tupla
        if primeiro_nome == ultimo_nome:
            nome_real = divas_estadunidenses[i]
            permutou = True
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
            if dados[1] == "Brasil":
                pontuacao -= 50
                diva_americana_trapaceando = True
                dados[1] = "Estados Unidos"
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
divas_remanescentes = divas.copy() # essa biblioteca vai garantir que o mesmo duelo não aconteça duas vezes
vencedor = "ninguem"
duelo_aconteceu = False
for diva in divas:
    del divas_remanescentes[diva] # para que, caso a rival esteja na competição, o duelo não aconteca de novo
    pontuacao_diva = divas[diva]['pontuacao']
    rivais = conflitos.get(diva, "diva não tem rivais")
    if rivais != "diva não tem rivais":
        for rival in rivais:
            #checar se a rival tá jogando
            info_rival = divas_remanescentes.get(rival, "rival não está participando")
            if info_rival != "rival não está participando":
                pontuacao_rival = divas[rival]['pontuacao']
                duelo_aconteceu = True
                print(f"DRAMA! A rivalidade entre {diva} e {rival} vai ser resolvida no palco, AGORA!")
                # comparacao das pontuacoes 
                if pontuacao_diva == pontuacao_rival:
                    vencedor = "ninguem"
                    del divas[diva]
                    del divas[rival]
                    print(f"Eliminada(s): {diva}, {rival}")
                if pontuacao_diva > pontuacao_rival:
                    vencedor = diva
                    del divas[rival]
                    print(f"Eliminada(s): {rival}")
                elif pontuacao_diva < pontuacao_rival:
                    vencedor = rival
                    del divas[diva]
                    print(f"Eliminada(s): {diva}")

if not duelo_aconteceu:
    print("O palco estava montado. Os holofotes, ligados. Mas o conflito não apareceu. Fase 2 cancelada: as divas escolheram reinar em paz.")
else:
    print_placar_ordenado(divas, 2)



