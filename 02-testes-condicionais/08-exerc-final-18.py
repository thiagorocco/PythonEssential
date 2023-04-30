'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque
e depois informar quantas notas de cada valor serão fornecidas. 

As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 

O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade d
e notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, 
uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

'''
saque = int(input('Informe o valor do saque: '))
resto = saque
notas100 = 0
notas50 = 0
notas10 = 0
notas05 = 0
notas01 = 0


if(resto>=100):
    notas100 = int(resto/100)
    resto = resto - notas100*100
if(resto>=50):
    notas50 = int(resto/50)
    resto = resto - notas50*50
if(resto>=10):    
    notas10 = int(resto/10)
    resto = resto - notas10*10
if(resto>=5):    
    notas05 = int(resto/5)
    resto = resto - notas05*5
if(resto>=1):    
    notas01 = int(resto)
    resto = resto - notas01

print('A quantia de R$',saque,' deverá ser paga nas seguintes notas e quantidades: ')
print('Notas de R$ 100,00 - ',notas100)
print('Notas de R$ 50,00 - ',notas50) 
print('Notas de R$ 10,00 - ',notas10)
print('Notas de R$ 5,00 - ',notas05)
print('Notas de R$ 1,00 - ',notas01)