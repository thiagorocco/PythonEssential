'''
     + - Indica que o caracter tem que ocorrer pelo menos uma vez
     Ou seja, o caractere tem que existir, diferente do asterisco

    No exemplo abaixo se não tiver um espaço em branco entre o 
    DDD e o número de telefone teremos um erro

'''
import re

while True:
    texto = input("Digite sua string: " )

    minhaRegex = re.compile(r'\d{2}( )+\d{4}-\d{4}?')
    resultado = minhaRegex.search(texto)
    print(resultado.group())