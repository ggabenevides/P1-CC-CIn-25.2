x = float(input())
y = float(input())

# 1o quadrante y>0 x>0
# 2o quadrante y>0 x<0
# 3o quadrante y<0 x<0
# 4 quadrante y<0 x>0
# eixo x  y=0 
# eixo y x=0
# origem y=0 x=0

if x>0:
    if y>0 :
        print("O ponto está no primeiro quadrante")
    elif y<0:
        print("O ponto está no quarto quadrante")
    else:
        print("O ponto está no eixo x")
elif y>0:
    if x<0:
        print("O ponto está no segundo quadrante")
    elif x<0:
        print("O ponto está no terceiro quadrante")
    else:
        print("O ponto está no eixo y")
else:
    print("O ponto está na origem")