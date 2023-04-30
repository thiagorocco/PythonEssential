'''Exercício: Crie um programa em Python que peça dois números ao usuário.
Em seguida, você vai mostrar a soma, subtração, multiplicação, divisão, 
exponenciação e resto da divisão do primeiro número pelo segundo.
Tem que ficar bonitinho e organizadinho assim, o resultado:'''

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

soma = num1 + num2
subtra = num1 - num2
multi = num1 * num2
divi = num1 / num2
exp = num1 ** num2
resto = num1 % num2

print('Soma: ',soma)
print('Subtração: ',subtra)
print('Multiplicação: ',multi)
print('Divisão: ',divi)
print('Exponenciação: ',exp)
print('Resto da divisão: ',resto)