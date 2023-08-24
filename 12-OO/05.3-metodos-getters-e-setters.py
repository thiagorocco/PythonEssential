'''class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def preco(self):
        return self._preco
    #Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$',''))

        self._preco = valor

p1 = Produto('Camiseta',50)
p1.desconto(10)
print(p1.preco)

p2 = Produto('Caneca','15')
p2.desconto(10)
print(p2.preco)'''
class Produto:
    def __init__(self, nome, preco):
        self._nome = nome  # Atributo privado
        self._preco = preco  # Atributo privado

    def desconto(self, percentual):
        self._preco = self._preco - (self._preco * (percentual / 100))

    # Getter
    @property
    def nome(self):
        return self._nome

    # Setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor

# Exemplo de uso
produto = Produto("Produto1", 100.0)
print(f"Nome: {produto.nome}, Preço: R${produto.preco}")

produto.desconto(10)
print(f"Nome: {produto.nome}, Preço com desconto: R${produto.preco}")
