'''
Você fornece a temperatura em graus Fahrenheit, seu programa conversar para Celsius e exibe na tela.
'''
fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))

celsius = (fahrenheit-32)/1.8

print('Graus em Celsius =  %.1f' %celsius)