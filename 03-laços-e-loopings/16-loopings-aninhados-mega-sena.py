'''
    Faça um script em Python que exiba todos os possíveis palpites da Mega-Sena.
    
    Dados:
    Cada palpite possui 6 dezenas
    As dezenas variam de 1 até 60
    Não pode repetir dezena
'''
import random

n1 = random.randint(1,60)
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0 

control = True
flow = True

while control == True:
    while flow == True:
        n2 = random.randint(1,60)
        if n2 != n1:
            flow = False
    
    flow = True
    while flow == True:
        n3 = random.randint(1,60)
        if n3 != n1 and n3 != n2:
            flow = False
    
    flow = True
    while flow == True:
        n4 = random.randint(1,60)
        if n4 != n1 and n4 != n2 and n4!=n3:
            flow = False
    
    flow = True
    while flow == True:
        n5 = random.randint(1,60)
        if n5 != n1 and n5 != n2 and n5!=n3 and n5!=n4:
            flow = False

    flow = True
    while flow == True:
        n5 = random.randint(1,60)
        if n5 != n1 and n5 != n2 and n5!=n3 and n5!=n4:
            flow = False
    
    flow = True
    while flow == True:
        n6 = random.randint(1,60)
        if n6 != n1 and n6 != n2 and n6!=n3 and n6!=n4 and n6!=n5:
            flow = False
    control = False

print('Dezenas da mega-sena: ',n1,'-',n2,'-',n3,'-',n4,'-',n5,'-',n6,'.')