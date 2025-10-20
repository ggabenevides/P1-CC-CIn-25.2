frases = ["Que tiro foi esse?", "Segura a marimba", "Tá com raiva? Morde as costas", "Bateu de frente é só rajadão"]

num_frases_novas = int(input())

for i in range(num_frases_novas):
    frase_nova = str(input())
    frases.append(frase_nova)

frases_ordenadas = frases.copy()
frases_ordenadass = frases_ordenadas.sort()

frases_ja_printadas = []
for frase in frases:
    if not(frase in frases_ja_printadas):
        print(f'"{frase}": {frases_ordenadas.count(frase)}')
        frases_ja_printadas.append(frase)

print(frases_ordenadas)