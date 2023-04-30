'''
10. Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''
dia_da_semana = int(input('Digite um número correspondente ao número da semana(1-7): '))

if dia_da_semana == 1:
    print('Domingo')
elif dia_da_semana == 2:
    print('Segunda-Feira')
elif dia_da_semana == 3:
    print('Terça-Feira')
elif dia_da_semana == 4:
    print('Quarta-Feira')
elif dia_da_semana == 5:
    print('Quinta-Feira')
elif dia_da_semana == 6:
    print('Sexta-Feira')
elif dia_da_semana == 7:
    print('Sábado')
else:
    print('Valor inválido')