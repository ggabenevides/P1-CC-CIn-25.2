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

    elif projeto == "Calculadora de 4 bits":
    elif projeto == "Sequenciador Musical":
    elif projeto == "Processador de 8 Bits":
    elif projeto == "Display de Vídeo 8x8":
    elif projeto == "Supercomputador V13":