import numpy as np
#Soma de matrizes
#maneira mais lenta
# print('seja bem vindo ao programa de soma de matriz')
# m1c1 = int(input('Digite o número de cima na esquerda, da matriz 1 :'))
# m1c2 = int(input('Digite o número de cima na direita, da matriz 1 :'))
# m1b1 = int(input('Digite o número de baixo na esquerda, da matriz 1 :'))
# m1b2 = int(input('Digite o número de baixo na direita, da matriz 1 :'))
#
# m1 = np.array([[m1c1,m1c2],[m1b1,m1b2]])
#
# m2c1 = int(input('Digite o número de cima na esquerda, da matriz 2 :'))
# m2c2 = int(input('Digite o número de cima na direita, da matriz 2 :'))
# m2b1 = int(input('Digite o número de baixo na esquerda, da matriz 2 :'))
# m2b2 = int(input('Digite o número de baixo na direita, da matriz 2 :'))
# m2 = np.array([[m2c1,m2c2],[m2b1,m2b2]])
#
# m3 = m1 + m2
#
# print('Matriz 1 = ')
# print(m1)
# print('Matriz 2 = ')
# print(m2)
# print('A soma da matriz 1 + matriz 2 = ')
# print(m3)

m1 = []
print('Seja bem vindo ao programa de soma de matriz')
for l1 in range (2):
    m1.append([])
    for c1 in range(2):
        valor = int(input(f'Digite o valor da matriz 1 na posição [{l1+1}][{c1+1}]: '))
        m1[l1].append(valor)
print('m1 = ',m1)

m2 = []
print('Seja bem vindo ao programa de soma de matriz')
for l2 in range (2):
    m2.append([])
    for c2 in range(2):
        valor2 = int(input(f'Digite o valor da matriz 1 na posição [{l2+1}][{c2+1}]: '))
        m2[l2].append(valor2)
print('m2 = ',m2)

m3 = []
for l in range (2):
    m3.append([])
    for c in range(2):
        valor3 = m1[l][c] + m2[l][c]
        m3[l].append(valor3)

print('A soma das matrizes é:')
for l in range(2):
    print(m3[l])