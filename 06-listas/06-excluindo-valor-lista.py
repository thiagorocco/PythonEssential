import os

bandas = []

while True:
    os.system('cls') or None
    op = int(input('1. Adicionar banda\n'
                    '2. Exibir bandas favoritas\n'
                    '3. Tamanho da lista de bandas\n'
                    '4. Alterar banda\n'
                    '5. Excluir banda\n'))

    if(op==1):
        os.system('cls') or None
        banda=input('Digite o nome da banda: ')
        bandas.append(banda)
        print('Banda cadastrada com sucesso!')
        input('Pressione qualquer tecla para continuar')
    elif(op==2):
        os.system('cls') or None
        print(bandas)
        input('Pressione qualquer tecla para continuar')
    elif(op==3):
        os.system('cls') or None
        print(len(bandas))
        input('Pressione qualquer tecla para continuar')
    elif(op==4):
        os.system('cls') or None
        index = int(input('Indice que vai alterar: '))
        if(index<len(bandas)):
            print('O índice ',index,' corresponde atualmente à banda: ',bandas[index])
            option = input('Deseja continuar com a alteração?(S/N): ')
            if option=='s' or option=='S':
                temp = input('Informe o novo nome da banda: ')
                bandas[index] = temp
                print('Banda alterada com sucesso')
                input('Pressione qualquer tecla para continuar')
        else:
            print('Esse índice não existe')
            input('Pressione qualquer tecla para continuar')
     #Exclusão de valor da lista
    elif(op==5):
        os.system('cls') or None
        if len(bandas)<1:
            print('Não há bandas cadastradas para você excluir')
            input('Pressione qualquer tecla para continuar')
        else:
            index= int(input('Índice que vai excluir: '))
            if(index<len(bandas)):
                print('O índice ',index,' corresponde atualmente à banda: ',bandas[index])
                option = input('Deseja continuar com a exclusão?(S/N): ')
                if option=='s' or option=='S':
                    del bandas[index]
                    print('Banda excluída com sucesso')
                    input('Pressione qualquer tecla para continuar')
            else:
                print('Índice não existe')
                input('Pressione qualquer tecla para continuar')