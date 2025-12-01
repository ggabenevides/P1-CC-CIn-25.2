# inicializando programa
print("Phil, querido... Você tem certeza que essa música é literalmente sobre... casas?")
print("A própria Sabrina disse que nada na música é uma metáfora! Além disso, o sobrenome dela é carpinteira, acho que ela tem lugar de fala…")
print()

# inputs iniciais
categorias = ("bairro", "quartos", "preço")
catalogo_phil = {}
num_propriedades = int(input())

enderecos = []
for i in range(num_propriedades): # criando catalogo
    informacoes = {} # dicionario interno temporario 

    # tratando dados
    dados = input().split(" - ") # [0] = bairro; [1] = endereco-quartos-preco 
    endereco_quarto_preco = dados[2].split("-")
    dados.pop(-1)
    dados.append(int(endereco_quarto_preco[0]))
    dados.append(int(endereco_quarto_preco[1])) # CORREÇÃO: [0] = str(bairro); [1] = str(endereco) = chave do catalogo ; [2] = int(quartos); [3] = int(preço)
    endereco = dados[1] # vai ser a chave do dicionario principal
    enderecos.append(endereco)
    dados.pop(1) # CORREÇÃO: [0] = bairro ; [1] = quartos ; [2] = preço
    
    # adicionando dados no dicionario interno do endereço
    for i in range(len(categorias)):
        informacoes[categorias[i]] = dados[i]

    # adicionando dicionario interno no dicionario externo (catalogo)
    catalogo_phil[endereco] = informacoes

print("Catálogo concluído! Quem será que irá comprar uma casa de Phil?")
print()

# loop de atendimento
cliente = ""

num_vendas = 0
while cliente != "FIM":
    scores = []
    enderecos_validos = []
    cliente = input()
    if cliente != "FIM":
        requisitos_cliente = tuple(input().split("-"))
        for i in range(num_propriedades):
            if (catalogo_phil[enderecos[i]]["quartos"] >= int(requisitos_cliente[0])) and (catalogo_phil[enderecos[i]]["preço"] <= int(requisitos_cliente[1])):
                # casa válida
                enderecos_validos.append(enderecos[i])
                score_total = catalogo_phil[enderecos[i]]["quartos"] * 10 
                scores.append(score_total)
        if len(enderecos_validos) == 0:
            print(f"Puxa, {cliente}, vou te avisar se algo aparecer. Não tenho nada com esses requisitos.")
            print()
        else:
            # escolhendo melhor casa para apresentar
            maior_score = max(scores)
            melhor_casa_idx = scores.index(maior_score) # index pega a primeira ocorrencia do maior score na iteracao
            melhor_casa = enderecos_validos[melhor_casa_idx]
            # apresentacao da casa
            print(f"🎤 Bem-vindo ao House Tour de {catalogo_phil[melhor_casa]['bairro']}, {cliente}!")
            print(f"➡ Casa: {melhor_casa}")
            print(f"💖 Score: {maior_score} pontos")
            print()
            if maior_score >= 40: # casa agradou
                if cliente == "Taylor Swift":
                    print('"Essa casa é perfeita para passar as férias na praia!"')
                elif cliente == "Sabrina Carpenter":
                    print('"Uau, Phil! Acho que finalmente encontrei o cenário perfeito para o clipe de House Tour!"')   
                else:
                    print(f'"{cliente} ficou encantado(a)! Phil comemora mais uma venda de sucesso!"')
                print()
                print('Venda concluída! Phil dança triunfante ao som de "House Tour"!')
                print()  
                num_vendas += 1              
            else:
                if cliente == "Taylor Swift":
                    print('"Nós nunca vamos comprar essa casa juntos, Phil!"')
                elif cliente == "Sabrina Carpenter":        
                    print('"Hmm... Sabe Phil, a letra não era tão literal assim…"')
                else:        
                    print('"Parece que a música não ajudou nas vendas dessa vez…"')
                print()
                print('Talvez a Sabrina realmente não estivesse falando de imóveis…')
                print()
else:
    print("===== RELATÓRIO DE VENDAS =====")
    print(f"Total de casas vendidas: {num_vendas}")
    print("===============================")