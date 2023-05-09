'''
    MODOS DE ABERTURA DE ARQUIVOS EM

"a"  - Escreve ao final do arquivo; se este não existir, é criado
"r"  - Abre o arquivo para a leitura, se não existir, lançar um eerro de IOError
"r+" - Abra um arquivo para leitura e escrita. Se não existe, lança um erro IOError
"w"  - Abre um arquivo para escrita. Se existe, ele 'trunca' tudo e escreve por cima. Se não existir o arquivo, ele cria
"w+" - Abre para leitura e escrita. Se existe, apaga todo conteúdo e escreve por cima. Se não existir o arquivo, ele cria
"ab", "rb", "r+b", "wb", "w+b" - Abre arquivos para trabalhar com entrada e saída no modo binário, para plataformas Windows e Macintosh

-> open('caminho') é o mesmo que open('caminho','r') - r siginifica read, ou seja, modo leitura.Não pode
alterar nada.

-> open('caminho','w') significa que vamos abrir o arquivo e escrever nele(Sobrescrever).
** Detalhe: Se você abrir e escrever em um arquivo que não existe, ele cria esse arquivo.

->open('caminho','a') Append: Adiciona novo conteúdo sem sobrescrever o antigo.

'''
caminho = 'C:/PythonCodes/PythonProgressivo/09-arquivos/file.txt'
meuArquivo = open(caminho,'a')
meuArquivo.write('\nCurso de Python Progressivo 6')
meuArquivo.close()
