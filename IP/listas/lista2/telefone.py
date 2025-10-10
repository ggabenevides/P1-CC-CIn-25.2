print("Vai começar a brincadeira! Será que a palavra vai ficar igual até o fim?")
num_participantes = int(input())

nome_participante = str(input())
palavra_inicial = str(input())
palavra_anterior = palavra_inicial

num_palavras_erradas = 0
for i in range(2,num_participantes+1):
    nome_participante = str(input())
    palavra_falada = str(input())
    if palavra_anterior != palavra_falada:
        print(f"Parece que {nome_participante} não conseguiu ouvir muito bem e acabou passando pra frente uma palavra diferente da que escutou…")
        num_palavras_erradas+=1
        if num_palavras_erradas ==1:
            jogador_errado1 = nome_participante
        if num_palavras_erradas ==2:
            jogador_errado2 = nome_participante
        if num_palavras_erradas == 5:
            print(f"Caramba, que confusão! A palavra {palavra_inicial} já tá toda embaralhada e virou {palavra_falada}!")
    palavra_anterior = palavra_falada 

if palavra_falada == palavra_inicial:
    if num_palavras_erradas==0:
        print(f"Impressionante, todos os jogadores ouviram e falaram perfeitamente a palavra {palavra_inicial}! Talvez os telefones modernos comecem a perder espaço pra moda antiga.")
    elif num_palavras_erradas>=1:
        print(f"Parece que ocorreram {num_palavras_erradas} trocas durante o processo, mas mesmo com essa pequena confusão, a palavra {palavra_inicial} conseguiu chegar no fim do telefone sem fio.")
if palavra_falada != palavra_inicial:
    if num_palavras_erradas == 1:
        print(f"Poxa, foi por pouco, só quem errou foi {jogador_errado1} que disse {palavra_falada} ao invés de {palavra_inicial}…")
    elif num_palavras_erradas==2:
        print(f"Se não fosse pelos erros de {jogador_errado1} e {jogador_errado2} a palavra {palavra_inicial} poderia ter chegado até o fim, talvez eles devessem tentar de novo.")
    elif num_palavras_erradas > 2:
        print(f"É, parece que os alunos se confundiram bastante durante a brincadeira e a palavra {palavra_inicial} acabou virando {palavra_falada}. No total, ocorreram {num_palavras_erradas} trocas.")