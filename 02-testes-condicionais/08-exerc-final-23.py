'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                    Até 5 Kg                 Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
    receberá ainda um desconto de 10% sobre este total. 
    
    Escreva um algoritmo para ler a quantidade (em Kg) de morangos e
    a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''
apple = float(input('Quantos Kg de Maçã irá comprar?: '))
strawberry = float(input('Quantos Kg de Morango irá comprar?: '))

totalApple = 0
totalStrawberry = 0
desconto = 0

if apple <= 5:
    totalApple = apple * 1.8
else:
    totalApple = apple * 1.5

if strawberry <= 5:
    totalStrawberry = strawberry * 2.5
else:
    totalStrawberry = strawberry * 2.2

totalWeight = apple + strawberry
totalBuy = totalApple + totalStrawberry

if totalWeight > 8.00 or totalBuy > 25:
    desconto = totalBuy * 0.10

totalBuy = totalBuy - desconto

print('Valor a ser pago pelo cliente: R$',totalBuy)

