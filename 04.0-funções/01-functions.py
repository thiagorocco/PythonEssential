def soma():
    x = float(input('Primeiro número: '))
    y = float(input('Segundo número: '))
    soma = x + y
    print('Soma: ',soma)

continuar = 1

while continuar:
    if continuar:
        soma()
    continuar = int(input("Digite 0 se desejar encerrar ou qualquer outro numero para continuar: "))