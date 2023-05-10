#rstrip -> remove um caracter de uma string, vamos remover o \n(quebra de linha)
path = 'C:/PythonCodes/PythonProgressivo/09-arquivos/bandas.txt'
meuArquivo = open(path,'r')
bandas = meuArquivo.readlines()
for banda in bandas:
    print(banda)
meuArquivo.close()
'''
Se imprimirmos cada valor da lista o resultado será o seguinte: 
----------------
Rush

Iron Maiden

Led Zeppelin
----------------
Por que o espaço em branco entre as linhas? Porque ao final de cada linha
existe o caracter \n(quebra de linha) e a função print por si só também já
possui nativamente '''
#Para resolver usamos rstrip
for banda in bandas:
    print(banda.rstrip('\n'))
meuArquivo.close()
#Ou então retirar a quebra de linha da função print com end=''
for banda in bandas:
    print(banda,end='')
meuArquivo.close()
