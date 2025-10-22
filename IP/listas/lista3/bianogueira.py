influencers = ["Sofia Santino", "Doarda", "Ciclopin", "Bruna Pinheiro"]
cantores = ["Thiaguinho", "Neiff", "Veigh", "Mc Loma"]
convidados_confirmados = []
tutorial = ["Como a vida não precisa ser only fechos, a gente vai finalizar minha franja hoje:",
            "Essa chapinha eu dei literalmente tipo 50 reais nela. Não é a mais potente, não é a mais mais... mas ela é algo. Às vezes a gente só precisa ser algo, não precisa ser tudo.",
            "E o protetor térmico? Vei, a chapinha sabe que eu tô fazendo de coração, ela nunca queimaria meu cabelo.",
            "Espera esfriar e você vai barbarizar quando tiver pronto",
            "É isso, tchau meus amores"]
idx_tutorial = 0
pautas = ["Medo de ficar musculosa demais por causa da academia",
          "O cara que eu gosto não me quer, mas eu continuo insistindo. Acha que eu consigo algo?",
          "Meu chefe só me dá um dia de folga, mas eu precisava de dois.",
          "Pessoas que adoram se fazer de coitadinhas",
          "Essa história de que homem sofre calado"]
respostas_pautas = ["AMIGA, ouça: tem nem o P do PERIGO de você ficar grandona sem querer. Não se preocupe!",
                    "Claro que consegue, amiga! Consegue virar uma palhaça, consegue perder a autoestima... Consegue várias coisas :)",
                    "Tem que ter pelo menos dois dias de descanso. Se seu chefe tem uma empresa que não pode passar dois dias fechada porque vai quebrar, ele deveria fechar! Isso não é nem uma empresa, é um quiosque!",
                    "Eu detesto quem gosta de ficar pagando de coitadinho(a). Se for chorar… Na verdade, não chora não, que eu não quero nem ouvir.",
                    "Vocês ficam dizendo que homem sofre, que homem sofre calado… E por que eu ainda estou ouvindo? Por que eu ainda ouço???"]

cabosse = False
entrada = ""
while not cabosse: # loop das entradas 
    entrada = input()

    if entrada == "WhatsApp: 0 mensagens.":
        #ninguem confirmou ainda - tutorial
        print(tutorial[idx_tutorial])
        idx_tutorial += 1
        if idx_tutorial == len(tutorial):
            cabosse = True

    else: # alguem confirmou 
        if entrada == "CABOSSE! Bora simbora organizar essa festa.":
                cabosse = True
        else:
            dados = entrada.split(maxsplit=2)
            nome = dados[0]
            if nome == "Little Thiago":
                nome = "Thiaguinho"
            elif nome == "O Diferenciado":
                nome = "Neiff"
            #nome composto
            if dados[1] != "acabou":
                nome = dados[0] + " " + dados[1]
            convidados_confirmados.append(nome)

if cabosse and len(convidados_confirmados) == 0:
     # ninguem confirmou mesmo 
     print("I hate to tell you this BUT")
     print("Bia tava achando que ia fazer um mousse. O mousse virou uma piada, parceira")
else:
    # avaliando convidados confirmados 
    num_influencers = 0
    num_cantores = 0
    for nome in convidados_confirmados:
        if nome in influencers:
            num_influencers += 1
        elif nome in cantores:
            num_cantores += 1

    tarde_fofocas = False
    paredao = False
    festa_mista = False
    if num_influencers == len(convidados_confirmados):
        tarde_fofocas = True
    elif num_cantores == len(convidados_confirmados):
        paredao = True
    else:
        festa_mista = True
    
    # detalhe mc loma
    if "Mc Loma" in convidados_confirmados:
        convidados_confirmados.append("Mirella Santos")
        convidados_confirmados.append("Mariely Santos")

    # relatorios 
    if paredao:
        print("<PLANOS PARA FESTA>")
        frase_convidados = ", ".join(convidados_confirmados)
        print("Convidados: " + frase_convidados + ".")
        print("Tipo de comemoração: Paredão - Show na minha casa!!")
    elif festa_mista:
        print("Cachaçaria na minha casa hoje, 21h.")
        print("Todo mundo lá em casa! Tem que ser uma festa que dure muito, tipo 27 anos e 3 meses!!")
    elif tarde_fofocas:
        print("<TARDE DE FOFOCAS>")
        frase_convidados = ", ".join(convidados_confirmados)
        print("Convidados: " + frase_convidados + ".")
        pautas_in = []
        for i in range(len(convidados_confirmados)):
            pauta = input()
            pautas_in.append(pauta)
        for pauta in pautas_in:
            if pauta in pautas:
                idx = pautas.index(pauta)
                print(respostas_pautas[idx])
        qtde_amigos_concordam = int(input())
        if qtde_amigos_concordam == 0:
            print("Apois me interne, me prenda, me jogue fora que eu tô maluca!")
        else:
            print("É isso, eu vejo tanta coisa errada nesse mundo… Mas é como dizem, né?! Life snake, a vida cobra em inglês.")