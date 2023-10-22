#programa que recebe 2 cadeias de caracteres, compara ela pra ver se são iguais,
# enquanto n forem iguais o programa não para de rodar

#ex: digite sua senha, digite novamente sua senha. Se n forem iguais repita o procedimento, se for igual deu certo parabens
#se 1 for diferente de 2

senha=str(input('digite sua senha: '))

confirma_senha=str(input('digite a confirmação de sua senha: '))

while senha!=confirma_senha:
    print('as senhas não correspondem...digite - as novamente')
    senha = str(input('digite sua senha: '))
    confirma_senha = str(input('digite a confirmação de sua senha: '))
print('excelente! as senhas correspondem')