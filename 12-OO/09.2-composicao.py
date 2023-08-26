'''
Nosso mundo é um punhado de objetos, compostos de outros objetos dentro, além de lidar com outros objetos de fora.

Damos a isso o nome de composição: combinação de objetos, quando instanciamos objetos de uma classe dentro de outra,
 quando usamos objetos de uma classe dentro de outros objetos.

Vamos ver um exemplo real de situação e código, para entendermos melhor o que é composição na prática.

*** Quando uma classe usa outra classe dentro dela. Ex: Empresa usa Funcionario
*** Ao remover o objeto de uma o objeto da outra também é apagado. EX: Acabou Empresa, acabou Funcionario
'''
class Funcionario:
    def __init__(self, nome):
        self.__nome = nome
   
    def retornaNome(self):
        return self.__nome

class Empresa:
 func = []
 def __init__(self):
  print("Empresa Tabajara em funcionamento")
 
  while True:
   print("1. Contratar")
   print("2. Exibir lista de funcionarios")
   op=int( input() )
   
   if op==1:
    self.contratar()
   elif op==2:
    self.exibir()
   else:
    print("Opçao invalida")
 
 def contratar(self):
  nome = input("Nome: ")
  self.func.append(Funcionario(nome))
 
 def exibir(self):
  for funcionario in self.func:
   print(funcionario.retornaNome())

Empresa()
