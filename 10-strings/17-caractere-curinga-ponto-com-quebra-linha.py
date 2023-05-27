'''
    *** Fazer caractere curinga ponto reconhecer a quebra de linha como um caractere
    use basta passarmos o valor re.DOTALL, como segundo argumento da re.compile()
'''
import re

texto = 'Meu primeiro texto\nImediato'
semQuebra = re.findall(r'.*ato',texto)
comQuebra = re.findall(r'.*ato',texto,re.DOTALL)
print('Texto integral: ', texto)
print('Texto sem considerar a quebra de linha: ', semQuebra)
print('Texto considerarando a quebra de linha: ', comQuebra)