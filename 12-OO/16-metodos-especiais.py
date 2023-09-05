'''
    MÉTODOS ESPECIAIS (SPECIAL METHODS):

    Estes 2 métodos são muito parecidos, mas tem finalidades diferentes. Ambos
    retornam uma string ao tentar imprimir o objeto.
    __str__ é usado para criar uma representação legível por humanos,
    __repr__ é usado para criar uma representação não ambígua do objeto.

    Você pode implementar um ou ambos, dependendo das suas necessidades,
    mas é uma boa prática implementar pelo menos __repr__ para fins de depuração.
    *** Se os dois métodos estiverem declarados, __str__ terá preferência.

    __eq__ compara o valor dos atributos dos objetos definidos na declaração do método
    __hash__ Retorna um número inteiro(positivo ou negativo) único para o atributo do objeto
    __bool__ e __len__ Retorna verdadeiro ou falso. Na ausência de bool o __len__ é procurado
    __del__ se declarado é executado após o garbage collector destruir o objeto
'''
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'__rpr__Person("{self.first_name}","{self.last_name}",{self.age})'

    def __str__(self):
        return f'__str__Person{self.first_name},{self.last_name},{self.age}'

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age
        return False
    def __hash__(self):
        return hash(self.first_name)

    def __bool__(self):
        if self.age < 18 or self.age > 65:
            return False
        return True
    def __del__(self):
        print('__del__ was called')
''' def __eq__(self, other):
        return self.age == other.age'''

person = Person('John', 'Doe', 25)
john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 25)
mary = Person('Mary', 'Doe', 27)

#__str__ e __repr__
print(person)#Sem o método __str__ mostra o endereço de memória, com o método exibe uma string formatada

#__eq__
print(john == jane)# True, sem o método __eq__ seria False, pois são objetos diferentes
print(john == mary)# False
print(john == 25)# False, pois o inteiro 25 não é um objeto da classe Person

#__hash__
print(hash(john))# 7900537227961911167
print(hash(jane))# 4012414512227509544
print(hash(mary))# -1061679634863054657

#__bool__
pessoa = Person('Jane','Austen', 16)
print(bool(pessoa))# False

