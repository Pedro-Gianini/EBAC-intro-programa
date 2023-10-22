#Jogo impar part
from random import randint
v=0
p=0
while True:
    jogador = int(input('Diga um valor:'))
    computador = randint(0,11)
    total = jogador + computador
    tipo =  " "
    while tipo not in"PI":
        tipo = str(input('Par ou  ímpar?[P/I]')).strip().upper()[0]
        print(f'você jogou {jogador} e o computador {computador}. total de {total} ',  end ='')
        print(' Deu Par'  if total %2  == 0 else ' Deu Impar ')
        if  tipo == 'P':
            if total  % 2 == 0:
                print('Você Venceu!')
                v +=1
            else:
                print('Você Perdeu!')
                p +=1
                break
        elif tipo == 'I':
            if total % 2 == 1:
                print('Você Venceu!')
                v += 1
            else:
                print('Você Perdeu!')
                p += 1
                break
        print('vamos jogar de novo')
    print(f'GAMEOVER! Voce venceu {v} vezes. O computador venceu {p} vezes')
