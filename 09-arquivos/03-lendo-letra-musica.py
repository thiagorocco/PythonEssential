meuArquivo = open('C:/PythonCodes/PythonProgressivo/09-arquivos/letra.txt')
nomes = meuArquivo.readlines()

for nome in nomes:
    print(nome)

print('Número de linhas na letra: ',len(nomes))