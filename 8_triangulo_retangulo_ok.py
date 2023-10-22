#Criar um programa que verifica se um triangulo é retangulo , ao receber os 2 valores da hipotenusa e catetos

# pega o valor do cat1 e cat2 , com uma função externa faça a soma dos quadrados dos catetos e depois compare com o quad da hip,
# se hip ao quad = soma dos cat ao quad , logo é triangulo retangulo, se n não é e se n for nem um nem outro os valores estão errados

#digite o maior valor (hipotenusa)
h = int(input('escreva o valor da hipotenusa: '))

#digite o segunda maior valor (maior cateto)
c1 = int(input('escreva o valor do maior cateto: '))

#digite o terceiro maior valor (menor cateto)
c2 = int(input('escreva o valor do menor cateto: '))

teste = (c1*c1)+(c2*c2)
if h>c1 and h>c2:
    if(h*h)==teste:
        print('O triângulo é um triangulo retângulo')
    else:
        print('O triângulo não é um triângulo retângulo')
else:
    print('os valores não formam um triângulo')



