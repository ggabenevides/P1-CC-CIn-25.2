print("RECEBA! É hoje que eu me torno o melhor dos melhores.")
num_treinos = int(input())
habilidade_luva = int(input())
sequencia_treinos = str(input())

# iterando sobre a string

i = 0
while habilidade_luva < 100 and i < num_treinos:

    #determinando qual é o tipo de partida, depois removendo ela da string para que a proxima informação a ser interpretada seja sempre a primeira
    if "Batida de Pênalti" in sequencia_treinos[0:16] and not "Batida de Pênalti" in sequencia_treinos[16:]:
        tipo_partida = "Batida de Pênalti"
        sequencia_treinos.remove("Batida de Pênalti-")
    elif "Batida de Falta" in sequencia_treinos[0:14] and not "Batida de Falta" in sequencia_treinos[14:]:
        tipo_partida = "Batida de Falta"
        sequencia_treinos.remove("Batida de Falta-")
    elif "Batida de Ataque" in sequencia_treinos[0:15] and not "Batida de Ataque" in sequencia_treinos[15:]:
        tipo_partida = "Batida de Ataque"
        sequencia_treinos.remove("Batida de Ataque-")

    #determinando quem é o goleiro
    if "Gabriel Vasconcelos" in sequencia_treinos[0:17] and not "Gabriel Vasconcelos" in sequencia_treinos[17:]:
        goleiro = "Gabriel Vasconcelos"
        sequencia_treinos.remove("Gabriel Vasconcelos-")
    elif "Neymar Jr" in sequencia_treinos[0:8] and not "Neymar Jr" in sequencia_treinos[8:]:
        goleiro = "Neymar Jr"
        sequencia_treinos.remove("Neymar Jr-")
    elif "Sérgio Soares" in sequencia_treinos[0:13] and not "Sérgio Soares" in sequencia_treinos[13:]:
        goleiro = "Sérgio Soares" 
        sequencia_treinos.remove("Sérgio Soares-")
    elif "IShowSpeed" in sequencia_treinos[0:9] and not "IShowSpeed" in sequencia_treinos[9:]:
        goleiro = "IShowSpeed"
        sequencia_treinos.remove("IShowSpeed-")
    elif "Rokenedy" in sequencia_treinos[0:7]  and not "Rokenedy" in sequencia_treinos[7:]:
        goleiro = "Rokenedy"
        sequencia_treinos.remove("Rokenedy-")
    else:
        habilidade_goleiro = int(input())
