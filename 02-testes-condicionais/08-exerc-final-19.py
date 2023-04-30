'''
19.Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
Dica: utilize uma função de arredondamento.
'''
import math

numero = input('Informe um número: ')
redondo = round(numero)

if(numero!=redondo):
    print('É um número decimal')
else:
    print('É um número inteiro')