'''
    self.count -> vai atuar em um objeto, especificamente
    Funcionario.count -> todos os objetos vão atuar numa mesma variável, o atributo de classe
'''
class Funcionario:
    
    #Atributo de classe
    count = 0

    def __init__(self,nome):
        self.__nome = nome
        print(nome,'contratado')
        Funcionario.count += 1
        print('Número de funcionários',Funcionario.count)

op = 1
func = []
while op:
    op = int(input('0.Sair\n1.Criar funcionário\n'))
    if op == 1:
        nome = input('Nome: ')
        func.append(Funcionario(nome))