#Há duas formas de alterarmos chaves no Python

#First Way - Define uma nova e depois apaga a antiga
notas = {
    'João':9.0,
    'Maria':10,
    'José':4
}
print('*** Primeira maneira ***')
print(notas)

notas['Marya'] = notas['Maria']
del notas['Maria']
print(notas)

#Second Way - Use o método Pop, pois ele retorna a key e depois descarta automaticamente
idades = {
    'thiago': 33,
    'Cris': 34,
    'Joanir': 68
}
print('*** Segunda maneira ***')
print(idades)
idades['Thiago'] = idades.pop('thiago')
print(idades)