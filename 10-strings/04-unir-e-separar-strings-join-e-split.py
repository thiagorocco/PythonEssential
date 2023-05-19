from ntpath import join


lista = ['Curso','Python','Progressivo']
delimitador = ' '

#join: Pegar cada elemento da lista e concatena um no outro com o caractere(delimitador). 
#split: Separa cada elemento da string separados por um delimitador padrão ou informado em uma lista

print(delimitador.join(lista))
print('-'.join(lista))

texto = 'Curso Python Progressivo'
print(texto.split())

texto2 = '123PI456PI654'
print(texto2.split('PI'))

#Aqui separamos o texto a partir de '$' e depois unimos com o caracter ' '
texto3 = 'Curso$Python$Progressivo'
print(delimitador.join(texto3.split('$')))