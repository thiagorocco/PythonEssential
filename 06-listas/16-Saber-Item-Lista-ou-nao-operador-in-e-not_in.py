workingDays = ['Segunda','Terça','Quarta','Quinta','Sexta']

dia01 = 'Sexta'
dia02 = 'Domingo'

if dia01 in workingDays:
    print('Sim,',dia01,'é um dia útil')
else:
    print('Não,',dia01,'não é um dia útil')

if dia02 not in workingDays:
    print('Sim,',dia02,'não é um dia útil')
else:
    print('Não,',dia02,'é um dia útil')