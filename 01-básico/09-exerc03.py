'''
criar um programa envolvendo a poupança.
Você vai perguntar o valor inicial investido na poupança, 
a rentabilidade mensal, quantos meses o cliente deseja deixar
o dinheiro investido e mostrar o valor final na conta do cliente do banco.
'''
capital = float(input('Qual o valor inicial do investimento?: '))
taxa = float(input('Qual a rentabilidade mensal?: '))
tempo = float(input('Quanto tempo o dinheiro ficará investido em meses?: '))

montante = capital*(1+taxa/100)**tempo
print('Valor total do montante: ',montante)
