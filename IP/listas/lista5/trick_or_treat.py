def particoes(n, k):
    if n == 0 : # caso base
        return 1
    elif n < 0 or k == 0:
        return 0
    else: # passo recursivo
        return particoes(n, k-1) + particoes(n-k, k)

# programa
print("DOCES OU TRAVESSURAS???")
doces = int(input())
num_particoes = particoes(doces, doces)
print(f"sem travessuras por hoje! tenho {num_particoes} sacolinhas pra vocês")
if num_particoes%2 == 0:
    print("doces equilibrados, sem travessuras!")
else:
    print("hmm... número ímpar de sacolinhas 🍭 cuidado com as bruxas!")
