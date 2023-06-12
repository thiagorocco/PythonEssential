import random

class CaraCoroa:
    def __init__(self):
        self.lado = 'Cara'
    
    def lancar(self):
        if (random.randint(0,1))%2==0:
            self.lado = 'Cara'
        else:
            self.lado = 'Coroa'
        return self.lado

class Dado:
    def __init__(self):
        self.lado = 1
    def lancar(self):
        return random.randint(1,6)

moeda = CaraCoroa()
dado = Dado()
op = 1

while op:
    op = int(input('0.Sair\n'
            '1. Lançar Moeda\n'
            '2. Lançar Dado\n'))
    if op == 1:
        print(moeda.lancar())
    if op == 2:
        print(dado.lancar())