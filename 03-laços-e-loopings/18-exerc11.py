'''
Faça um programa que receba dois números inteiros e gere os números inteiros que 
estão no intervalo compreendido por eles.

Altere o programa anterior para mostrar no final a soma dos números.
'''
maior = int(input('Informe um número inteiro'))
menor = int(input('Informe outro número inteiro'))
aux = 0
soma = 0

if(menor > maior):
    aux = menor
    menor = maior
    maior = aux

for menor in range(menor,maior-1):
    print(menor+1)
    soma += menor+1

print('Soma = ',soma)
