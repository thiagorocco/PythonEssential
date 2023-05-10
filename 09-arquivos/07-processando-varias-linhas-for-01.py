path = 'C:/PythonCodes/PythonProgressivo/09-arquivos/linguagens.txt'
arquivo = open(path,'r')
linguas = arquivo.readlines()

print('Existem ',len(linguas),'linguanges de programação. Quantas deseja ver?')
num = int(input())

for count in range(num):
    print(str(count+1),':',linguas[count].rstrip('\n'))

arquivo.close()

#Se não tiver um for que controle o número de linhas e o número de linguagens digitadas
#ocorrerá um erro ao acessar o index do array que não existe. Ex: num= 800, vai dar erro
