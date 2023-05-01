lista01 = [1,2,3,4]

''' *** JEITO ERRADO *** '''
# lista02 vai apontando para o mesmo endereço de memória de lista01
lista02 = lista01

print('Valores originais')
print('Lista01 = ',lista01)
print('Lista02 = ',lista02)

lista02[0] = 99

# Dessa forma, ao mudar um elemento de lista02, automaticamente mudará o valor de lista01 e vice-versa
print('***Jeiro Errado *** Valores após a modificação do valor da posição 0 de lista02 para 99:')
print('Lista01 = ',lista01)
print('Lista02 = ',lista02)

''' *** JEITO CERTO DIFÍCIL - For + append *** '''
lista03 = []
for item in lista01:
    lista03.append(item)

lista03[0] = 23
print('***Jeito Certo Difícil*** Valores após a modificação do valor da posição 0 de lista03 para 23: ***')
print('Lista01 = ',lista01)
print('Lista03 = ',lista03)

''' *** JEITO CERTO FÁCIL - listanova = []+lista *** '''
lista04 = [] + lista01

lista04[0] = 33
print('***Jeito Certo Fácil *** Valores após a modificação do valor da posição 0 de lista04 para 33: ***')
print('Lista01 = ',lista01)
print('Lista04 = ',lista04)