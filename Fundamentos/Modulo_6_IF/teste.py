venda= 20000
bonus= (venda * 3/ 100)
print(bonus)

#####################################
faturamento = input('Informe o faturamento: ')
custo = input('Informe o custo: ')

if faturamento == '' and custo == '':
    print('Faturamento e custo não informados')
else:
    lucro = int(faturamento) - int(custo)
    print(f'O lucro é de: {lucro}')
#OU
if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print(f'O lucro é de: {lucro}')
else:
    print('Faturamento e custo não informados')

#####################################