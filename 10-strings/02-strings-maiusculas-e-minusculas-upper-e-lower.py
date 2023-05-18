texto = 'Curso de Python Progressivo'
#string.upper() - Transforma todos os caracteres em maiúsculos
#string.lower() - Transforma todos os caracteres em minúsculos
maiusculas = texto.upper()
minusculas = texto.lower()

print(texto)
print(maiusculas)
print(minusculas)

#Verificar se toda a string é maiúscula ou minúscula com isupper() e islower()
print(texto.islower()) #False
print(maiusculas.isupper()) #True
print(minusculas.islower()) #True

teste = input('Digite algum texto: ')

if teste.isupper():
    print('Tudo maiúsculo')
elif teste.islower():
    print('Tudo minúsculo')
else:
    print('Misturado')