# coletar dados
nota_1 = float(input())
nota_2 = float(input())
nota_3 = float(input())
qtde_aulas = int(input())
qtde_faltas = int(input())

# calcular média e frequência de chris
media = float((nota_1 + nota_2 + nota_3)/3)
porcentagem_frequencia = ((qtde_aulas - qtde_faltas)/qtde_aulas)*100

#resultado
print(f"Chris, você conseguiu média {media:.2f} e {porcentagem_frequencia:.2f}% de presença.")

#requisitos p passar: média (simples) maior ou igual a 7,0 pontos; 75% de frequência nas aulas 
if (media >= 8) and (porcentagem_frequencia >= 75) :
    print ("Chris está APROVADO por nota e por presença! 🎉")
    print("Pisante maneiro, Chris! Agora é só torcer pros outros não vacilarem.")
elif (7 <= media < 8) and (porcentagem_frequencia >= 75):
    print("Chris está APROVADO! ✅")
    print("Sacomé, né? Passou raspando, mas a pizza ainda ficou longe.") 
elif (media >= 7) and (porcentagem_frequencia < 75):
    print("Chris ESTÁ REPROVADO por FALTA. ❌")
    print("Trágico! Não adianta só saber, tem que aparecer.")
elif (media < 7) and (porcentagem_frequencia >= 75):
    print("Chris ESTÁ REPROVADO por NOTA. ❌")
    print("Chris, já pro seu quarto ou eu vou te bater até você virar o avesso!")
else:
   print("Chris ESTÁ REPROVADO por NOTA e por FALTA. ❌")
   print("Chris, você perdeu o juízo? Eu trouxe você para esse mundo e posso muito bem tirar você dele.") 