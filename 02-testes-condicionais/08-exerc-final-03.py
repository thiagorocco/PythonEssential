#3. Faça um Programa que leia três números inteiros e mostre o maior deles.
num1 = int(input('Digite o 1.o número: '))
num2 = int(input('Digite o 2.o número: '))
num3 = int(input('Digite o 3.o número: '))

if num1>num2 and num1>num3:
    print('Maior número informado: ',num1)
elif num2>num3:
    print('Maior número informado: ',num2)
else:
    print('Maior número informado: ',num3)