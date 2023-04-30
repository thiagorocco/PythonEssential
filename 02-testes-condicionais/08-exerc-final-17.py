'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''

numero = int(input('Informe um número inteiro menor que 1.000: '))
resto = numero
centenas = 0
dezenas = 0
unidades = 0

if(numero>1000):
    print('O número informado é maior que 1.000. Tente novamente.')
else:
    if(resto>=100):
        centenas = int(resto/100)
        resto = resto - centenas*100
    if(resto>=10):
        dezenas = int(resto/10)
        resto = resto - dezenas*10
    if(resto>0):
        unidades = int(resto)
    print('O número ',numero,' possui ',centenas,' centenas, ',dezenas,' dezenas e ',unidades,' unidades')
