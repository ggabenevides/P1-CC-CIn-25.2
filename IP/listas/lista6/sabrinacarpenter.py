# inicializando programa
print("Phil, querido... Você tem certeza que essa música é literalmente sobre... casas?")
print("A própria Sabrina disse que nada na música é uma metáfora! Além disso, o sobrenome dela é carpinteira, acho que ela tem lugar de fala…")
print()

# inputs iniciais
categorias = ("bairro", "quartos", "preço")
catalogo_phil = {}
num_propriedades = int(input())

for i in range(num_propriedades): # criando catalogo
    informacoes = {} # dicionario interno temporario 

    # tratando dados
    dados = input().split(" - ") # [0] = bairro; [1] = endereco-quartos-preco 
    endereco_quarto_preco = dados[1].split("-")
    dados.pop(-1)
    dados.append(endereco_quarto_preco[0])
    dados.append(int(endereco_quarto_preco[1]))
    dados.append(int(endereco_quarto_preco[2])) # CORREÇÃO: [0] = str(bairro); [1] = str(endereco) = chave do catalogo ; [2] = int(quartos); [3] = int(preço)
    endereco = dados[1] # vai ser a chave do dicionario principal
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
while cliente != "FIM":
    cliente = input()
    if cliente != "FIM":
        requisitos_cliente = tuple(input().split("-"))
        
