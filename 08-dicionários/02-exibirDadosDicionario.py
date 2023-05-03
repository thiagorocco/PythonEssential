'''
Podemos usar três métodos:

    Método items(): exibe todos os itens, ou seja, os pares chave-valor
    Método keys(): exibe todas as chaves de um dicionário
    Método values(): exibe todos os valores de um dicionário

'''
notas={'joao'   :  9,
       'maria'  : 10,
       'zezinho': 4}

print('Exibindo os items:')
print(notas.items())
print('Exibindo as chaves:')
print(notas.keys())
print('Exibindo os valores:')
print(notas.values())

#Exibindo os dados com um laço for
for nome in notas.keys():
    print(nome,'tirou nota:',notas[nome])