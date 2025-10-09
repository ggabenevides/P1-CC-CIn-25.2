n = int(input())

completou_ana = False
completou_adrieli = False
completou_joab = False
completou_duda = False

num_pessoas_completaram = 0

# ana
for i in range(1, n+1):
    tentativa_ana = int(input())
    if tentativa_ana == 5:
        completou_ana = True
        num_pessoas_completaram += 1

# adrieli 
for i in range(1, n+1):
    tentativa_adrieli = int(input())
    if tentativa_adrieli == 5:
        completou_adrieli = True
        num_pessoas_completaram += 1

# joab
for i in range(1, n+1):
    tentativa_joab = int(input())
    if tentativa_joab == 5:
        completou_joab = True
        num_pessoas_completaram += 1

# duda 
for i in range(1, n+1):
    tentativa_duda = int(input())
    if tentativa_duda == 5:
        completou_duda = True
        num_pessoas_completaram += 1

# resultados
# ana
print(f"Ana tentou {n} vezes e completou a última casa {tentativa_ana}")
if completou_ana:
    print("Ana completou a amarelinha!")
else:
    print("Ana não conseguiu completar a amarelinha!")

# adrieli
print(f"Adrieli tentou {n} vezes e completou a última casa {tentativa_adrieli}")
if completou_adrieli:
    print("Adrieli completou a amarelinha!")
else:
    print("Adrieli não conseguiu completar a amarelinha!")

# joab
print(f"Joab tentou {n} vezes e completou a última casa {tentativa_joab}")
if completou_joab:
    print("Joab completou a amarelinha!")
else:
    print("Joab não conseguiu completar a amarelinha!")

# duda
print(f"Duda tentou {n} vezes e completou a última casa {tentativa_duda}")
if completou_duda:
    print("Duda completou a amarelinha!")
else:
    print("Duda não conseguiu completar a amarelinha!")

# vencedor ou empate
vencedor1 = "Ana"
vencedor2 = "Adrieli"
vencedor3 = "Joab"
vencedor4 = "Duda"
if num_pessoas_completaram == 1:
    if completou_ana:
        print(f"O vencedor é {vencedor1}!")
    elif completou_adrieli:
        print(f"O vencedor é {vencedor2}!")
    elif completou_joab:
        print(f"O vencedor é {vencedor3}!")
    elif completou_duda:
        print(f"O vencedor é {vencedor4}!")
else:
    if num_pessoas_completaram == 2:
        if completou_ana and completou_adrieli:
            print(f"Houve empate entre: {vencedor1}, {vencedor2}")
        elif completou_ana and completou_joab:
                print(f"Houve empate entre: {vencedor1}, {vencedor3}")
        elif completou_ana and completou_duda:
                print(f"Houve empate entre: {vencedor1}, {vencedor4}")
        elif completou_adrieli and completou_joab:
            print(f"Houve empate entre: {vencedor2}, {vencedor3}")
        elif completou_adrieli and completou_duda:
            print(f"Houve empate entre: {vencedor2}, {vencedor4}")
        elif completou_joab and completou_duda:
            print(f"Houve empate entre: {vencedor3}, {vencedor4}")
    if num_pessoas_completaram == 3:
        if completou_ana and completou_adrieli and completou_joab:
            print(f"Houve empate entre: {vencedor1}, {vencedor2}, {vencedor3}")
        elif completou_ana and completou_adrieli and completou_duda:
            print(f"Houve empate entre: {vencedor1}, {vencedor2}, {vencedor4}")
        elif completou_adrieli and completou_joab and completou_duda:
            print(f"Houve empate entre: {vencedor2}, {vencedor3}, {vencedor4}")
    if num_pessoas_completaram == 4:
        print(f"Houve empate entre: {vencedor1}, {vencedor2}, {vencedor3}, {vencedor4}")
