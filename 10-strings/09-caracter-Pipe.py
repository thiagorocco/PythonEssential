'''
    Caractere Pipe(|) a barra vertical.
    Significado de "OU" nas Regex

    Seguindo o exemplo dos códigos anteriores usando número de telefone,
    vamos detectar os seguintes formatos de números:

    xx yyyy-zzzz
    xx yyyyzzzz
    xxyyyyzzzz

'''
import re
while True:
    texto = input('Digite sua string: ')
    minhaRegex = re.findall(r'\d{2} \d{4}-\d{4}|\d{2} \d{8}|\d{10}',texto)
    print('Gostei dessas ',minhaRegex)