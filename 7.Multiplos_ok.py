#FALATA ARRUMAR CONCEITO MATEMÁTICO
#pensei na logica de contabilizar a segunda casa decimal depois da virgula, se maior que zero é multiplo, se n , não
#digite o numero 1
n1 = int(input ('escreva seu 1º numero: '))
#digite o numero 2
n2 = int(input ('escreva seu 2º numero: '))
contagem_multiplo = 0
print('numero 1 :',n1)
print('numero 2 :',n2)

if n1 < n2:
    r1 = (n2/n1)
    if r1.is_integer():
        print('os numeros são muiltiplos')
        contagem_multiplo +=1
    else:
        print('os numeros não são multiplos')

elif n1 > n2:
    r2 = n1/n2
#r2 == 0
    if r2.is_integer():
        print('os numeros são muiltiplos')
        contagem_multiplo +=1
    else:
        print('os numeros não são multiplos')
else :
    print('os numeros não são multiplos')

print(f'Numéro 1 é multiplo de número 2 por: {contagem_multiplo} vezes')




