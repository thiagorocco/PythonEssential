#04. Crie uma função que recebe 3 números e exiba o maior deles.
def maior(n1,n2,n3):
    if n1 > n2 and n1>n3:
        print('O maior número informado é o ',n1)
    elif n2 > n1 and n2 > n3:
        print('O maior número informado é o ',n2)
    else:
        print('O maior número informado é o ',n3)

n1 = int(input('Informe o 1.o número inteiro: '))
n2 = int(input('Informe o 2.o número inteiro: '))
n3 = int(input('Informe o 3.o número inteiro: '))

maior(n1,n2,n3)
