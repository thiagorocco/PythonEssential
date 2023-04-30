'''Crie um programa em Python que peça a nota do aluno, que deve ser um float entre 0.00 e 10.0

Se a nota for menor que 6.0, deve exibir a nota F.
Se a nota for de 6.0 até 7.0, deve exibir a nota D.
Se a nota for entre 7.0 e 8.0, deve exibir a nota C.
Se a nota for entre 8.0 e 9.0, deve exibir a nota B.

Por fim, se for entre 9.0 e 10.0, deve exibir um belo de um A.'''

nota = float(input('Informe uma nota entre 0 e 10: '))

if nota < 6.0:
    print('F')
elif nota >= 6.0 and nota < 7.0:
    print('D')
elif nota >=7.0 and nota < 8.0:
    print('C')
elif nota >=8.0 and nota < 9.0:
    print('B')
elif nota >=9.0:
    print('Parabéns! Você tirou um A!!!')    
