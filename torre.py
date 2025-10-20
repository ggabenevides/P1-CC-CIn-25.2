altura = int(input())
for linha in range(altura):
    espacos = altura - linha
    for espaco in range (espacos):
        print("⠀", end="")
    for hash in range (1, (linha+1)*2):
        print("#", end="")
    print()