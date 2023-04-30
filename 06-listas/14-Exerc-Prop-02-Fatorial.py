'''
    2. Faça um script que pede um número inteiro positivo ao usuário.
    Em seguida, cria uma lista com igual número de itens, onde o primeiro termo é 1!, 
    o segundo é 2!, o terceiro é o valor de 3!, etc, até o termo que ele digitou. 
    Ou seja, se digitou n, vai exibir até o termo de índice n-1, e lá na lista vai ter o valor de (n-1)!.
'''

def fatorial(n):
    if n==1:
        return 1
    else:
        return n * fatorial(n-1)

print('*** Programa Array com fatoriais ***')
n = int(input('Informe um número inteiro positivo: '))
lista = []

for count in range(n):
    lista += [fatorial(count+1)]

print('Elementos do array: ',lista)
