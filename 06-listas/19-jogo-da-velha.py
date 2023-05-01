opcao = 3
jogador1 = ''
jogador2 = ''
matriz = [['-' for i in range(4)]for j in range(4)]

while opcao!= 1 and opcao != 2:
    opcao = int(input('Escolha a opção 1 para jogar com "X" e 2 para jogar com "O": '))

if opcao == 1:
    jogador1 = 'X'
    jogador2 = 'O'
elif opcao == 2:
    jogador1 = 'O'
    jogador2 = 'X'

controle = True

while controle:
    
    print('Jogador 1 informe em qual casa deseja marcar')