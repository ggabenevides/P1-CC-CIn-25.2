#input qtde média de diamantes por hora (A, L e P) e tempo
A = int(input())
L = int(input())
P = int(input())
H = int(input())

#cálculo da quantidade total de diamantes 
A *= H
L *= H
P *= H

# valor máximo entre dois valores x = (a + b + (|a - b|)) / 2.
al = (A + L + ( A - L )) / 2
m = int((al + P + ( al - P )) / 2)

#output 
print(m)