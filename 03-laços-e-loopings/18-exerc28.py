'''
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor
para em cada um.
'''
cd = int(input('Informe quantos CD''s há na coleção: '))
valor = 0
media  = 0

for count in range(1,cd+1):
    valor = float(input('Informe o valor pago no %.0f.o CD: ' %count))
    media += valor

media = media/cd
print('Valor médio pago em cada um dos ',cd,' CDs'' = R$%.2f' %media)  