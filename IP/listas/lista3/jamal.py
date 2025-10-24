# inicializando programa
monitores = ["Júnior", "Henrique", "Miguel", "Guilherme"]
movimentos_print = [['Jamal - Movimentação 0:', '. . .', '. . .', 'E . D'], 
                    ['Jamal - Movimentação 1:', '. 1 .', '. . .', 'E . .'],
                    ['Jamal - Movimentação 2:', '. . .', '. . .', 'E . 2'],
                    ['Jamal - Movimentação 3:', '. 3 .', '. . .', '. . D'],
                    ['Jamal - Movimentação 4:', '. . .', '. . .', '4 . D'],
                    ['Jamal - Movimentação 5:', '. 5 .', '. . .', 'E . .'],
                    ['Jamal - Movimentação 6:', '. D .', '. . .', '6 . .'],
                    ['Jamal - Movimentação 7:', '. 7 .', '. . .', 'E . .']]
movimentos_ref = ['D12', 'D33', 'E12', 'E31', 'D12', 'E31', 'D12']

print("Finalmente Jamal chega no CInbebeda, pronto pra causar, quando de repente…")
print('Jamal - "Que danado é isso?"')


# input inicial 
valido = False
segunda_chance = False
nomes_invalidos = True
acertou = False
while not valido:
    while nomes_invalidos:
        lista_nomes = []
        lista_notas_in = []
        contagem = 0
        entrada = input()
        dados = entrada.split(", ")
        for dado in dados:
            if dados.index(dado) % 2 == 0:
                lista_nomes.append(dado)
            else:
                lista_notas_in.append(int(dado))
        ja_apareceu = [] # o mesmo nome nao pode aparecer duas vezes
        contagem = 0 # contagem de entradas invalidas (nome aparece duas vezes ou não esta entre os monitores validos)
        for nome in lista_nomes:
            if nome in ja_apareceu:
                contagem += 1
            if nome in monitores:
                ja_apareceu.append(nome)
            else:
                contagem += 1
                print("Insira nomes válidos.")
        if contagem == 0:
            valido = True
            nomes_invalidos = False

    # consideracoes iniciais do jamal
    if not segunda_chance:
        melhor_nota = max(lista_notas_in)
        melhor_monitor = lista_nomes[lista_notas_in.index(melhor_nota)]
        pior_nota = min(lista_notas_in)
        pior_monitor = lista_nomes[lista_notas_in.index(pior_nota)]
        if melhor_nota == 10:
            print(f"O monitor {melhor_monitor} é diferenciado! Teve a aprovação do próprio Jamal.")
        print(f"Jamal avaliou a situação dos monitores e viu que {pior_monitor} é o mais necessitado.")
        print('Jamal - "Vou ensinar apenas uma vez, então preste atenção."')
        print()

        # print movimentos pra o monitor se inspirar
        for i in range(len(movimentos_print)):
            for j in range(len(movimentos_print[i])):
                print(movimentos_print[i][j])
            print()

    # entrada da movimentação dos pes
    numeros_validos = [ 1, 2, 3]
    entrada_valida = False
    while not entrada_valida:
        movimentacao_na_matriz = input()
        movimentos = movimentacao_na_matriz.split(", ")

        # avaliando entrada
        num_movimentos = 0
        letra_valida = 0
        numero_valido = 0
        for movimento in movimentos:
            num_movimentos += 1
            if movimento[0] == "E" or movimento[0] == "D":
                letra_valida += 1
            if int(movimento[1]) in numeros_validos and int(movimento[2]) in numeros_validos:
                numero_valido += 1
        if num_movimentos == 7 and numero_valido == 7 and letra_valida == 7:
            entrada_valida = True
        else:
            print("Movimento inválido! Por favor, insira outro.")

    # print movimentos do monitor 
    movimentos_print_monitor = [[['. ', '. ', '. '], ['. ', '. ', '. '], ['E ', '. ', 'D ']]]
    for matriz in range(1, 8):
        nova_matriz = []
        linha_passo = int(movimentos[matriz-1][1])-1 
        coluna_passo = int(movimentos[matriz-1][2])-1
        pe = movimentos[matriz-1][0]
        if matriz > 1:
            pe_anterior = movimentos[matriz-2][0]
        else:
            pe_anterior = ''
        for linha in range(3):
            nova_linha = []
            for coluna in range(3):
                # mesmo ponto na matriz anterior
                ponto_anterior = movimentos_print_monitor[matriz-1][linha][coluna]
                # passo atual
                if coluna == coluna_passo and linha_passo == linha:
                    nova_linha.append(f'{matriz} ')
                # passo anterior, se o pé mudou
                elif ponto_anterior.isnumeric() and pe != pe_anterior:
                    nova_linha.append(pe_anterior)
                # passo anterior, se o pé não mudou
                elif ponto_anterior.isnumeric() and pe == pe_anterior:
                    nova_linha.append('. ')
                # removendo o pe que se mexeu 
                elif ponto_anterior in ['E', 'D'] and ponto_anterior == pe:
                     nova_linha.append('. ')
                # 
                elif ponto_anterior in ['E', 'D'] and ponto_anterior != pe:
                    if pe == "E":
                        nova_linha.append("D")
                    else:
                        nova_linha.append("E")
                else:
                    nova_linha.append('. ')
            nova_matriz.append(nova_linha)
            
        movimentos_print_monitor.append(nova_matriz)

    for i in range(8):
        print(f"{pior_monitor} - Movimentação {i}:")
        for l in range(3):
            for c in range(3):
                if  c == 2:
                    print(movimentos_print_monitor[i][l][c])
                else:
                    print(movimentos_print_monitor[i][l][c], end="")
        print()
                
    # avaliando movimentos
    num_acertos = 0
    for i in range(len(movimentos)):
        if movimentos[i] == movimentos_ref[i]:
            num_acertos += 1

    # prints depois da apresentação do monitor
    if not segunda_chance:    
        if num_acertos == 6:
            segunda_chance = True
            valido = False 
            print("Foi quase! O monitor merece uma nova chance!")
        elif num_acertos == 7:
            acertou = True
            if pior_monitor == "Júnior":
                print("Uma máquina! Depois de horas vendo o passinho no Instagram ele conseguiu pegar mais rápido.")
            elif pior_monitor == "Guilherme":
                print("Ninguém nunca tinha visto ele dançar! Sabíamos que ele estava escondendo um dom.")
            elif pior_monitor == "Henrique":
                print("O maldito talento ataca novamente! Tinha que ser o desenrolado.")
            elif pior_monitor == "Miguel":
                        print("O cara veio do interior pra mostrar como que se faz!")
        elif num_acertos < 4:
            print(f"O monitor {pior_monitor} foi expulso da festa por não saber dançar.")
        elif num_acertos == 4:
            print("Isso tá horrível!")
        elif num_acertos == 5:
            print(f"Melhor o monitor {pior_monitor} deixar esse negócio de dança pra lá.")
    else:
        if num_acertos == 7:
            acertou = True
            print(f"Era isso! {pior_monitor} só estava precisando de um empurrãozinho.")
        else:
            print(f"Nem com outra tentativa {pior_monitor} conseguiu ajeitar isso.")

# convite final
if acertou:
    print('Jamal - "Vocês aprendem rápido! Quero que vocês dancem no meu próximo show!"')
    resposta = input()
    if resposta == "Sim":
        print(f"Óbvio que o monitor {pior_monitor} não perderia essa oportunidade por nada!")
    else:
        print(f"Infelizmente o monitor {pior_monitor} jogou essa oportunidade fora. Todos sabem que lá na frente ele vai se arrepender disso.")
else:
    print("Jamal desistiu de ensinar pra quem não aprende. Ele saiu em grande estilo, mandando o passinho e andando.")