entrada = ""
exigencias = {}

while entrada != "MIMOS RECEBIDOS": # armazenando exigencias da diva
    entrada = input()

    # tratando dados
    if entrada != "MIMOS RECEBIDOS":
        entrada = entrada.split(": ")
        categoria = entrada[0]
        item = entrada[1]
        quantidade = int(entrada[2])

        # caso especial da diva 
        if item == "latte":
            quantidade += 1

        # adicionando a biblioteca de exigencias 
        tupla = (item, quantidade)
        exigencias[categoria] = tupla

else: # reabastecimento
    while entrada != "ACABOU, a Glinda está pronta!":
        entrada = input()
        if entrada != "ACABOU, a Glinda está pronta!":
            entrada = entrada.split(" ")
            categoria_recebida = entrada[5]

            flag_chave_existente = exigencias.get(categoria_recebida, "chave inexistente")

            if flag_chave_existente != "chave inexistente":
                tupla_exigencia = exigencias[categoria_recebida] # (item, quantidade)
                quantidade_recebida = int(entrada[1])
                item_recebido = entrada[-1][:-1] 

                # lógica de estoque 
                exigencias.update({categoria_recebida : (item_recebido, tupla_exigencia[1] - quantidade_recebida)})

    else:
        # relatorio final
        print("Relatório de Balanço Final:")

        categorias = tuple(exigencias.keys())
        for i in range(len(categorias)):
            if exigencias[categorias[i]][1] <= 0:
                frase = "Você entregou TUDO! O mimo tá mais que garantido."
            else: 
                frase = f"Golpe BAIXÍSSIMO! Faltam {exigencias[categorias[i]][1]} mimos. Corre!"
            print(f"Categoria: {categorias[i]} Item: {exigencias[categorias[i]][0]} Status: {frase}")
        # checagens especificas
        print()

        flag_maquiagem = exigencias.get("Maquiagem", "chave inexistente")
        if flag_maquiagem != 'chave inexistente':
            if exigencias['Maquiagem'][0] == "Gloss":
                if exigencias["Maquiagem"][1] <= 0:
                    print("TUDO! O Gloss tá on. O look de Glinda tá salvo!")
                else:
                    print("CADÊ meu gloss? Como divarei? ... A Glinda tá chorando de raiva!")

        flag_bebidas = exigencias.get("Bebidas", "chave inexistente")
        if flag_bebidas != "chave inexistente":
            if exigencias['Bebidas'][0] == "latte":
                if exigencias["Bebidas"][1] <= 0:
                    print("Latte gelado pronto! A voz de Glinda está salva. Pode vir o próximo take")
                else:
                    print("Cadeia neles! Faltou o Mimo Sagrado. Essa equipe tá perdida!")   

        # veredito da diva
        num_estoque_neg = 0
        print()
        print("Veredito Final")    
        for i in range(len(categorias)):
            if exigencias[categorias[i]][1] > 0:
                num_estoque_neg += 1 

        if num_estoque_neg >= 3:
            print("Thank U, Next! A equipe de camarim foi demitida!")
        else:
            print("Estoque Aprovado! Glinda vai brilhar em Wicked!")
