'''
    As regular expressions (também conhecidas pela abreviação Regex) 
    são um padrão de um texto que vamos procurar.
'''
#Função sem expressão regular
def eTelefone(numero):
    #verifica se tem 9 dígitos
    if len(numero) != 9:
        return False
    #verifica se os dígitos 0, 1, 2 e 3 NÃO são númericos
    for index in range(0,4):
        if numero[index].isdecimal() is not True:
            return False
    #verifica se o 4º dígito NÃO é hífen  
    if numero[4] != '-':
        return False
    for index in range(5,9):
        if numero[index].isdecimal() is not True:
            return False
    print("Numero detectado: ", numero)
    return True
 
while True:
 numero = input("Numero no formato 'xxxx-yyyy': " )
 
 for i in range( len(numero)):
    pedaco=numero[i:i+9]
    eTelefone(pedaco)