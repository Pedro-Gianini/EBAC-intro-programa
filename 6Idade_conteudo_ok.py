
print('Vamos achar programas para sua idade')

idade = int(input('Qual a sua idade?'))
#Contrução do encademaneto

if idade < 10 :
     print('Você é uma criança, veja programas com classificação: (L)')
elif 10 <= idade <12:
    print('Você ainda é uma criança, veja programas com classificação: (10)')
elif 12 <= idade < 14:
    print('Você ainda é uma criança, veja programas com classificação: (12)')
elif 14 <= idade < 16:
    print('Olá adolescente! Você já pode ver programas de classificação: (14)')
elif 14 <= idade < 16:
    print('Olá adolescente! Você já pode ver programas de classificação: (16)')
elif idade > 18:
    print('Olá adulto! Você já pode ver programas de qualquer classificação)')
