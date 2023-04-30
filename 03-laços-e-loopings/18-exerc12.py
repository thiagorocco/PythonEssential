'''

Desenvolva um gerador de tabuada, 
capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
'''
n = 0

while n > 10 or n < 1:
    n = int(input('Informe um número que deseja saber a tabuada de 1 a 10: '))

for i in range(1,10+1):
    print(n,' x ',i,'\t = ',n*i)