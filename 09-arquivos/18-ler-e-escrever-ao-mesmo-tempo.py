import os.path

op=1
while op:
    if os.path.isfile("teste.txt") is False:
        print("Arquivo teste.txt nao existe. Criando...")
        meuArquivo = open("teste.txt", "w")
    
    meuArquivo = open("teste.txt", "r+")

    op=int(input("0. Sair \n"
                 "1. Ler\n"
                 "2. Escrever\n"))

    if op==1:
        print( meuArquivo.read() )
        meuArquivo.close()
        
    if op==2:
        num = input("Numero:")
        meuArquivo.truncate()
        meuArquivo.write(num)
        meuArquivo.close()

meuArquivo.close()