opcao = 3
jogador1 = 'X'
jogador2 = 'O'
tabuleiro = [[0 for i in range(3)]for j in range(3)]
linha1 = []
linha2 = []
linha3 = []
col1 = []
col2 = []
col3 = []

def imprimir():
    for i in range(3):
        for j in range(3):
            print("%4d" % tabuleiro[i][j], end='')
        print()

def checagem():

    for i in range(3):
        for j in range(3):
            if i==0:
                linha1[j] = tabuleiro[i][j]
            if i==1:    
                linha2[j] = tabuleiro[i][j]
            if i==2:    
                linha3[j] = tabuleiro[i][j]
        

    if linha1.count('X') == 3:
        print('Jogador 1 é o vencedor')
    elif linha1.count('O') == 3:
        print('Jogador 2 é o vencedor')