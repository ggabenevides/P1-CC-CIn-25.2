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

lista_nomes = []
lista_notas_in = []
# input inicial 
contagem = 10
while contagem > 0:
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

# consideracoes iniciais do jamal
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
movimentos_print_monitor = [[[['. '], ['. '], ['. ']], [['. '], ['. '], ['. ']], [['E '], ['. '], ['D ']]], [], [], [], [], [], [], []]
matriz_vazia = [[['. '], ['. '], ['. ']], [['. '], ['. '], ['. ']], [['E '], ['. '], ['D ']]]
for i in range(1, 8):
    linha = int(movimentos[i-1][1])-1 
    coluna = int(movimentos[i-1][2])-1
    # falta ajeitar a posição do pe que fica parado
    matriz_vazia[linha][coluna].append(i)
    matriz_vazia[linha][coluna].remove(matriz_vazia[linha][coluna][0])
    movimentos_print_monitor.insert(i+1, matriz_vazia)

for i in range(len(movimentos_print_monitor)+1):
    print(f"'{pior_monitor} - Movimentação {i}:', ")
    for j in movimentos_print_monitor:
        idx_j = movimentos_print_monitor.index(j)
        for l in movimentos_print_monitor[idx_j]:
            idx_l = movimentos_print_monitor[idx_j].index(l)
            for c in movimentos_print_monitor[idx_j][idx_l]:
                print(c, end="")
            

# avaliando movimentos
num_acertos = 0
for i in range(len(movimentos)):
    if movimentos[i] == movimentos_ref[i]:
        num_acertos += 1

