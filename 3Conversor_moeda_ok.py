print('Vamos converter a moeda real para dolar')


#real = float(input('Qual a cotação  do real?'))
dolar = float(input('Qual a cotação  do dolar?'))
#real = 1

#opçao2= dolar/real #
real = float(input('Quanto voce quer converter??'))
opçao1 = real/dolar # real para dolar
print('Com R${:.2f} você pode comprar US${:2f}'.format(real,opçao1))