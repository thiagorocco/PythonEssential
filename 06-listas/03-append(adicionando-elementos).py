bandas = []

while True:
    op = int(input('1. Adicionar banda\n'
                    '2. Exibir bandas favoritas\n'))
    if(op==1):
        banda=input('Digite o nome da banda: ')
        bandas.append(banda)
    elif(op==2):
        print(bandas)