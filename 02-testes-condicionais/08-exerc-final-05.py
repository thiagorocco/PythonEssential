'''
5. Faça um programa que pede dois inteiros e armazene em duas variáveis. 
Em seguida, troque o valor das variáveis e exiba na tela
'''
num1 = int(input('Informe o 1.o número inteiro: '))
num2 = int(input('Informe o 2.o número inteiro: '))

print('Valor do 1.o primeiro número = %.0f e valor do 2.o número = %.0f' %(num1,num2))

auxiliar = num2
num2 = num1
num1 = auxiliar

print('Valor do 1.o primeiro número = %.0f e valor do 2.o número = %.0f' %(num1,num2))