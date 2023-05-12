path = 'C:\\PythonCodes\\PythonProgressivo\\09-arquivos\\linguagens.txt'
arquivo = open(path, 'r')
num = int(input("Numero de linguagens: "))
count=0

for linha in arquivo:
    if count<num:
        print(count+1,':',linha.rstrip('\n'))
        count=count+1
    else:
        break

arquivo.close()