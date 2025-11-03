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

def analise_greatsword (acao):
    dano = 0
    if acao == "Golpe Carregado":
        dano = 165
    elif acao == "Corte Largo":
        dano = 120
    elif acao == "Divisor de Mundos":
        dano = 200
    return dano 

def analise_fuziarco (acao):
    dano = 0
    if acao == "Tiro Carregado":
        dano = 90
    elif acao == "Bala de Penetração":
        dano = 120
    elif acao == "Tiro Devastador":
        dano = 150
    return dano 

def analise_glaiveinseto (acao, extrato=""):
    dano = 0
    if acao == "Corte Aéreo":
        dano = 100
    elif acao == "Descida Carregada":
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
lista_vidas = [200, 200, 200]
lista_status = ["Desprotegido", "Desprotegido", "Desprotegido"]
rodada = 0
fatalis_morreu = False
num_eliminados = 0

# programa
print("Hora de Lutar contra a Historia!")
print()
while rodada < 4 and not fatalis_morreu and num_eliminados < 3:
    if lista_status[0] != "Eliminado":
        acao = input()
        dano = analise_greatsword(acao)
        vidas_fatalis -= dano
    if lista_status[2] != "Eliminado":
        acao = input()
        if acao == "Kinseto":
            extrato_do_kinseto = input()
            if extrato_do_kinseto == "Verde": # curando amigos, se eles estiverem no jogo ainda
                if lista_status[0] != "Eliminado":
                    lista_vidas[0] += 40
                if lista_status[2] != "Eliminado":
                    lista_vidas[2] += 40  
            dano = analise_glaiveinseto(acao, extrato_do_kinseto)   
        else: 
            dano = analise_glaiveinseto(acao)                 
        vidas_fatalis -= dano
    if lista_status[1] != "Eliminado":
        acao = input()
        dano = analise_fuziarco(acao)
        vidas_fatalis -= dano   
    if vidas_fatalis <= 0:
        fatalis_morreu = True 
    if not fatalis_morreu and num_eliminados<3:
        acao_fatalis = input()
        if acao_fatalis == "Mar de Chamas Negras":
            lista_status[0] = input()
            lista_status[1] = input()
            lista_status[2] = input()
        dano = analise_fatalis(acao_fatalis, lista_status)
        for i in range(3):
            if lista_vidas[i] > 0:
                lista_vidas[i] -= dano
            if lista_vidas[i] <= 0:
                lista_vidas[i] = 0
                lista_status[i] = "Eliminado"
                num_eliminados += 1
    rodada += 1

if fatalis_morreu:
    print("Eu não acredito, vocês conseguiram!")
    print("Obrigado caçadores! O mundo está salvo.")
else:
    print("O Fatalis conseguiu sobreviver ao combate...")
    print("O mundo corre perigo!")