# mensagem inicial
print("Bem-vindos ao Jimmy Jab!")

# informaçoes iniciais 
participante_1 =  str(input()).capitalize()
participante_2 = str(input()).capitalize()
participante_3 = str(input()).capitalize()
participante_4 = str(input()).capitalize()

if participante_1 == "Terry" or participante_1 == "Holt" or participante_2 == "Terry" or participante_2 == "Holt" or participante_3 == "Terry" or participante_3 == "Holt" or participante_4 == "Terry" or participante_4 == "Holt":
    print("Jimmy Jab CANCELADO!")
else:
    # bocatona
    print("Nosso primeiro evento é...")
    print("A Bocatona!")
    if participante_1 == "Scully" or participante_2 == "Scully" or participante_3 == "Scully" or participante_4 == "Scully":
        perdedor_bocatona = str(input()).capitalize()
        print("Scully leva a melhor, não tem como competir com ele.")
        print(f"{perdedor_bocatona} não avançou para a próxima fase!")
    else:
        vencedor_bocatona = str(input()).capitalize()
        perdedor_bocatona = str(input()).capitalize()
        print(f"{vencedor_bocatona} levou a melhor na Bocatona!")
        print(f"{perdedor_bocatona} não avançou para a próxima fase!")

    # comida volumosa
    print("O segundo evento é A corrida volumosa!")
    if perdedor_bocatona == participante_1:
        tempo_participante2 = int(input())
        tempo_participante3 = int(input())
        tempo_participante4 = int(input())
        if tempo_participante2 < tempo_participante3 and tempo_participante2 < tempo_participante4:
            vencedor_corrida = participante_2 
            finalista_1 = participante_2
            print(f"{vencedor_corrida} levou a melhor na Corrida Volumosa!")
            if tempo_participante3 <tempo_participante4:
                perdedor_corrida = participante_4
                finalista_2 = participante_3
            elif tempo_participante4 < tempo_participante3:
                perdedor_corrida = participante_3
                finalista_2 = participante_4
            print(f"{perdedor_corrida} não avançou para a próxima fase!")
        if tempo_participante3 < tempo_participante2 and tempo_participante3 < tempo_participante4:
            vencedor_corrida = participante_3 
            finalista_1 = participante_3
            print(f"{vencedor_corrida} levou a melhor na Corrida Volumosa!")
            if tempo_participante2 < tempo_participante4:
                perdedor_corrida = participante_4
                finalista_2 = participante_2
            elif tempo_participante4 < tempo_participante2:
                perdedor_corrida = participante_2
                finalista_2 = participante_4
            print(f"{perdedor_corrida} não avançou para a próxima fase!")
        if tempo_participante4< tempo_participante3 and tempo_participante4< tempo_participante2:
            vencedor_corrida = participante_4
            finalista_1 = participante_4
            print(f"{vencedor_corrida} levou a melhor na Corrida Volumosa!")
            if tempo_participante3 < tempo_participante2:
                perdedor_corrida = participante_2
                finalista_2 = participante_3
            elif tempo_participante2< tempo_participante3:
                perdedor_corrida = participante_3
                finalista_2 = participante_2
            print(f"{perdedor_corrida} não avançou para a próxima fase!")
    if perdedor_bocatona == participante_2:
        tempo_participante1= int(input())
        tempo_participante3= int(input())
        tempo_participante4 = int(input())
        if tempo_participante1< tempo_participante3 and tempo_participante1< tempo_participante4:
            vencedor_corrida = participante_1
            finalista_1 = participante_1
            print(f"{vencedor_corrida} levou a melhor na Corrida Volumosa!")
            if tempo_participante3 < tempo_participante4:
                perdedor_corrida = participante_4
                finalista_2 = participante_3
            elif tempo_participante4< tempo_participante3:
                perdedor_corrida = participante_3
                finalista_2 = participante_4
            print(f"{perdedor_corrida} não avançou para a próxima fase!")
        if tempo_participante3 < tempo_participante1 and tempo_participante3 < tempo_participante4:
            vencedor_corrida = participante_3
            finalista_1 = participante_3
            print(f"{vencedor_corrida} levou a melhor na Corrida Volumosa!")
            if tempo_participante1 < tempo_participante4:
                perdedor_corrida = participante_4
                finalista_2 = participante_1
            elif tempo_participante4 < tempo_participante1:
                perdedor_corrida = participante_1
                finalista_2 = participante_4
            print(f"{perdedor_corrida} não avançou para a próxima fase!")
        if tempo_participante4< tempo_participante3 and tempo_participante4<tempo_participante1:
            vencedor_corrida = participante_4
            finalista_1 = participante_4
            print(f"{vencedor_corrida} levou a melhor na Corrida Volumosa!")
            if tempo_participante3 < tempo_participante1:
                perdedor_corrida = participante_1
                finalista_2 = participante_3
            elif tempo_participante1< tempo_participante3:
                perdedor_corrida = participante_3
                finalista_2 = participante_1
            print(f"{perdedor_corrida} não avançou para a próxima fase!")
    if perdedor_bocatona == participante_3:
        tempo_participante1 = int(input())
        tempo_participante2 = int(input())
        tempo_participante4 = int(input())
        if tempo_participante2 < tempo_participante1 and tempo_participante2 < tempo_participante4:
            vencedor_corrida = participante_2 
            finalista_1 = participante_2
            print(f"{vencedor_corrida} levou a melhor na Corrida Volumosa!")
            if tempo_participante1 < tempo_participante4:
                perdedor_corrida = participante_4
                finalista_2 = participante_1
            elif tempo_participante4 < tempo_participante1:
                perdedor_corrida = participante_1
                finalista_2 = participante_4
            print(f"{perdedor_corrida} não avançou para a próxima fase!")
        if tempo_participante4 < tempo_participante1 and tempo_participante4 < tempo_participante2:
            vencedor_corrida = participante_4 
            finalista_1 = participante_4
            print(f"{vencedor_corrida} levou a melhor na Corrida Volumosa!")
            if tempo_participante2 < tempo_participante1:
                perdedor_corrida = participante_1
                finalista_2 = participante_2
            elif tempo_participante1 < tempo_participante2:
                perdedor_corrida = participante_2
                finalista_2 = participante_1
            print(f"{perdedor_corrida} não avançou para a próxima fase!")
        if tempo_participante1< tempo_participante2 and tempo_participante1< tempo_participante4:
            vencedor_corrida = participante_1
            finalista_1 = participante_1
            print(f"{vencedor_corrida} levou a melhor na Corrida Volumosa!")
            if tempo_participante4< tempo_participante2:
                perdedor_corrida = participante_2
                finalista_2 = participante_4
            elif tempo_participante2< tempo_participante4:
                perdedor_corrida = participante_4
                finalista_2 = participante_2
            print(f"{perdedor_corrida} não avançou para a próxima fase!")
    if perdedor_bocatona == participante_4:
        tempo_participante1 = int(input())
        tempo_participante2 = int(input())
        tempo_participante3 = int(input())
        if tempo_participante1 < tempo_participante3 and tempo_participante1 < tempo_participante2:
            vencedor_corrida = participante_1
            finalista_1 = participante_1
            print(f"{vencedor_corrida} levou a melhor na Corrida Volumosa!")
            if tempo_participante3 < tempo_participante2:
                perdedor_corrida = participante_2
                finalista_2 = participante_3
            elif tempo_participante2 < tempo_participante3:
                perdedor_corrida = participante_3
                finalista_2 = participante_2
            print(f"{perdedor_corrida} não avançou para a próxima fase!")
        if tempo_participante3 < tempo_participante2 and tempo_participante3 < tempo_participante1:
            vencedor_corrida = participante_3 
            finalista_1 = participante_3
            print(f"{vencedor_corrida} levou a melhor na Corrida Volumosa!")
            if tempo_participante2 < tempo_participante1:
                perdedor_corrida = participante_1
                finalista_2 = participante_2
            elif tempo_participante1<tempo_participante2:
                perdedor_corrida = participante_2
                finalista_2 = participante_1
            print(f"{perdedor_corrida} não avançou para a próxima fase!")
        if tempo_participante2< tempo_participante3 and tempo_participante2< tempo_participante1:
            vencedor_corrida = participante_2
            finalista_1 = participante_2
            print(f"{vencedor_corrida} levou a melhor na Corrida Volumosa!")
            if tempo_participante3 < tempo_participante1:
                perdedor_corrida = participante_1
                finalista_2 = participante_3
            elif tempo_participante1< tempo_participante3:
                perdedor_corrida = participante_3
                finalista_2 = participante_1
            print(f"{perdedor_corrida} não avançou para a próxima fase!")

    # mensagem final
    if (finalista_1 == "Jake" and finalista_2 == "Amy") or (finalista_1 == "Amy" and finalista_2 == "Jake"):
        print("Jake ficou com o 2º lugar!")
        print("Amy VENCEU O JIMMY JABS!")
    else:     
        vencedor_geral = str(input())
        if vencedor_geral == finalista_1:
            print(f"{finalista_2} ficou com o 2º lugar!")
            print(f"{vencedor_geral} VENCEU O JIMMY JABS!")
        elif vencedor_geral == finalista_2:
            print(f"{finalista_1} ficou com o 2º lugar!")
            print(f"{vencedor_geral} VENCEU O JIMMY JABS!")
