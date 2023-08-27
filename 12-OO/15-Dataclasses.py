from dataclasses import dataclass
class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

    def __repr__(self):
        return f"Pessoa(nome='{self.nome}', idade={self.idade}, cidade='{self.cidade}')"

    def __eq__(self, other):
        if isinstance(other, Pessoa):
            return (
                    self.nome == other.nome and
                    self.idade == other.idade and
                    self.cidade == other.cidade
            )
        return False

@dataclass
class PessoaDataClass:
    nome: str
    idade: int
    cidade: str

# Instâncias da classe Pessoa
pessoa1 = Pessoa("Alice", 30, "São Paulo")
pessoa2 = Pessoa("Bob", 25, "Rio de Janeiro")
print(pessoa1)
print(pessoa1 == pessoa2)

# Instâncias da classe PessoaDataClass
pessoa3 = PessoaDataClass("Thiago",33,"Piraquara")
pessoa4 = PessoaDataClass("Cristiane",34,"Piraquara")
print(pessoa3)
print(pessoa3 == pessoa4)

# Observe que o resultado é o mesmo de usar Pessoa e PessoaDataClass,
# a diferença é que a segunda classe é muito mais enxuta são apenas 4 linhas contra
# 16 linhas da primeira.