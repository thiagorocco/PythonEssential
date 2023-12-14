#03. Crie uma função que recebe 4 notas de um aluno, e exiba a média dele.
def media(n1,n2,n3,n4):
    print('Média = %.1f' %((n1+n2+n3+n4)/4))

n1 = float(input('Informe a 1.a nota: '))
n2 = float(input('Informe a 2.a nota: '))
n3 = float(input('Informe a 3.a nota: '))
n4 = float(input('Informe a 4.a nota: '))

media(n1,n2,n3,n4)