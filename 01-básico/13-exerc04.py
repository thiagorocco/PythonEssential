'''
Um novo modelo de carro, super econômico foi lançado.
Ele faz 20 km com 1 litro de combustível.
Cada litro de combustível custa R$ 5,00.

Faça um programa que pergunte ao usuário quanto de dinheiro ele tem 
e em seguida diga quantos litros de combustível ele pode comprar e 
quantos kilometros o carro consegue andar com este tanto de combustível.
'''
dinheiro = float(input('Quanto dinheiro você tem para o combustível?: '))
precoCombustivel = 5.00
litros = dinheiro/precoCombustivel
km = litros * 20

print('Você tem dinheiro para %.1f litros e poderá percorrer até %.1f km' %(litros,km))
