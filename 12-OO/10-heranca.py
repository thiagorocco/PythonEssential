'''
    Na herança as subclasses, classes que herdam da classe mãe
    todos métodos declaradas nela, inclusive o construtor

    Porém essas herdeiras podem ter seus próprios métodos e atributos
'''
class Veiculo:
    def __init__(self,tipo,modelo,km):
        self.tipo = tipo
        self.modelo = modelo
        self.km = km

class Carro(Veiculo):
    def __init__(self, tipo, modelo, km, portas):
        Veiculo.__init__(self, tipo, modelo, km)
        self.portas = portas
    def exibe(self):
        print(self.tipo,"modelo",self.modelo,'com',self.km,'km rodados e ',self.portas,'portas')

class Moto(Veiculo):
    def __init__(self, tipo, modelo, km, cilindrada):
        Veiculo.__init__(self, tipo, modelo, km)
        self.cilindrada = cilindrada
    def exibe(self):
        print(self.tipo,"modelo",self.modelo,'com',self.km,'km rodados e ',self.cilindrada,'cilindrada')

palio = Carro('Carro','Palio','10000',2)
palio.exibe()
fazer = Moto('Moto','Fazer','5000',350)
fazer.exibe()