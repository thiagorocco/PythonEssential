'''
21. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" 
    
    O programa deve no final emitir uma classificação sobre a 
    participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
    ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
     
     Caso contrário, ele será classificado como "Inocente".
'''
respostas = 0
perg1 = input('Telefonou para a vítima? S/N: ')
perg2 = input('Esteve no local do crime? S/N: ')
perg3 = input('Mora perto da vítima? S/N: ')
perg4 = input('Devia para a vítima? S/N: ')
perg5 = input('Já trabalhou com a vítima? S/N: ')

if perg1 == 's' or perg1 == 'S':
    respostas = respostas+1
if perg2 == 's' or perg2 == 'S':
    respostas = respostas+1
if perg3 == 's' or perg3 == 'S':
    respostas = respostas+1
if perg4 == 's' or perg4 == 'S':
    respostas = respostas+1
if perg5 == 's' or perg5 == 'S':
    respostas = respostas+1

if respostas == 5:
    print('Assassino')
elif respostas >= 3 and respostas <= 4: 
    print('Cúmplice')
elif respostas == 2: 
    print('Suspeito')
else:
    print('Inocente')
