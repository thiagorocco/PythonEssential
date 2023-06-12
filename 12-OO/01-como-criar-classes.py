class MinhaClasse:

    nome = 'Thiago'
    idade = 33
    sexo = 'm'

objeto = MinhaClasse
print('Nome: ', objeto.nome)


class Carro:
    def __init__(self):
        print('Carro criado')

#Objeto instanciado com parenteses e sem parenteses
#O primeiro vai executar o método construtor enquanto o segundo não
corolla = Carro()
civic = Carro