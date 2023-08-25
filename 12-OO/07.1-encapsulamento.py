'''
    public - Acessíveis de qualquer lugar, dentro ou fora da classe
    protected - Acessíveis apenas por classes que herdam a classe pai
    private - Acessíveis apenas dentro da própria classe

    Esse é o conceito da OO clássica, e como fica isso em Python???

    No Python existem convenções e não restrições:

    _ recomenda mas não impede o acesso diretamente
    __ impede o acesso direto, porém se usar _NOMEDACLASSE__nomeatributo conseguirá acessar

    O ideal é usar um método getter para acessar esses atributos
'''
class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    @property
    def dados(self):
        return self.__dados
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id:nome})

bd = BaseDeDados()
bd.inserir_cliente(1,'Otávio')
bd.inserir_cliente(2,'Miranda')
bd.inserir_cliente(3,'Rose')
#print(bd._BaseDeDados__dados)
print(bd.dados)