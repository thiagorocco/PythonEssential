'''
    1. Faça um script que pede ao usuário um número inteiro positivo.
    Em seguida, deve criar uma lista onde o primeiro termo é 0, o segundo é 1 
    e os outros são a sequência de Fibonacci. O número de termos é o que o usuário forneceu como número.
'''

print('*** Sequência Fibonacci ***')
n = int(input('Informe um número inteiro positivo para o número de termos da sequência Fibonacci: '))

anterior = 0
proximo = 1
atual = 0

for count in range(n):
    print(atual)
    atual = proximo
    proximo += anterior
    anterior = atual
