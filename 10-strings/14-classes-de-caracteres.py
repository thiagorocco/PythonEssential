'''
    Nos códigos anteriores usamos o \d para fins didáticos, ele é um classe, mas apenas
    uma das classes de caracteres, vejamos abaixo as outras classes de caracteres:

    \d - Qualquer dígito de 0 a 9
    \D - Qualquer caractere que não seja um dígito (contrário de \d)
    \w - Qualquer letra, dígito ou o caractere underscore (qualquer caractere de uma palavra)
    \W - Qualquer caractere que não seja uma letra, um dígito ou o underscore (contrário de \w)
    \s - Qualquer espaço, tabulação ou caractere de quebra de linha,  ou seja, qualquer 
    espaçamento
    \S - Qualquer caractere que não seja um espaço, uma tabulação ou uma quebra de linha 
    (contrário de \S)

    Vamos supor que queiramos detectar o seguinte padrão:
    Um ou mais números
    Um espaçamento
    Um ou mais caractere

    Para detectar um ou mais número: \d+
    Para detectar apenas um espaçamento: \s
    Para detectar um ou mais caractere, seja dígito ou não: \w+

    Logo, nossa regex é: \d+\s\w+
'''
#Você também pode criar suas próprias classes de caracteres:
'''
    Por exemplo, se desejar detectar dígitos de 0 até 5, use a Regex:
    r'[0-5]'

    Para detectar vogais minúsculas:
    r'[aeiou]' ou r'[a-u]

    Para detectar tanto letras minúsculas como maiúsculas:
    r'[a-zA-Z]'
    
    Para detectar um padrão formado só por letras do alfabeto e dígitos:
    r'[a-zA-Z0-9]'

    E para detectar o CONTRÁRIO do que você deseja, basta inserir o acento circunflexo antes ^.
    Por exemplo, detecta tudo menos letras do alfabeto e dígitos:
    r'[^a-zA-Z0-9]'

    Detectar tudo que não é dígito:
    r'^\d' que é o mesmo de r'\D'
    
'''