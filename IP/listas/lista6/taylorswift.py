vida_amorosa = {"Jake Gyllenhaal": (("All too Well", "We are never ever getting back together", "Red"), 2010),
                "Joe Jonas": (("Forever & Always", "Holy Ground"), 2008),
                "Taylor Lautner": (("Back to December", "I can see you", "Midnight rain"), 2009),
                "Tom Hiddleston": (("Getaway Car"), 2016),
                "Joe Alwyn": (("Paper Rings", "Lover", "So Long London"), 2020),
                "Harry Styles":  (("Style", "Out of the Woods", "All You Had to Do Was Stay"), 2012),
                "Travis Kelce": (("The Fate of Ophelia", "The Alchemy", "Wi$h Li$t"), 2023)}

carreira = {"Fearless": [("Ganhou o VMA 2009, porém Kanye West interrompeu seu discurso de vitória. Também ganhou o Grammy de Álbum do Ano (2010), sendo a artista mais jovem da história (na época) a receber esse prêmio.",)],
            "Speak Now": [("Teve uma turnê mundial massiva que consolidou seu status de superestrela global, o albúm Speak Now vendeu mais de 1 milhão de cópias na primeira semana, superando qualquer outro álbum dos últimos dois anos.",)],
            "1989": [("“1989” tornou-se o primeiro álbum de Taylor exclusivamente pop; a artista emplacou dois hits mundiais: Blank Space e Bad Blood. Fun Fact: Taylor nasceu em 13 de dezembro de 1989.",)],
            "Reputation": [("O álbum foi uma resposta à mídia, às traições públicas e ao controle da narrativa sobre sua imagem. Além disso, em 2019, Taylor tem os direitos autorais de seus álbuns roubados.",)],
            "The Eras Tour": [("The Eras Tour é uma turnê comemorativa, com detalhes que buscam fazer jus á tudo que Taylor Swift fez e alcançou em seus anos de carreira. No Brasil, aconteceram seis apresentações em novembro de 2023 em São Paulo e no Rio de Janeiro.",)]}

def achar_pessoa_pela_musica (vida_amorosa, musica):
    for pessoa in tuple(vida_amorosa.keys()):
        if musica in vida_amorosa[pessoa][0]:
            return pessoa
        else:
            return None
        
ataque_ye = "Que grande mentira! Taylor Swift só mente"
entrada = ""
eras_roubadas = []

while entrada != "Já chega de fatos sobre a Taylor, vai fazer a lista de IP":
    entrada = input()

    if entrada == "Qual a situação de relacionamento?":
        pessoa = input()
        ano = int(input())
        if vida_amorosa[pessoa][1] == ano:
            situacao = "estão namorando"
        else:
            situacao = "não estão namorando"
        print(f"{pessoa} e Taylor Swift {situacao} em {ano}")

    elif entrada == "Qual pessoa está relacionada essa música?":
        musica = input()
        pessoa = achar_pessoa_pela_musica(vida_amorosa, musica)
        print(f"A pessoa relacionada é {pessoa}, Taylor nunca erra em suas músicas")

    elif entrada == "Quais são todas as músicas relacionadas a essa pessoa?":
        pessoa = input()
        print(f"Cartas de amor ou indiretas, as músicas dedicadas a {pessoa} são: ", end="")
        for musica in vida_amorosa[pessoa][0]:
            if vida_amorosa[pessoa][0].index(musica) == -1:
                print(musica)
            else:
                print(f"{musica}, ", end="")

    elif entrada == "O que aconteceu nessa era?":
        era = input()
        print(carreira[era])

    elif entrada == "Wayne nunca deixará Taylor vencer! O CIn precisa manter o hate na diva pop, eu vou alterar as informações":
        era = input()
        carreira[era].append(ataque_ye)
        print("Cuidado, há um impostor no guia... Informações comprometidas")

    elif entrada == "Scooter não liga que ela comprou todos os álbuns de volta, ele vai roubar tudo dessa era":
        era = input()
        eras_roubadas.append(era)
        del carreira[era]
        print(f"Para onde foi a história sobre {era}? Parece que alguém roubou tudo e não avisou a Taylor")

# relatorio final / eras roubadas
if len(eras_roubadas) > 0:
    print("Big Machine Records roubou:")
    for era in eras_roubadas:
        print(era)