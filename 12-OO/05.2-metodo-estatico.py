#Não precisa da instância e nem da classe
from random import randint

class Pessoa:
    ano_atual = 2023
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    @staticmethod
    def gera_id():
        rand =randint(10000,19999)
        return rand

p1 = Pessoa('Thiago',33)

#Formas de chamar o método estático

#com o objeto
print(p1.gera_id())
#Ou sem o objeto diretamente pela classe
print(Pessoa.gera_id())