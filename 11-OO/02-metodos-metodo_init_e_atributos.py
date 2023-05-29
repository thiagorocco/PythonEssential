'''
    Note que o primeiro parâmetro de todo método, é self.
    Se quiser retornar um atributo de uma classe, também use o self:
    self.portas
'''
class Carro:
    portas = 4
    automatica = ''
 
    def __init__(self):
        print("Carro criado")
    def exibirPortas(self,tipoPorta):
        self.automatica = tipoPorta
        return self.portas,self.automatica
 
veloster = Carro()
print("Numero de portas:", veloster.exibirPortas('Automática'))
