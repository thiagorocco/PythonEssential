caminho = 'C:/PythonCodes/PythonProgressivo/09-arquivos/arquivo.csv'
meuArquivo = open(caminho,'a')

notas = {
        'Clark' : 9.7,
        'Diana' : 10,
        'Bruce' : 8.4,
        'John' : 8.3
}


meuArquivo.write('NOTAS;ALUNOS\n')

for nome in notas.keys():
    texto = f"{nome};{notas[nome]}\n"
    meuArquivo.write(texto)


meuArquivo.close()
