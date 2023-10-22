#Jogo impar part

print('Olá! Descubra se um numero é impar ou par')
n = int(input('Digite o valor que quer descobrir : '))
print(f'você digitou {n}')
if n%2 == 0:
    print(f'O número {n} é "PAR"')
else:
    print(f'o número {n} é impar')