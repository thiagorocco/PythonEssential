'''
    Início da string: ^
    Um ou mais dígitos: \d+
    Final de string: $
'''
import re

# *** Início da string *** 
# O script abaixo detecta a palavra "Olá", no início de qualquer string:


texto = input("Início de string Olá - Digite sua string: " )

minhaRegex = re.compile(r'^Ol(á|a)')
resultado = minhaRegex.search(texto)
print(resultado.group())

texto = input("Início de string geral - Digite sua string: " )

#Informa a primeira palavra da string
minhaRegex = re.compile(r'^(\w)+\s')
resultado = minhaRegex.search(texto)
print(resultado.group())

# *** Final de String $ ***

#Detecta se os quatro últimos caracteres de uma string são: 
# ponto e três letras
texto = input("Final de string - Digite sua string: " )

minhaRegex = re.findall(r'\.\w{3}$', texto)
print(minhaRegex)

#Detecta padrões compostos somente por dígitos, com um ou mais presente, senão tiver dígitos dá erro
texto = input("Padrões compostos só por dígitos - Digite sua string: " )

minhaRegex = re.compile(r'^(\d)+$')
resultado = minhaRegex.search(texto)
print(resultado.group())