def fatorial(x):
    if x==0:
        return 0
    if x==1:
        return 1
    else:
        return x * fatorial(x-1)

x = int(input('Informe um número: '))
print('Fatorial de ',x,' = ',fatorial(x))