'''
    raise - você cria uma exceção de acordo com uma regra definida
'''
num = 'Thiago'

if not type(num) is int:
    raise Exception('Somente números são permitidos')
else:
    print(num)