'''
 Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. 
 Dica: utilize o operador módulo (resto da divisão): %

'''

numero = int(input('Informe um número: '))

if(numero%2==0):
    print('Número par')
else:
    print('Número ímpar')