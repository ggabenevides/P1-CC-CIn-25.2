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
while entrada != "FIM DAS INSCRIÇÕES.":
    entrada = input() 
    if entrada != "FIM DAS INSCRIÇÕES.":
        dados = entrada.split(" - ") #{nome_candidata} - {país} - {grammys} - {popularidade} - {shows_no_brasil}
        pontuacao = (dados[2]*15)+(dados[3]*10)+(dados[4]*5)   

        # identificar e corrigir nomes permutados 
        nome_corrigido = identificando_permutacoes(divas_estadunidenses, dados[0])
        if nome_corrigido in divas_estadunidenses:
            # pode ser que ela tenha tentado se disfarçar como brasileira
            if dados[1] == "Brasil":
                print(f"A CASA CAIU! A produção pegou {nome_corrigido} no pulo do gato tentando se livrar da penalidade! Por essa tentativa de malandragem, o preço veio dobrado")
                pontuacao -= 100
                divas[nome_corrigido] = ("Estados Unidos", dados[2], dados[3], dados[4], pontuacao) 
            # ou que ela seja a azealia banks tentando passar 
            if nome_corrigido == "Azealia Banks":
                print(f"Eita, climão! Parece que o histórico de polêmicas de {nome_corrigido} falou mais alto. A produção barrou a entrada e aqui ela não canta!")
        else:
            if dados[1] == "Brasil":
                pontuacao += 50
                print(f"ESSA TEM O TEMPERO BRASILEIRO! Por jogar em casa, {dados[0]} já larga com 50 pontos de vantagem.")
            divas[dados[0]] = (dados[1], dados[2], dados[3], dados[4], pontuacao) 
