bandas = []

while True:
    op = int(input('1. Adicionar banda\n'
                    '2. Exibir bandas favoritas\n'
                    '3. Tamanho da lista de bandas\n'
                    '4. Alterar banda\n'))

    if(op==1):
        banda=input('Digite o nome da banda: ')
        bandas.append(banda)
    elif(op==2):
        print(bandas)
    elif(op==3):
        print(len(bandas))
    elif(op==4):
        #Alterando valor da lista
        index = int(input('Indice que vai alterar: '))
        if(index<len(bandas)):
            print('O índice ',index,' corresponde atualmente à banda: ',bandas[index])

            option = input('Deseja continuar com a alteração?(S/N): ')

            if option=='s' or option=='S':
                temp = input('Informe o novo nome da banda: ')
                bandas[index] = temp
                print('Banda alterada com sucesso')
        else:
            print('Esse índice não existe')
   