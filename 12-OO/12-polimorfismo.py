'''
    O objeto tem a capacidade de assumir diferentes formas (polimorfismo).

    Observe que o método da subclasse faz uma sobreposição, ele sobrepõe,
    passa por cima do método da superclasse.

'''
class Super:
    def hello(self):
        print("Olá, sou a superclasse!")

class Sub (Super):
    def hello(self):
        print("Olá, sou a subclasse!")

class Subsub(Sub):
    def hello(self):
        print('Olá, sou a Subsubclasse')

testeSuper = Super()
testeSub = Sub()
testeSubsub = Subsub()

testeSuper.hello()
testeSub.hello()
testeSubsub.hello()

