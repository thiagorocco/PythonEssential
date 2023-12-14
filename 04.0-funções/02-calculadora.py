def soma():
    x = float(input('Primeiro número: '))
    y = float(input('Segundo número: '))
    soma = x + y
    print('Soma: ',soma)

def subtracao():
    x = float(input('Primeiro número: '))
    y = float(input('Segundo número: '))
    subtracao = x - y
    print('Subtração: ',subtracao)

def multiplicacao():
    x = float(input('Primeiro número: '))
    y = float(input('Segundo número: '))
    multiplicacao = x * y
    print('Multiplicação: ',multiplicacao)

def divisao():
    x = float(input('Primeiro número: '))
    y = float(input('Segundo número: '))
    divisao = x / y
    print('Divisão: ',divisao)

opcao = 1

while opcao:
    print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")

    opcao = int(input("Opção: "))

    if(opcao==1):
        soma()
    if(opcao==2):
        subtracao()
    if(opcao==3):
        multiplicacao()
    if(opcao==4):
        divisao()