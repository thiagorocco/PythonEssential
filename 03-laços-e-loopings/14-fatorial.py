numero = int(input('Informe um número inteiro para calcular a sua fatorial: '))
fat = numero
n = numero

while n > 1:
    fat = fat * (n -1)
    n -= 1

print('Fatorial de ',numero,' = ',fat)