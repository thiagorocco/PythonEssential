''' 
    Exercício de Regex
    Faça um script que detecte números no formato:
    (xx) yyyy-zzzz
    (xx) yyyyzzzz 
'''
import re

while True:
    texto = input('Informe sua string: ')
    minhaRegex = re.findall(r'\(\d{2}\) \d{4}-\d{4}|\(\d{2}\) \d{8}',texto)
    print(minhaRegex)