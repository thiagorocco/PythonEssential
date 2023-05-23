''' 
    Aplicando Regex 

    Regex de dígito \d
    Logo uma regex que detecta nosso número de telefone é:
    \d\d\d\d-\d\d\d\d

    Se colocarmos um valor entre chaves, dizemos que aquela regex deve
    'bater' aquele número de vezes:
    \d{4}-\d{4}

    E com DDD ? As expressões abaixo funcionariam
    \d{2} \d{4}-\d{4}   :bate com xx yyyy-zzzz
    (\d{2}) \d{4}-\d{4}: bate com (xx) yyyy-zzzz
    (\d{2}) \d{8} : bate com xx yyyyzzzz

    Módulo re - COleção para tratar e lidar com regex - Importe-o

    compile e group: acha somente a primeira ocorrência e retorna uma string
    findall: acha todas as ocorrências e retorna um array com as strings

 '''
from queue import Empty
import re
while True:
    texto = input('Número no formato "xxxx-yyyy": ') 
    minhaRegex = re.compile(r'\d{4}-\d{4}')
    resultado = minhaRegex.search(texto)
    if resultado != None:
        print(resultado.group())
        break

while True:
    texto = input("Numero no formato 'xxxx-yyyy': " )
    minhaRegex = re.findall(r'\d{4}-\d{4}', texto)
    if not not minhaRegex:
        print(minhaRegex)
        break