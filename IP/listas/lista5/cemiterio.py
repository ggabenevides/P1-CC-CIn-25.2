# funcao recursiva para calcular numero de formas de posicionar n almas no cemiterio
def calculo_possibilidades(matriz, ala_ocupada, lote_ocupado, possibilidades_atuais=0):
    n = len(matriz)
    
    ala_atual = 0
    encontrou_vazia = False
    i = 0
    while i < n and not encontrou_vazia:
        tem_alma = False
        j = 0
        while j < n and not tem_alma:
            if matriz[i][j] == "A":
                tem_alma = True
            j += 1
        
        if not tem_alma:
            ala_atual = i
            encontrou_vazia = True
        
        i += 1
        
    if not encontrou_vazia:
        ala_atual = n

    #Caso Base
    if ala_atual == n:
        return 1

    count = 0

    for lote in range(n):
        
        #Verificar se é o túmulo
        eh_tumulo = (ala_atual == ala_ocupada and lote == lote_ocupado)
        
        if not eh_tumulo:
            esta_seguro = True
            
            #Vertical
            lin = 0
            while lin < ala_atual and esta_seguro:
                if matriz[lin][lote] == "A":
                    esta_seguro = False
                lin += 1
            
            #diagonal
            lin = ala_atual - 1
            col = lote - 1
            while lin >= 0 and col >= 0 and esta_seguro:
                if matriz[lin][col] == "A":
                    esta_seguro = False
                lin -= 1
                col -= 1

            #outra diagonal
            lin = ala_atual - 1
            col = lote + 1
            while lin >= 0 and col < n and esta_seguro:
                if matriz[lin][col] == "A":
                    esta_seguro = False
                lin -= 1
                col += 1
            
            if esta_seguro:
                matriz[ala_atual][lote] = "A"
                
                # Recursão
                count += calculo_possibilidades(matriz, ala_ocupada, lote_ocupado, possibilidades_atuais)
                
                matriz[ala_atual][lote] = "L"

    return count

# programa principal
n = int(input())
matriz_espacial = []
for i in range(n):
    linha = ["L"] * n # L para espaço Livre
    matriz_espacial.append(linha)
ala_ocupada = int(input())
lote_ocupado = int(input())
 # O para espaço Inutilizavel
while ala_ocupada > n or lote_ocupado > n or ala_ocupada < 1 or lote_ocupado < 1:
    print(f"Rogério e Chaguinha não encontraram o túmulo ocupado na posição ({ala_ocupada}, {lote_ocupado}). Assim eles nunca vão conseguir sair do cemitério!") 
    ala_ocupada = int(input())
    lote_ocupado = int(input())
else: 
    print(f"Rogério e Chaguinha conseguiram encontrar o túmulo ocupado em ({ala_ocupada}, {lote_ocupado})!")
    total_possibilidades = calculo_possibilidades(matriz_espacial, ala_ocupada-1, lote_ocupado-1)
    print()
    print(f"Rogério e Chaguinha conseguiram encontrar {total_possibilidades} possíveis posições para as almas se posicionarem sem conflitos!")
    if total_possibilidades == 0:
        print("Não existe nenhuma configuração segura para as almas... Rogério e Chaguinha estão presos no meio da guerra das almas!")
    elif 1<=total_possibilidades<=10:
        print("Os amigos vão precisar tomar muito cuidado para não pegar um caminho errado!")
    elif 10 < total_possibilidades <= 50:
        print("Uau! São tantas opções que eles até se perderam contando!")
    elif total_possibilidades > 50:
        print("Em pleno Halloween e as almas descansando em paz! Rogério e Chaguinha vão conseguir sair logo do cemitério.")
