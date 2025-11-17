
def decifrando (indice_final, chave, frase, idx=0):
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T' ,'U', 'V' ,'W', 'X', 'Y' ,'Z']
    if idx == indice_final+1:
        return ""
    else:        
        chave_idx = alfabeto.index(chave)
        letra_encript_idx = alfabeto.index(frase[idx])

        letra_decript_idx = (letra_encript_idx - chave_idx) % 26

        letra_decript = alfabeto[letra_decript_idx]
        chave = letra_decript

        return  letra_decript + decifrando(indice_final, chave, frase, idx+1)

# variaveis
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T' ,'U', 'V' ,'W', 'X', 'Y' ,'Z']
num_pegadinhas = 0
indices_pegadinhas = []

# programa
chave_inicial = input()
frase_criptografada = list(input())   
print("Decifrando mensagem do Trickster...")
for i in range(len(frase_criptografada)):
    if frase_criptografada[i] not in alfabeto:
        num_pegadinhas += 1
        indices_pegadinhas.append(i)
frase_sem_pegadinhas = []
for letra in frase_criptografada:
    if letra in alfabeto:
        frase_sem_pegadinhas.append(letra)
if num_pegadinhas > 0:
    print("Esse Trickster é um picareta mesmo. Foram encontradas armadilhas nas posições: ", end="") 
    for i in range(len(indices_pegadinhas)):
        if i == len(indices_pegadinhas)-1:
            print(indices_pegadinhas[i])
        else:
            print(f"{indices_pegadinhas[i]}, ", end="")
else:
    print("Nenhuma armadilha encontrada! Até que o Trickster foi bonzinho.")
indice_inicial = len(frase_sem_pegadinhas) - 1
frase_decript = decifrando(indice_inicial, chave_inicial, frase_sem_pegadinhas)
print(f"Mensagem revelada: {frase_decript}")