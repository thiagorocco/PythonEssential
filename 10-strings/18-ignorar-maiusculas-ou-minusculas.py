'''
    Ignorando caracteres maiusculas e minusculas em 
    uma busca com re.IGNORECASE ou re.I
'''

import re

texto = input('Digite sua string aqui: ')

#Por mais que na regex esteja ato em minúscula, se digitar maiuscula também funciona
minhaRegex = re.compile(r'.*ato',re.IGNORECASE)
resultado = minhaRegex.search(texto)
print(resultado.group())