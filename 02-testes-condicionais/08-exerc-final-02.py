'''
2. Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular 
a média do aluno e dar o seguinte resultado:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2
if media == 10:
    print('Aprovado com distinção')
elif media >= 7.0:
    print('Aprovado')
else:
    print('Reprovado')    