#readlines() -> Lê as linhas e coloca o conteúdo de cada linha em uma posição de um array
#realine() -> lê apenas uma linha até '\n'. Se executado de novo lê a próxima linha

meuArquivo = open('C:/PythonCodes/PythonProgressivo/09-arquivos/funcionarios.txt')
nomes = meuArquivo.readlines()
print('Linhas: ',nomes)

#realines Resultado
#['Geddy Lee\n', 'Neil Peart\n', 'Alex Lifeson\n']
#Para a readlines() cada linha é uma string que termina no caractere '\n'.

#readline resultado
#
meuArquivo = open('C:/PythonCodes/PythonProgressivo/09-arquivos/funcionarios.txt')
linha = meuArquivo.readline()
print('Linha: ',linha)