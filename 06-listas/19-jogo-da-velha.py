import os
import platform

jogador = ''
tabuleiro = [['-' for i in range(3)]for j in range(3)]
linha1 = ['-' for i in range(3)]
linha2 = ['-' for i in range(3)]
linha3 = ['-' for i in range(3)]
col1 = ['-' for i in range(3)]
col2 = ['-' for i in range(3)]
col3 = ['-' for i in range(3)]
coluna = ''
linha = ''

def limparTela():
    so = platform.system()
    limpar = 'cls' if so == 'Windows' else 'clear'
    os.system(limpar) or None

def imprimir():
    limparTela()
    print("\tC1\tC2\tC3")
    for i in range(3):
        for j in range(3):
            if j==0:
                print(f"L{i+1}\t{tabuleiro[i][j]}", end='')
            else:
                print(f"\t{tabuleiro[i][j]}", end='')    
        print()

def checarResultado():

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
        return False
    elif linha1.count('O') == 3 or linha2.count('O') == 3 or linha3.count('O')==3:
        print('Jogador 2 é o vencedor')
        return False
    if col1.count('X') == 3 or col2.count('X') == 3 or col3.count('X')==3:
        print('Jogador 1 é o vencedor')
        return False
    elif col1.count('O') == 3 or col2.count('O') == 3 or col3.count('O')==3:
        print('Jogador 2 é o vencedor')
        return False

    #Diagonais
    if linha1[0] == 'X' and linha2[1]=='X' and linha3[2]=='X':
        print('Jogador 1 é o vencedor')
        return False
    elif linha1[2] == 'X' and linha2[1]=='X' and linha3[0]=='X':
        print('Jogador 1 é o vencedor')
        return False
    if linha1[0] == 'O' and linha2[1]=='O' and linha3[2]=='O':
        print('Jogador 2 é o vencedor')
        return False
    elif linha1[2] == 'O' and linha2[1]=='O' and linha3[0]=='O':
        print('Jogador 2 é o vencedor')
        return False
    
    empate=True
    for l in range(3):
        for c in range(3):
            if tabuleiro[i][c] == '-':
                empate = False
                break
        if empate == False:
            break
    if empate:
        print('Terminou em empate')
        return False
    
    
    return True

def jogar():
    vez = 1
    controle = True
    while controle:    
        validar = True
        while validar:
            imprimir()
            if vez%2!=0:
                jogador = 'X'
            else:
                jogador = 'O'

            linha = input(f'Jogador "{jogador}", escolha uma linha entre 1 e 3: ')
            coluna = input(f'Jogador "{jogador}", escolha uma coluna entre 1 e 3: ')

            if linha.isnumeric() and coluna.isnumeric():
                linha = int(linha)
                coluna = int(coluna)
                if coluna > 3 or coluna < 1 or linha > 3 or linha < 1:
                    print('Posição inválida! Escolha os valores 1, 2 ou 3 para as linhas e colunas')
                    input('Pressione qualquer tecla para continuar...')
                elif tabuleiro[linha-1][coluna-1] != '-':
                    print('Posição já preenchida! Escolha outra')
                    input('Pressione qualquer tecla para continuar...')
                else:
                    tabuleiro[linha-1][coluna-1] = jogador
                    validar = False
                    vez += 1
            else:
                print('Somente números inteiros de 1 a 3 são válidos para as posições!!!')
                input('Pressione qualquer tecla para continuar...')
        imprimir()
        controle = checarResultado()
    print('*** Fim de jogo ***')
    input('Pressione qualquer tecla para continuar...')

jogar()    
