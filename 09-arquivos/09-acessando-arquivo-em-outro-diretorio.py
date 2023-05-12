import os
os.system('cls') or None

path = 'C:\\PythonCodes\\PythonProgressivo\\09-arquivos\\arquivos\\virus.txt'
arquivo = open(path,'r')

for linha in arquivo:
    print(linha.rstrip('\n'))

arquivo.close()