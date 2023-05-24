'''
    * - corresponde a zero ou mais elementos.Ou seja, pode existir ou não

    Neste exemplo, vamos supor que entre o DDD e o número de telefone
    possa existir zero, um, dois, três ou inúmeros espaços em branco

    xx yyyy-zzzz
    xxyyyy-zzzz
    xx  yyyy-zzzz
    xx       yyyy-zzzz

    Para isso usamos o asterisco(*) em nossa Regex

'''
import re
while True:
    texto = input("Digite sua string: " )

    minhaRegex = re.compile(r'\d{2}( )*\d{4}-?\d{4}')
    resultado = minhaRegex.search(texto)
    print(resultado.group())