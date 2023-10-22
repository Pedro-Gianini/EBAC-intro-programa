# escrever um programa que recebe uma lista de nomes e depois são apresentados
#Criar conjunto de cacteres, ou seja uma cadei de caracteres por meio de um vetor e no final será gerado uma
# lista com todos os carcteres

#Ex digitar nomes de pessoas(numa lista de 100 conv poer exemplo), ai nos perguntamos "Quer alimentar?"
#Se sim , digite o nome da pessoa; se quer parar de alimentar, digita não e como resultado seria
#uma lista com os nomes digitados e os lugares não digitados aparecer como "-" ou " "



#resolução :Antes de tudo perguntar se quer add o nomes, tamanho da lista, em pegar o nome e armazena - lo
# nomes dos convidades e sua posição na lista (index)

# Limite máximo de convidados
limite_convidados = 100

# Criar uma lista vazia para armazenar os nomes dos convidados
convidados = []

# Criar uma lista de lugares
lugares = ['Lugar ' + str(i) for i in range(1, limite_convidados + 1)]

# Perguntar se deseja adicionar convidados
inicio = input('Você deseja adicionar algum convidado? (S/N): ')
indice = 1  # Começar o índice em 1

while inicio.lower() == 's':
    if len(convidados) >= limite_convidados:
        print('Você atingiu o limite máximo de convidados.')
        break
    convidado = input('Digite o nome do convidado: ')
    convidados.append(convidado)
    lugares[indice - 1] = f'{indice}: {convidado}'  # Preencher o lugar com índice e nome
    ainda_pode_chamar = limite_convidados - len(convidados)
    print(f'Você ainda pode chamar {ainda_pode_chamar} convidados.')
    inicio = input('Deseja adicionar mais convidados? (S/N): ')
    indice += 1  # Incrementar o índice

# Exibir a lista de convidados e lugares
print('Sua lista de Convidados:')
for lugar in lugares[:len(convidados)]:
    print(lugar)
