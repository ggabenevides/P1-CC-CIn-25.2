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

def criando_nome (string, index_inicial):
    nome = ""
    if index_inicial == 0:
        j = 0
        letra = string[j]
        while letra != " ":
            letra = string[j]
            if letra != " ":
                nome += string[j]
                j += 1
        return nome
    else:
        nome_inverso = ""
        j = len(string) - 1
        letra = string[j]
        while letra != " ":
            letra = string[j]
            if letra != " ":
                nome_inverso += letra
                j -= 1

        nome_str = ""
        k = len(nome_inverso) - 1
        while k >= 0:
            nome_str += nome_inverso[k]
            k -= 1
        return nome_str

def identificando_permutacoes (divas_estadunidenses, diva):
    ultimo_nome = criando_nome(diva, -1)
    flag = False
    for i in range(len(divas_estadunidenses)):
        # criando permutacao do nome sem usar split :(
        primeiro_nome = criando_nome(divas_estadunidenses[i], 0)
        if primeiro_nome == ultimo_nome:
            nome_real = divas_estadunidenses[i]
            flag = True
    if not flag:
        nome_real = diva
    return nome_real

# fase 1
divas = {}
entrada = ""

# flags dos prints após a fase de pontos
acesso_negado = False
diva_americana_trapaceando = False
diva_apenas_americana = False
diva_brasileira = False

print("A BATALHA DAS DIVAS começa... AGORA!")
while entrada != "FIM DAS INSCRIÇÕES.":
    entrada = input() 
    if entrada != "FIM DAS INSCRIÇÕES.":
        dados = entrada.split(" - ") #{nome_candidata} - {país} - {grammys} - {popularidade} - {shows_no_brasil}
        pontuacao = (dados[2]*15)+(dados[3]*10)+(dados[4]*5)   

        # identificar e corrigir nomes permutados 
        dados[0] = identificando_permutacoes(divas_estadunidenses, dados[0]) #sempre vai retornar o nome real da diva 

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
            divas[dados[0]] = (dados[1], dados[2], dados[3], dados[4], pontuacao)
            print(f"{dados[0]} acaba de entrar na Batalha das Divas!")
            if diva_apenas_americana and not diva_americana_trapaceando:
                print(f'Por excesso de "estrelas e listras", {dados[0]} recebe uma penalidade de 50 pontos.')
            elif diva_brasileira:
                print(f"ESSA TEM O TEMPERO BRASILEIRO! Por jogar em casa, {dados[0]} já larga com 50 pontos de vantagem.")
            elif diva_americana_trapaceando:
                print(f"A CASA CAIU! A produção pegou {dados[0]} no pulo do gato tentando se livrar da penalidade! Por essa tentativa de malandragem, o preço veio dobrado.")
