import os

op = 1
while op:
    os.system('cls') or None
    if os.path.isfile('teste.txt') is False:
        print('Arquivo teste não existe. Criando ...')
        meuArquivo = open('teste.txt','w')
    
    meuArquivo = open('teste.txt','r+')

    op = int(input(
                    '0. Sair\n'
                    '1. Ler\n'
                    '2. Escrever\n'
        ))
    
    if op==1:
        print(meuArquivo.read())
        meuArquivo.close()
        input('Pressione qualquer tecla para continuar')
    if op==2:
        num = input('Número:')
        num2 = meuArquivo.read()
        meuArquivo.seek(0)

        if(num2 is '') or (int(num)>int(num2)):
            meuArquivo.truncate()
            meuArquivo.write(num)
            meuArquivo.close()
        else:
            print('Número não gravado!',num,'menor ou igual a',num2)
            input('Pressione qualquer tecla para continuar')
meuArquivo.close()