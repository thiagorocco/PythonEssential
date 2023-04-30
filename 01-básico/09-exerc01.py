'''
Criar um programa em Python que pede o preço original de um produto e dá 20% de desconto.
Você deve mostrar uma tabela contendo:
Preço original do produto
Valor do desconto em R$ (tipo 'Você ganho R$ xx,xx de desconto')
Valor do produto com o desconto
'''
priceOriginal = float(input('Digite o preço do produto: '))
valorDesconto = priceOriginal * 0.2
valorFinal = priceOriginal - valorDesconto

print('Valor original: ',priceOriginal)
print('Valor do desconto: ',valorDesconto)
print('Valor final: ',valorFinal)
