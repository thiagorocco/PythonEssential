'''
    ? - Indica que o caractere é opcional/não obrigatório

    1. Pode usar logo ao lado do caracter:
    -?
    2. Ou ao lado do parenteses que enclausura o caractere
    (-)?
    A segunda prática não é obrigatória, mas é recomendada
'''
import re

while True:
    texto = input("Digite sua string: " )

    minhaRegex = re.compile(r'\d{2} \d{4}(-)?\d{4}')
    resultado = minhaRegex.search(texto)
    print(resultado.group())
