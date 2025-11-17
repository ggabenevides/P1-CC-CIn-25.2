# funcoes
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fatorial(n-1)
    
def calculo_possibilidades (valor):
    cedulas = [5, 10, 20, 50, 100]
    for i in cedulas:
        combinacao = fatorial(valor) / (fatorial(valor-i)*fatorial(i))

# programa
cedulas = [100, 50, 20, 10, 5]
valor_total_da_conta = int(input())
print(f"Calculando possibilidades para o valor: {valor_total_da_conta}")
if valor_total_da_conta % 5 == 0:
    # o programa segue normalmente p a funcao recursiva
    resultado = calculo_possibilidades(valor_total_da_conta)
else:
    resultado = [0, 0, 0, 0, 0, 0]
    print("\nInfelizmente, não há como pagar essa conta com as notas disponíveis.")

# relatorio final
print(f"\nTotal de possibilidades: {resultado[0]}")
print("\nUso das notas:")
for i in range(5):
    print(f"R${cedulas[i]}: usada em {resultado[i+1]} combinações")
