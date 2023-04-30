bandas = []

while True:
    op = int(input('1. Adicionar banda\n'
                    '2. Exibir bandas favoritas\n'
                    '3. Tamanho da lista de bandas\n'))
    if(op==1):
        banda=input('Digite o nome da banda: ')
        bandas.append(banda)
    elif(op==2):
        print(bandas)
    elif(op==3):
        print(len(bandas))