componentes_rom = ["Repetidores", "Redstone", "Tochas de Redstone"]
componentes_calc4bits = ["Repetidores", "Redstone", "Tochas de Redstone", "Lâmpadas de Redstone"]
componentes_sequenc = ["Redstone", "Repetidores", "Blocos de Notas", "Observadores"]
componentes_proc8bits = ["Repetidores", "Redstone", "Pistões Aderentes", "Lâmpadas de Redstone"]
componentes_display8x8 = ["Redstone", "Repetidores", "Comparadores", "Pistões"]
componentes_supercomp = ["Redstone", "Repetidores", "Comparadores", "Pistões Aderentes"]

lista_componentes = []
lista_quantidades = []

projeto = str(input())
dados = ""

while dados != "Construir!":
    elementos = []
    dados = str(input())
    elementos = dados.split('')
    lista_componentes.append(elementos[0])
    lista_quantidades.append(elementos[1])

    if projeto == "Memória ROM Simples":
        if not elementos[0] in componentes_rom:
            print(f"Hmm, {elementos[0]} não parece ser útil para este projeto.")
    elif projeto == "Calculadora de 4 bits":
        if not elementos[0] in componentes_calc4bits:
            print(f"Hmm, {elementos[0]} não parece ser útil para este projeto.")
    elif projeto == "Sequenciador Musical":
        if not elementos[0] in componentes_sequenc:
            print(f"Hmm, {elementos[0]} não parece ser útil para este projeto.")
    elif projeto == "Processador de 8 Bits":
        if not elementos[0] in componentes_proc8bits:
            print(f"Hmm, {elementos[0]} não parece ser útil para este projeto.")
    elif projeto == "Display de Vídeo 8x8":
        if not elementos[0] in componentes_display8x8:
            print(f"Hmm, {elementos[0]} não parece ser útil para este projeto.")
    elif projeto == "Supercomputador V13":
        if not elementos[0] in componentes_supercomp:
            print(f"Hmm, {elementos[0]} não parece ser útil para este projeto.")

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

print()

conseguiu = False
contagem_componentes = 0
contagem_quantidades = 0
for i in range(len(lista_componentes)):
    