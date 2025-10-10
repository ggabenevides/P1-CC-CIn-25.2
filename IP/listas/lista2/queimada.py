# definindo variaveis
num_front = 6
num_back = 6
mortos_front = 0
mortos_back = 0
local = "campo"

# input inicial
print("Serão 12 desenvolvedores defendendo a honra de seus lados do código! Que vença a melhor stack!")
atacante = str(input())
while atacante != "Front-End" and atacante != "Back-End":
    print("Entrada inválida!")
    atacante = str(input())

# loop principal
while num_front > 0 and num_back > 0:
    while atacante == "Front-End":
        defensor = "Back-End"
        resultado_ataque =str(input())
        while resultado_ataque != "acertou" and resultado_ataque != "errou":
            print("Entrada inválida!")
            resultado_ataque = str(input())
        if resultado_ataque == "acertou":
            print(f"{atacante} acertou um jogador!")
            num_back -= 1
            mortos_back += 1
            atacante = "Back-End"
            defensor = "Front-End"
            print(f"Back-End: {num_back} dev(s) em campo. | Front-End: {num_front} dev(s) em campo.")
            resultado_ataque =str(input()) #ataque do morto do outro time
            while resultado_ataque != "acertou" and resultado_ataque != "errou":
                print("Entrada inválida!")
                resultado_ataque = str(input())
            if resultado_ataque == "acertou": #morto do back volta
                print(f"O morto do {atacante} acertou um jogador!")
                mortos_back -= 1
                num_front -= 1
                mortos_front += 1
                atacante = "Front-End"
                defensor = "Back-End"
                print(f"Back-End: {num_back} dev(s) em campo. | Front-End: {num_front} dev(s) em campo.")
            else: 
                resultado_defesa = str(input())
                while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                    print("Entrada inválida!")
                    resultado_defesa = str(input()) 
                if resultado_defesa == "pegou":
                    atacante = "Front-End"
                else:
                    atacante = "Back-End"  
        else:
            if mortos_front == 0:
                atacante = "Back-End"
                defensor = "Front-End"
            else:
                resultado_defesa = str(input())
                while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                    print("Entrada inválida!")
                    resultado_defesa = str(input())
                if resultado_defesa == "pegou":
                    atacante = "Back-End"
                else: #ataque no morto
                    resultado_ataque =str(input())
                    while resultado_ataque != "acertou" and resultado_ataque != "errou":
                        print("Entrada inválida!")
                        resultado_ataque = str(input())
                    if resultado_ataque == "acertou":
                        print(f"O morto do {atacante} acertou um jogador!")
                        mortos_front -= 1
                        num_back -= 1
                        mortos_back += 1
                        print(f"Back-End: {num_back} dev(s) em campo. | Front-End: {num_front} dev(s) em campo.")
                        resultado_ataque =str(input()) #ataque do morto do outro time
                        while resultado_ataque != "acertou" and resultado_ataque != "errou":
                            print("Entrada inválida!")
                            resultado_ataque = str(input())
                        if resultado_ataque == "acertou": #morto do front volta
                            print(f"O morto do {atacante} acertou um jogador!")
                            mortos_front -= 1
                            num_back -= 1
                            mortos_back += 1
                            atacante = "Front-End"
                            defensor = "Back-End"
                            print(f"Back-End: {num_back} dev(s) em campo. | Front-End: {num_front} dev(s) em campo.")
                        else: 
                            resultado_defesa = str(input())
                            while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                                print("Entrada inválida!")
                                resultado_defesa = str(input()) 
                            if resultado_defesa == "pegou":
                                atacante = "Front-End"
                            else:
                                atacante = "Back-End" 
                    else:
                        resultado_defesa = str(input())
                        while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                            print("Entrada inválida!")
                            resultado_defesa = str(input()) 
                        if resultado_defesa == "pegou":
                            atacante = "Back-End"
                        else:
                            atacante = "Front-End"
    else: # atacante = back
        defensor = "Front-End"
        resultado_ataque =str(input())
        while resultado_ataque != "acertou" and resultado_ataque != "errou":
            print("Entrada inválida!")
            resultado_ataque = str(input())
        if resultado_ataque == "acertou":
            print(f"{atacante} acertou um jogador!")
            num_front -= 1
            mortos_front += 1
            atacante = "Front-End"
            defensor = "Back-End"
            print(f"Back-End: {num_back} dev(s) em campo. | Front-End: {num_front} dev(s) em campo.")
        else:
            if mortos_back == 0:
                atacante = "Front-End"
                defensor = "Back-End"
            else:
                resultado_defesa = str(input())
                while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                    print("Entrada inválida!")
                    resultado_defesa = str(input())
                if resultado_defesa == "pegou":
                    atacante = "Front-End"
                else: #ataque no morto
                    resultado_ataque =str(input())
                    while resultado_ataque != "acertou" and resultado_ataque != "errou":
                        print("Entrada inválida!")
                        resultado_ataque = str(input())
                    if resultado_ataque == "acertou":
                        print(f"O morto do {atacante} acertou um jogador!")
                        mortos_back -= 1
                        num_front -= 1
                        mortos_front += 1
                        print(f"Back-End: {num_back} dev(s) em campo. | Front-End: {num_front} dev(s) em campo.")
                    else:
                        resultado_defesa = str(input())
                        while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                            print("Entrada inválida!")
                            resultado_defesa = str(input()) 
                        if resultado_defesa == "pegou":
                            atacante = "Front-End"
                        else:
                            atacante = "Back-End"     
 
 # relatorio final
if num_front == 0:
    print(f"Vitória do Back-End! Restaram {num_back} devs ainda mantendo o servidor de pé!")
elif num_back == 0:
    print(f"Vitória do Front-End! Restaram {num_front} devs ainda segurando o layout!")
