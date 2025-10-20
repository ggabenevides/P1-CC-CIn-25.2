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
    while local == "campo" and num_front>0 and num_back>0:
        resultado_ataque =str(input())
        while resultado_ataque != "acertou" and resultado_ataque != "errou":
            print("Entrada inválida!")
            resultado_ataque = str(input())
        if resultado_ataque == "acertou":
            if atacante == "Back-End":
                num_front -= 1
                mortos_front += 1
                local = "fora"
            else:
                num_back -=1
                mortos_back += 1
                local = "fora"
            print(f"{atacante} acertou um jogador!")
            print(f"Back-End: {num_back} dev(s) em campo. | Front-End: {num_front} dev(s) em campo.") 
            local = "fora"
            if atacante == "Back-End":
                atacante = "Front-End"
            else: 
                atacante = "Back-End"
        else:
            if atacante == "Back-End":
                if mortos_back == 0:
                    atacante = "Front-End"
                else:
                    resultado_defesa = str(input())
                    while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                        print("Entrada inválida!")
                        resultado_defesa = str(input()) 
                    if resultado_defesa == "pegou":
                        atacante = "Front-End"
                    else:
                        local = "fora"
            else:
                if mortos_front == 0:
                    atacante = "Back-End"
                else:
                    resultado_defesa = str(input())
                    while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                        print("Entrada inválida!")
                        resultado_defesa = str(input()) 
                    if resultado_defesa == "pegou":
                        atacante = "Back-End"
                    else:
                        local = "fora"
    while local == "fora" and num_back>0 and num_front>0:
        resultado_ataque =str(input())
        while resultado_ataque != "acertou" and resultado_ataque != "errou":
            print("Entrada inválida!")
            resultado_ataque = str(input())
        if resultado_ataque == "acertou":
            if atacante == "Front-End":
                if mortos_front>0:
                    mortos_front -= 1
                    num_front += 1
                num_back -= 1
                mortos_back += 1
            else: 
                if mortos_back>0:                
                    mortos_back -= 1
                    num_back += 1
                mortos_front += 1
                num_front -= 1
            print(f"O morto do {atacante} acertou um jogador!")
            print(f"Back-End: {num_back} dev(s) em campo. | Front-End: {num_front} dev(s) em campo.")
            if atacante == "Front-End":
                atacante = "Back-End"
            else:
                atacante = "Front-End"
            local = "fora"
        else:
            resultado_defesa = str(input())
            while resultado_defesa != "pegou" and resultado_defesa != "deixou":
                print("Entrada inválida!")
                resultado_defesa = str(input()) 
            if resultado_defesa == "pegou":
                if atacante == "Back-End":
                    atacante = "Front-End"
                    local = "campo"
                else:
                    atacante = "Back-End"
                    local = "campo"
            else:
                local = "campo"

 # relatorio final
if num_front == 0:
    print(f"Vitória do Back-End! Restaram {num_back} devs ainda mantendo o servidor de pé!")
elif num_back == 0:
    print(f"Vitória do Front-End! Restaram {num_front} devs ainda segurando o layout!")