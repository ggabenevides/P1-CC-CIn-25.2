# Leitura dos dados de entrada

x1_ted = int(input())
y1_ted = int(input())

x2_gc = int(input())
y2_gc = int(input())

amigo = str(input())

# Cálculo da distância 

distancia_original = ((x2_gc - x1_ted)² + (y2_gc - y1_ted)**2)**0.5
if amigo == "Barney":
    distancia_final = distancia_original + 10
elif amigo == "Marshall":
    distancia_final = distancia_original - 5
elif amigo == "Lily":
    distancia_final = distancia_original - 10
elif amigo == "Robin":
    distancia_final = distancia_original + 5

distancia_final = round(distancia_final)

# Impressão do resultado

