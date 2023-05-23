'''
Usando paretenses indicamos para o método compile que temos grupos
distintos em nossa Regex.

Dessa forma podemos acessar o grupo que desejarmos através do método group(número do grupo)

O método groups() sem informar parâmetros retorna uma tupla com todos os grupos separados

'''
import re
while True:
    texto = input('Digite sua String no formato xx yyyy-zzzz: ')
    minhaRegex = re.compile(r'(\d{2}) (\d{4}-\d{4})')
    resultado = minhaRegex.search(texto)

    print('Número detectado: ',resultado.group())
    print('DDD desse número: ',resultado.group(1))
    print('Número sem DDD: ',resultado.group(2))
    print('Tuplas com os elementos: ',resultado.groups())