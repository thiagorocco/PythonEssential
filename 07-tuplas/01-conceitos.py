#Tuplas são listas com elementos imutáveis
'''
    Nas listas, os valores vinham entre colchetes: [ ]
    
    Nas tuplas, os valores vem enter parenteses: ( )
'''

#Exemplo de tupla:
aluno = ('Joaozinho', 10, 9)

#Caso queria criar uma tupla com apenas um elemento, deixe uma vírgula no final
#para o Python entender que não é apenas um número entre parenteses
nota = (9.0,)

#Recomendação: usar uma tupla sempre que tiver valores, items, que nunca serão mudados, serão constantes.
#Exemplo: Informações de conexão com BD como servidor, senha, nome do banco

#Transformar tupla em lista
'list() que recebe uma tupla e transforma em lista.'
aluna = list(aluno)

print('Aluno(Tupla): ',aluno)
print('Aluna(lista): ',aluna)

#Transformar lista em tupla
'tuple() que recebe uma lista e retorna uma tupla'
estudante = tuple(aluna)

print('Estudante(Tupla): ',estudante)

#Acessando elementos da tupla:
print('Nome: ',aluno[0])
print('Nota1: ',aluno[1])
print('Nota2: ',aluno[2])
