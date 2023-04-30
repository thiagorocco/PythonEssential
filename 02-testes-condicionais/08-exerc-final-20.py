'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
'''
import math

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o primeiro número: '))
option = input('Qual operação deseja realizar: \n\
1 - Soma\n\
2 - Subtração\n\
3 - Multiplicação\n\
4 - Divisão: ')

option = int(option)

if(option == 1):
    oper = num1+num2
elif(option == 2):
    oper = num1-num2
elif(option == 3):
    oper = num1*num2
elif(option == 4):
    oper = num1/num2

if (oper%2) == 0:
    print(oper,' é par')
else:
    print(oper,' é ímpar')

if oper>=0:
    print(oper,' é positivo')
else:
    print(oper,' é negativo')

if round(oper)==oper:
    print(oper,' é inteiro')
else:
    print(oper,' é decimal')
