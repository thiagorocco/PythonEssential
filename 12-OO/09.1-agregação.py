'''
    Na agregação, as classes existem de forma independente, porém
    para o correto funcionamento, ambas dependem uma da outra.

    Ex: Carro e rodas. Não faz muito sentido carro sem rodas. As rodas sozinhos fazem algum sentido
    Carrinho de Compras e Produto. Não faz muito sentido Carrinho sem produtos. Os produtos sozinhos fazem sentido

'''
from agregacaoClasses import CarrinhoDeCompras
from agregacaoClasses import Produto

carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta',50)
p2 = Produto('iPhone',10000)
p3 = Produto('Caneca',40)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.lista_produto()
print('Total: R$',carrinho.soma_total())