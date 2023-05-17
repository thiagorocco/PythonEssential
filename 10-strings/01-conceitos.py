'''
Lista de caracteres especiais em Python:
    \\ - Exibe uma barra
    \' - Exibe a aspa simples
    \" - Exibe a aspa dupla
    \a - Dá um bipe
    \b - Retrocesso
    \f - Avanço
    \n - Caractere de nova linha (enter)
    \r - Carriage return
    \t - Tab horizontal
    \v - Tab vertical
'''
#Acessando elementos de uma string
texto = 'Curso de Python Progressivo'
for caracter in texto:
    print(caracter)
#Print sem quebrar linha com end=''
for caracter in texto:    
    print(caracter,end='')

#Pode acessar diretamente caractere por caractere, como se fosse uma lista:
print(texto[0])

#Exibindo partes da string com texto[inicio:fim], texto[a partir de:] e texto[:até tantas posições]
print(texto[0:5])#resultado: 'Curso ' 
print(texto[6:])#resultado: 'de Python Progressivo 
print(texto[:7])#resultado: 'Curso d' 