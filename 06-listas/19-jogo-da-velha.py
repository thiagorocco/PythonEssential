jogador1 = 'X'
jogador2 = 'O'
tabuleiro = [[0 for i in range(3)]for j in range(3)]
linha1 = []
linha2 = []
linha3 = []
col1 = []
col2 = []
col3 = []
controle = True

def imprimir():
    print('Co1\tCol2\tCol3')
    for i in range(3):
        for j in range(3):
            print('L',i,"%4d" % tabuleiro[i][j], end='')
        print()

def checagem():

    for i in range(3):
        for j in range(3):
            if i==0:
                linha1[j] = tabuleiro[i][j]
                col1[j] = tabuleiro[j][i]
            if i==1:    
                linha2[j] = tabuleiro[i][j]
                col2[j] = tabuleiro[j][i]
            if i==2:    
                linha3[j] = tabuleiro[i][j]
                col3[j] = tabuleiro[j][i]


    if linha1.count('X') == 3 or linha2.count('X') == 3 or linha3.count('X')==3:
        print('Jogador 1 é o vencedor')
        controle = False
    elif linha1.count('O') == 3 or linha2.count('O') == 3 or linha3.count('O')==3:
        print('Jogador 2 é o vencedor')
        controle = False

    if col1.count('X') == 3 or col2.count('X') == 3 or col3.count('X')==3:
        print('Jogador 1 é o vencedor')
        controle = False
    elif col1.count('O') == 3 or col2.count('O') == 3 or col3.count('O')==3:
        print('Jogador 2 é o vencedor')
        controle = False
    
    #Diagonais
    if linha1[0] == 'X' and linha2[1]=='X' and linha3[2]=='X':
        print('Jogador 1 é o vencedor')
        controle = False
    elif linha1[2] == 'X' and linha2[1]=='X' and linha3[0]=='X':
        print('Jogador 1 é o vencedor')
        controle = False
    
    if linha1[0] == 'O' and linha2[1]=='O' and linha3[2]=='O':
        print('Jogador 2 é o vencedor')
        controle = False
    elif linha1[2] == 'O' and linha2[1]=='O' and linha3[0]=='O':
        print('Jogador 2 é o vencedor')
        controle = False

imprimir()
    