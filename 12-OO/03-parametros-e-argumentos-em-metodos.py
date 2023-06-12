'''
A coisa que você mais deve se lembrar, ao trabalhar com métodos e atributos de uma classe,
é de usar o self.

Parametros: o self sempre vai estar lá seguido do parametro que queremos trabalhar
'''
class Carro:
    portas = 2

    def __init__(self):
        print('Carro criado')
    
    def definePortas(self, num):
        self.portas = num
    
    def exibePortas(self):
        return self.portas
 
carro = Carro()
num = int(input('Número de portas: '))
carro.definePortas(num)
print('Número de portas = ', carro.exibePortas())