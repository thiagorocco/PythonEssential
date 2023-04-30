'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120
'''
fat = int(input('Informe um número para saber sua fatorial: '))
n = fat-1
termos = fat

for count in range(1,n+1):
    fat *= n
    n -=1

print('Fatorial de ',termos,' = ',fat)