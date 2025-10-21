# definindo variaveis e listas
nivel_suspeita = 0
SIGLA_PERSONAGEM = []
EVENTO = []
HORA_INICIO = []
HORA_FIM = []


# input inicial
print("Iniciando investigação... Zé Felipe está focado.")
numero_eventos = int(input())
for i in range(numero_eventos): # SIGLA_PERSONAGEM - EVENTO - HORA_INICIO - HORA_FIM
    elementos = []
    dados = input()
    elementos = dados.split(" - ")
    SIGLA_PERSONAGEM.append(dados[0])
    EVENTO.append(dados[1])
    HORA_INICIO.append(dados[2])
    HORA_FIM.append(dados[3])

# bubble sort das listas de acordo com hora de inicio (regra 0)
n = len(HORA_INICIO)
for i in range(n):
    for j in range(0, n-i-1):
        if HORA_INICIO[j] > HORA_INICIO[j+1]:
            HORA_INICIO[j], HORA_INICIO[j+1] = HORA_INICIO[j+1], HORA_INICIO[j]
            HORA_FIM[j], HORA_FIM[j+1] = HORA_FIM[j+1], HORA_FIM[j]
            SIGLA_PERSONAGEM[j], SIGLA_PERSONAGEM[j+1] = SIGLA_PERSONAGEM[j+1], SIGLA_PERSONAGEM[j]
            EVENTO[j], EVENTO[j+1] = EVENTO[j+1], EVENTO[j]

# regra definitiva 
if "VJM" in SIGLA_PERSONAGEM:
    nivel_suspeita = 100

# avaliação dos eventos 
while nivel_suspeita < 100:
    # regra 2
    for horario in HORA_INICIO:
        idx = HORA_INICIO.index(horario)
        if SIGLA_PERSONAGEM[idx] == "V":
            if horario 