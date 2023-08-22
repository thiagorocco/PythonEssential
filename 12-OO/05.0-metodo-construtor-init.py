'''
Método construtor é o método que é executado automaticamente
ao chamar um objeto.

Pode conter parametros ou não

O método construtor __init__ serve para criar logo um objeto 
fazendo o necessário e obrigatório.

'''
class Carro:
    def __init__(self, nome, num):
        self.nome = nome
        self.portas = num
        print(self.nome,' criado! Ele tem ',self.portas,' portas')

palio = Carro('Palio',2)