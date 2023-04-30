'''
Um cliente pediu que o sistema do banco tivesse a seguinte função:
Dizer o valor inicial que ele deve investir, para ao final de 'n' 
meses ele tenha um valor 'vf', supondo que este dinheiro esteja 
rendendo uma rentabilidade 'i' mensal, em porcentagem esse 'i'.
Faça um programa que pede o valor final, o tanto de meses que 
vai ficar aplicado, a rentabilidade e o script mostre o valor inicial que ele deve investir para 
atingir tal objetivo.
'''
montante = float(input('Qual o valor inicial do montante que deseja ganhar?: '))
taxa = float(input('A qual taxa mensal?: '))
tempo = float(input('Em quanto tempo o dinheiro ficará investido em meses?: '))

capital = montante/(1+taxa/100)**tempo

print('Valor total do capital a investir: ',capital)