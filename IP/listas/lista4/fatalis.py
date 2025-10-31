# funcoes 
def analise_fatalis(acao, status):
    dano = 0
    if acao == "Ataque com Cauda":
        dano = 55
    elif acao == "Bola de Fogo":
        dano = 65
    elif acao == "Mar de Chamas Negras":
        for i in range(len(status)):
            if status[i] == "Desprotegido":
                dano = 1000
    return dano

def analise_cacador (acao, cacador, extrato=""):
    dano = 0
    if cacador == "Great Sword":
        if acao == "Golpe Carregado":
            dano = 165
        elif acao == "Corte Largo":
            dano = 120
        elif acao == "Divisor de Mundos":
            dano = 200
    elif cacador == "Fuzi_Arco":
        if acao == "Tiro Carregado":
            dano = 90
        elif acao == "Bala de Penetração":
            dano = 120
        elif acao == "Tiro Devastador":
            dano = 150
    elif cacador == "Glaive Inseto":
        if acao == "Corte Aéreo":
            dano = 100
        elif acao == "Descida Carregada:":
            dano = 120
        elif acao == "Kinseto":
            if extrato == "Vermelho":
                dano = 40
            elif extrato == "Amarelo":
                dano = 15
            elif extrato == "Verde":
                dano = 0 # cura
    return dano 
      

# variaveis
vidas_fatalis = 1800
lista_nomes = ["Great Sword", "Glaive Inseto", "Fuzi Arco"]
lista_vidas = [200, 200, 200]
lista_status = ["Desprotegido", "Desprotegido", "Desprotegido"]
rodada = 0
fatalis_morreu = False
num_eliminados = 0

# programa
print("Hora de Lutar contra a Historia!")
print()
while rodada < 4 and not fatalis_morreu and num_eliminados < 3:
    for j in range(3): # acoes dos cacadores
        if lista_status[j] != "Eliminado":
            acao = input()
            if lista_nomes.index(lista_nomes[j]) == 1 and acao == "Kinseto": # se o jogador for glaive inseto e a acao for kinseto
                extrato_do_kinseto = input()
                if extrato_do_kinseto == "Verde": # curando amigos, se eles estiverem no jogo ainda
                    if lista_status[0] != "Eliminado":
                        lista_vidas[0] += 40
                    if lista_status[2] != "Eliminado":
                        lista_vidas[2] += 40  
                dano = analise_cacador(lista_nomes[j], acao, extrato_do_kinseto)   
            else: 
                dano = analise_cacador(lista_nomes[j], acao)                 
            vidas_fatalis -= dano
    if not fatalis_morreu and num_eliminados<3:
        acao_fatalis = input()
        if acao_fatalis == "Mar de Chamas Negras":
            lista_status[0] = input()
            lista_status[1] = input()
            lista_status[2] = input()
        dano = analise_fatalis(acao_fatalis, lista_status)
        for i in range(len(lista_nomes)):
            if lista_vidas[i] > 0:
                lista_vidas[i] -= dano
            if lista_vidas[i] <= 0:
                lista_vidas[i] = 0
                lista_status[i] = "Eliminado"
                num_eliminados += 1
        if vidas_fatalis <= 0:
            fatalis_morreu = True
    rodada += 1

if fatalis_morreu:
    print("Eu não acredito, vocês conseguiram!")
    print("Obrigado caçadores! O mundo está salvo.")
else:
    print("O Fatalis conseguiu sobreviver ao combate...")
    print("O mundo corre perigo!")