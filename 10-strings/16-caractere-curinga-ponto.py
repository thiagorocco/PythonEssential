'''

    O caractere de ponto . é dito curinga, pois ele substitui todo e qualquer caractere,
    exceto a quebra de linha \n

    *** Aplicações: 

        re.findall(r'.ato',texto) -> Uma letra antes de ato
        re.findall(r'..ato',texto) -> Duas letras antes de ato
        re.findall(r'...ato',texto) -> Três letras antes de ato
        re.findall(r'.*ato',texto) -> Todas as letras antes de ato
'''
import re

texto = input("Digite sua string: " )

minhaRegex = re.findall(r'.*ato', texto)
print(minhaRegex)

texto = 'String com quebra de linha\nSegunda linha'
print(texto)
re.compile(texto,re.DOTALL)