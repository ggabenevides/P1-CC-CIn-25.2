# coleta de dados
casos = int(input())
dias = int(input())
assistências_casos = int(input())
operações_campo = int(input())
operação_especial = str(input()).capitalize()
tipo_operação_especial = ""
if operação_especial == "Sim":
    tipo_operação_especial = str(input()).capitalize()
localização = str(input()).capitalize()

# cálculo da pontuação
pontuação = casos*2 + assistências_casos*1.5 + operações_campo*0.5
if operação_especial == "Sim":
    if tipo_operação_especial == "Infiltração":
        pontuação = pontuação*1.5
    elif tipo_operação_especial == "Escuta":
        pontuação = pontuação*1.3
    elif tipo_operação_especial == "Invasão":
        pontuação = pontuação*1.2
    elif tipo_operação_especial == "Nenhuma das anteriores":
        pontuação = pontuação*1.1

# relatório 
if localização != "Brooklyn" and localização != "Manhattan":
    print("Os casos não são nas áreas designadas por Holt. Peralta está desclassificado!")
else:
    print("Pelo menos nos bairros corretos Jake está!")
    if casos < 20:
        print("Vishh, Jake já foi eliminado por não ter o mínimo de casos necessários.")
    else:
        print ("Detetive Peralta bateu o mínimo de casos, ele ainda está dentro da competição.")
        if (casos/dias) < 0.5:
            print("A média diária de casos tá muito baixa, Peralta foi desclassificado.") 
        else: 
            print("Parece que Jake é bem consistente na sua média diária de casos.")
            if assistências_casos < 5:
                print("Desclassificado! Jake precisa ajudar mais os companheiros.")
            else:
                print("Peralta ajudou bastante outros detetives, ele ainda está na competição!")
                if operações_campo < 20:
                    print("Peralta precisa sair mais da delegacia, está faltando ação em campo!")
                else: 
                    print("Jake ainda sobrevive por sua participação em campo, será que ele vai levar pra casa o prêmio?")
                    if operação_especial == "Sim":
                        print("Minha nossa! Jake Peralta é realmente um detetive diferenciado.")

                    else:
                        print("Para que operação especial quando se tem números, não é?")
                    if pontuação >= 70:
                        print("Jake é candidato forte ao prêmio. Será que Holt vai premiá-lo?")
                    elif 40 <= pontuação <= 69:
                        print("Muito bem! Mas ainda é incerto se vai ser suficiente para ganhar o prêmio.")
                    elif pontuação < 40:
                        print("Muito difícil de Jake ganhar o prêmio.")