'''
 ** get(key, value):
    Antes de trabalhar com um dicionário, 
    especificamente quando queremos adicionar mais items ou acessar uma chave, 
    é necessário verificar se uma chave já existe.

 ** setdefault
    Verifica se a chave já existe, se não existir cria uma nova chave com valor,
    se já existir simplesmente não faz nada

'''

notas={'João'   :  9,
       'Maria'  : 10,
       'José': 4}

#Testando Método get
if notas.get('Ralf') == None:
    print('Nao existe aluno "Ralf"')
else:
    print('Aluno existente')

#Testando Método setdefault
notas.setdefault('Maria', 8)
notas.setdefault('Bruce', 8)
print(notas)