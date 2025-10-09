# coletar dados
nome_item = str(input()).capitalize
valor_item = float(input())
responsavel_compra = str(input()).capitalize
tipo_evento = str(input()).capitalize

# regra de ouro da angela
if valor_item > 100:
    if responsavel_compra == "Angela":
        print("Compra Aprovada!")
        print("Apenas eu tenho discernimento para gastos desta magnitude.")
    else:
        print("Compra Reprovada!")
        print("Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!")

# regras por pessoa
if responsavel_compra == "Angela":
    print("Compra Aprovada!")
    print("Compra feita por mim, obviamente dentro dos padrões de excelência.")
elif responsavel_compra == "Michael":
    if valor_item <= 60:
        if nome_item == "Mágica" or nome_item == "Fantasia":
            print("Compra Reprovada!")
            print("O Comitê não financia frivolidades e palhaçadas, Michael.")
        else:
            print("Compra Aprovada!")
            print("Uma compra surpreendentemente sensata vinda do Michael. Suspeito.")
    elif valor_item > 60:
        print("Compra Aprovada com ressalvas!")
        if nome_item == "Natal":
            print("O espírito natalino de Michael é... excessivo. A nota será conferida.")
        elif nome_item == "Aniversário":
            print("Michael nunca gasta tanto nos aniversários dos funcionários, deve ser o dele!")

# regras por evento
if tipo_evento == "Halloween":
    if nome_item == "Abóbora" and valor_item <= 30:
        print("Compra Aprovada!")
        print("Uma abóbora de tamanho e custo razoáveis. Eficiente.")
    else:
        print("Compra Aprovada com ressalvas!")
        if nome_item == "Abóbora" and valor_item > 30:
            print("Por que uma abóbora precisa ser tão cara? Extravagância.")
        else:
            print("Decoração de Halloween... Tenho certeza que Phyllis exagerou de novo.")
elif tipo_evento == "Aniversário":
    if nome_item == "Bolo" and valor_item <= 40:
        print("Compra Aprovada!")
        print("Um bolo modesto para celebrar mais um ano de produtividade, parabéns!")
    elif nome_item == "Sorvete de Menta com Chocolate":
        print("Compra Reprovada!")
        print("Este sabor de sorvete é uma abominação e não entrará em meu evento.")
    else:
         print("Compra Aprovada!")
         print("Itens de aniversário devem ser práticos, não uma distração do trabalho.")

# demais casos
else:
    if valor_item > 50:
        print("Compra Aprovada com ressalvas!")
        print("Está dentro do orçamento, mas não quer dizer que não vou verificar!")
    else: 
        print("Compra Aprovada!")
        print("Esta compra não viola nenhum regulamento... por enquanto.")
    