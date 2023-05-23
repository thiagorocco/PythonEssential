'''
    As regular expressions (também conhecidas pela abreviação Regex) 
    são um padrão de um texto que vamos procurar.

    Elas podem facilitar muito o trabalho do programador

    Vejamos um exemplo sem expressão regular e com expressão regular
'''
''' *** Função sem expressão regular *** '''

#FUNCIONA PARA BOA PARTE DOS CASOS, MAS DÁ MUITO TRABALHO E NÃO COBRE TODA A NECESSIDADE

def eTelefone(numero):
    #verifica se NÃO tem 9 dígitos
    if len(numero) != 9:
        return False
    #verifica se os dígitos 0, 1, 2 e 3 NÃO são númericos
    for index in range(0,4):
        if numero[index].isdecimal() is not True:
            return False
    #verifica se o 4º dígito NÃO é hífen  
    if numero[4] != '-':
        return False
    #verifica se os dígitos 5,6,7 e 8 NÃO são númericos
    for index in range(5,9):
        if numero[index].isdecimal() is not True:
            return False
    print("Numero detectado: ", numero)
    return True

controle = True

while controle:
    numero = input("Numero no formato 'xxxx-yyyy': " )
 
    #laço que executa de 0 até o tamanho da variável numero
    for i in range( len(numero)):
        #pedaco receberá a posição de i até i+9 da variável número
        #dessa forma, a cada interação do laço, novos 9 dígitos são testados
        pedaco=numero[i:i+9]
        if(eTelefone(pedaco)):
            controle = False
            break
