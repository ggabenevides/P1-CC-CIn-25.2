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
    dados = str(input())

    if dados != "Construir!":

        elementos = dados.rsplit(maxsplit=1)

        if not elementos[0] in lista_componentes[idx]:
            print(f"Hmm, {elementos[0]} não parece ser útil para este projeto.")
            lista_componentes_inuteis.append(elementos[0])
            lista_quantidades_inuteis.append(int(elementos[1]))
        else: # componente é util 
            lista_componentes_uteis.append(elementos[0])
            lista_quantidades_uteis.append(int(elementos[1]))

        if elementos[0] in lista_componentes_uteis:
            if elementos[0] == "Redstone":
                print(f"Mais redstone! A energia que move o progresso! (+{elementos[1]} Redstone)")
            elif elementos[0] == "Repetidores":
                print(f"Repetidores para garantir que o sinal chegue longe! Perfeito! (+{elementos[1]} Repetidores)")
            elif elementos[0] == "Tochas de Redstone":
                print(f"Tochas de Redstone! Ótimo para inverter um sinal ou energizar o sistema. (+{elementos[1]} Tochas de Redstone)")
            elif elementos[0] == "Lâmpadas de Redstone":
                print(f"Lâmpadas para o display! O resultado vai ficar bem visível. (+{elementos[1]} Lâmpadas de Redstone)")    
            elif elementos[0] == "Bloco de Notas":
                print(f"Blocos de Notas! Quem sabe não rola uma musiquinha no final? (+{elementos[1]} Blocos de Notas)")
            elif elementos[0] == "Observadores":
                print(f"Observadores a postos! Nenhuma atualização de bloco passará despercebida. (+{elementos[1]} Observadores)")
            elif elementos[0] == "Comparadores":
                print(f"Comparadores para a lógica! A precisão é a alma do negócio. (+{elementos[1]} Comparadores)")
            elif elementos[0] == "Pistões":
                print(f"Pistões para mover as coisas de lugar. Isso vai ser útil! (+{elementos[1]} Pistões)")
            elif elementos[0] == "Pistões Aderentes":
                print(f"Pistões Aderentes! Perfeitos para criar mecanismos retráteis. (+{elementos[1]} Pistões Aderentes)")



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
        if componente == lista_componentes[idx][lista_componentes_uteis.index(componente)]:
            contagem += 1
    if len(lista_componentes[idx]) ==  contagem:
        todos_os_componentes = True

contagem = 0
for quantidade in lista_quantidades_uteis:
    if quantidade > lista_quantidades[idx][lista_quantidades_uteis.index(quantidade)] or quantidade == lista_quantidades[idx][lista_quantidades_uteis.index(quantidade)]:
        contagem += 1
if len(lista_quantidades[idx]) == contagem:
    quantidades_suficientes = True

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

    for componente in lista_componentes[idx]:
        if not componente in lista_componentes_uteis:
            packs_faltantes = lista_quantidades[idx][lista_componentes[idx].index(componente)] // 64
        else:
            packs_faltantes = (lista_quantidades[idx][lista_componentes[idx].index(componente)] - lista_quantidades_uteis[lista_componentes_uteis.index(componente)]) // 64
        if packs_faltantes == 0:
            packs_faltantes = 1
        elif packs_faltantes < 0:
            packs_faltantes = 0
        print(f"{packs_faltantes} pack(s) de {componente}")