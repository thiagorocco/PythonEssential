class MinhaClasse:

    nome = 'Thiago'
    idade = 33
    sexo = 'm'

    def __init__(self,time_futebol, manequim):
        self.time_futebol = time_futebol
        self.manequim = manequim

objeto = MinhaClasse('Coritiba','M')
print('Nome: ', objeto.nome)
print(f'Torce para o {objeto.time_futebol} e veste {objeto.manequim}')


class Carro:
    def __init__(self):
        print('Carro criado')

    @staticmethod
    def consumo(a,b):
        return a*b
#Objeto instanciado com parenteses e sem parenteses
#O primeiro vai executar o método construtor enquanto o segundo não
corolla = Carro()
civic = Carro
print('Consumo = ',Carro.consumo(10,2))