'''
12. Faça um Programa que peça os 3 lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes; 

'''
lado1 = int(input('Informe o valor do 1.o lado do triângulo: '))
lado2 = int(input('Informe o valor do 2.o lado do triângulo: '))
lado3 = int(input('Informe o valor do 3.o lado do triângulo: '))

if (lado1+lado2)>lado3:
    print('É triângulo')
    if lado1==lado2 and lado1==lado3:
        print('Equilátero')
    elif lado1==lado2 or lado1==lado3:
        print('Isósceles')
    elif lado1!=lado2 and lado1!=lado3:
        print('Escaleno')

else:
    print('Não é triângulo')

