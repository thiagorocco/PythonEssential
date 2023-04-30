'''
01. Escreva um programa que pede o raio de um círculo, e em seguida exiba o perímetro e área do círculo.
Para saber o valor do pi, faça:
import math
print(math.pi)
Pronto, para saber o valor de pi, basta usar 'math.pi', que é um float
'''
import math

pi = math.pi
raio = float(input('Digite o raio de um círculo: '))
perimetro = 2 * pi * raio

print('Perímetro da circunferência = %.2f' %perimetro)