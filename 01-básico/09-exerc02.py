'''
A loja percebeu que não quer dar 20% em tudo. 
Quer dar 20% em algumas coisas, 10% em outra, nada em outro produto e até 30% em alguns outros produtos.
Crie um script em Python que pergunte o preço original e o desconto que deve ser concedido.
Ele deve mostrar a tabela igual a do exercício anterior.
'''
priceOriginal = float(input('Digite o preço do produto: '))
percentualDesconto = float(input('Digite o percentual de desconto: '))
percentualDesconto = percentualDesconto/100
valorDesconto = priceOriginal * percentualDesconto
valorFinal = priceOriginal - valorDesconto

print('Valor original: ',priceOriginal)
print('Valor do desconto: ',valorDesconto)
print('Valor final: ',valorFinal)