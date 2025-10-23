lista_projetos = ["Memória ROM Simples", 
                  "Calculadora de 4 bits", 
                  "Sequenciador Musical", 
                  "Processador de 8 Bits", 
                  "Display de Vídeo 8x8", 
                  "Supercomputador V13"]
lista_componentes = [["Redstone", "Repetidores", "Tochas de Redstone"], 
                     ["Redstone", "Repetidores", "Tochas de Redstone", "Lâmpadas de Redstone"], 
                     ["Redstone", "Repetidores", "Blocos de Notas", "Observadores"],
                     ["Redstone", "Repetidores", "Lâmpadas de Redstone", "Pistões Aderentes"],
                     ["Redstone", "Repetidores", "Comparadores", "Pistões"],
                     ["Redstone", "Repetidores", "Comparadores", "Pistões Aderentes"]]
lista_quantidades = [[256, 64, 128],
                     [512, 128, 64, 256],
                     [1024, 256, 64, 128],
                     [4096, 1024, 2048, 512],
                     [2048, 512, 256, 128],
                     [8192, 2048, 1024, 1024]]
prints_componente = [['Mais redstone! A energia que move o progresso! (+{0} Redstone)' , 'Repetidores para garantir que o sinal chegue longe! Perfeito! (+{0} Repetidores)' , 'Tochas de Redstone! Ótimo para inverter um sinal ou energizar o sistema. (+{0} Tochas de Redstone)'] , 
                     ['Mais redstone! A energia que move o progresso! (+{0} Redstone)' , 'Repetidores para garantir que o sinal chegue longe! Perfeito! (+{0} Repetidores)' , 'Tochas de Redstone! Ótimo para inverter um sinal ou energizar o sistema. (+{0} Tochas de Redstone)' , 'Lâmpadas para o display! O resultado vai ficar bem visível. (+{0} Lâmpadas de Redstone)'] , 
                     ['Mais redstone! A energia que move o progresso! (+{0} Redstone)' , 'Repetidores para garantir que o sinal chegue longe! Perfeito! (+{0} Repetidores)' , 'Blocos de Notas! Quem sabe não rola uma musiquinha no final? (+{0} Blocos de Notas)' , 'Observadores a postos! Nenhuma atualização de bloco passará despercebida. (+{0} Observadores)'] , 
                     ['Mais redstone! A energia que move o progresso! (+{0} Redstone)' , 'Repetidores para garantir que o sinal chegue longe! Perfeito! (+{0} Repetidores)' , 'Lâmpadas para o display! O resultado vai ficar bem visível. (+{0} Lâmpadas de Redstone)' , 'Pistões Aderentes! Perfeitos para criar mecanismos retráteis. (+{0} Pistões Aderentes)'] , 
                     ['Mais redstone! A energia que move o progresso! (+{0} Redstone)' , 'Repetidores para garantir que o sinal chegue longe! Perfeito! (+{0} Repetidores)' , 'Comparadores para a lógica! A precisão é a alma do negócio. (+{0} Comparadores)' , 'Pistões para mover as coisas de lugar. Isso vai ser útil! (+{0} Pistões)'] , 
                     ['Mais redstone! A energia que move o progresso! (+{0} Redstone)', 'Repetidores para garantir que o sinal chegue longe! Perfeito! (+{0} Repetidores)' , 'Comparadores para a lógica! A precisão é a alma do negócio. (+{0} Comparadores)' , 'Pistões Aderentes! Perfeitos para criar mecanismos retráteis. (+{0} Pistões Aderentes)']]


lista_componentes_uteis = []
lista_quantidades_uteis = []
lista_componentes_inuteis = []
lista_quantidades_inuteis = []

projeto_in = str(input())
idx = lista_projetos.index(projeto_in)
dados = ""

quantidades_suficientes = False
todos_os_componentes = False

while not todos_os_componentes:
    elementos = []
    dados = input()

    while dados != "Construir!":

        elementos = dados.rsplit(maxsplit=1)

        if not elementos[0] in lista_componentes[idx]:
            lista_componentes_inuteis.append(elementos[0])
            lista_quantidades_inuteis.append(int(elementos[1]))
        else: # componente é util 
            if elementos[0] in lista_componentes_uteis:
                lista_quantidades_uteis[lista_componentes_uteis.index(elementos[0])] += int(elementos[1])
            else:
                lista_componentes_uteis.append(elementos[0])
                lista_quantidades_uteis.append(int(elementos[1]))  
            idx_elemento = lista_componentes[idx].index(elementos[0])

        if elementos[0] in lista_componentes[idx]:
            print(prints_componente[idx][idx_elemento].format(elementos[1]))
        else:
            print(f"Hmm, {elementos[0]} não parece ser útil para este projeto.")

        dados = input()

    # copiando lista na ordem da entrada pra o print final
    lista_componentes_uteis_entrada = lista_componentes_uteis.copy()
    lista_quantidades_uteis_entrada = lista_quantidades_uteis.copy()

    # ordenando componentes p comparar com lista fornecida 
    for componente in  lista_componentes[idx]:
        if componente in lista_componentes_uteis:
            quantidade = lista_quantidades_uteis[lista_componentes_uteis.index(componente)]
            idx_certo = lista_componentes[idx].index(componente)
            idx_errado = lista_componentes_uteis.index(componente)
            if idx_certo != idx_errado:
                lista_componentes_uteis.insert(idx_certo, componente)
                lista_componentes_uteis.pop(idx_errado+1)
                lista_quantidades_uteis.insert(idx_certo, quantidade)
                lista_quantidades_uteis.pop(idx_errado+1)

    for componente in  lista_componentes[idx]:
        if componente in lista_componentes_inuteis:
            quantidade = lista_quantidades_inuteis[lista_componentes_inuteis.index(componente)]
            idx_certo = lista_componentes[idx].index(componente)
            idx_errado = lista_componentes_inuteis.index(componente)
            if idx_certo != idx_errado:
                lista_componentes_inuteis.insert(idx_certo, componente)
                lista_componentes_inuteis.pop(idx_errado)
                lista_quantidades_inuteis.insert(idx_certo, quantidade)
                lista_quantidades_inuteis.pop(idx_errado)

    # verificando se a lista de componentes fornecidos contem todos os componentes necessários
    contagem = 0
    for componente in lista_componentes_uteis:
        if componente in lista_componentes[idx]:
            contagem += 1
    if len(lista_componentes[idx]) ==  contagem:
        todos_os_componentes = True

    contagem = 0
    if todos_os_componentes:
        
        for i in range(len(lista_quantidades[idx])):
            quantidade_exigida = lista_quantidades[idx][i]
            quantidade_fornecida = lista_quantidades_uteis[i]
            if quantidade_fornecida >= quantidade_exigida:
                contagem += 1

        if len(lista_quantidades[idx]) == contagem:
            quantidades_suficientes = True
        else:
          quantidades_suficientes = False

    else:
      quantidades_suficientes = False

    print()
    if todos_os_componentes:
        print(f"Viniccius13 conseguiu construir o {projeto_in}! Partiu programar!")
        print()
        print(f"Para construirmos a(o) {projeto_in}, utilizamos:")
        print()
        for componente in lista_componentes_uteis_entrada:
            print(f"{componente} : {lista_quantidades_uteis_entrada[lista_componentes_uteis_entrada.index(componente)]}")
        if lista_componentes_inuteis != []:
            print()
            print(f"Mas, em nossa jornada, também coletamos:")
            print()
            for componente in lista_componentes_inuteis:
                print(f"{componente} : {lista_quantidades_inuteis[lista_componentes_inuteis.index(componente)]}")
    else:
        print(f"Ainda não é possível construir o {projeto_in}! Faltam:")
        print()
        for componente in lista_componentes[idx]:
            if not componente in lista_componentes_uteis:
                packs_faltantes = lista_quantidades[idx][lista_componentes[idx].index(componente)] // 64
            else:
                qtde_faltando = (lista_quantidades[idx][lista_componentes[idx].index(componente)] - lista_quantidades_uteis[lista_componentes_uteis.index(componente)])
                if 0 < qtde_faltando < 64:
                    packs_faltantes = 1
                else:
                    packs_faltantes = qtde_faltando // 64
            if packs_faltantes < 0:
                packs_faltantes = 0
            if packs_faltantes > 0:
                print(f"{int(packs_faltantes)} pack(s) de {componente}")
        print()