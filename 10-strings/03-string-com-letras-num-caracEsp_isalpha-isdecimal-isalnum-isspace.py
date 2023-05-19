'''
Certamente você já viu algum formulário ou programa que pede somente determinados tipos
de caracteres. Por exemplo, no campo de nome, devemos receber apenas letras.

Já no campo CPF ou data, pedimos e detectamos se a pessoa digitou apenas números.

Alguns cadastros de senha, precisamos fornecer tanto letras como números e algum caractere especial. 
Podemos 'tratar' e analisar a entrada do usuário com os métodos vistos hoje.
'''

texto = input("Digite uma string: ")

if texto.isalpha():
    print("Tudo tudo letra")
elif texto.isdecimal():
    print("Tudo numero")
elif texto.isalnum():
    print("Numeros e letras")
elif texto.isspace():
    print("Composto só de espaço, e/ou tabulação e/ou quebra de linha")
else:
    print("Vazia ou caractere especial")