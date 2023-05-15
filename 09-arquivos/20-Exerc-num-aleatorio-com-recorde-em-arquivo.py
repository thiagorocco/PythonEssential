import random
import os

caminho = 'C:\\PythonCodes\\PythonProgressivo\\09-arquivos\\recorde.txt'
tentativas = 0
controle = True
sorteado = random.randint(1,100)

while controle:
    tentativas += 1
    num = int(input('Adivinhe o número entre 1 e 100: '))
    if(sorteado==num):
        controle = False
        print('Você acertou em ', tentativas,'tentativas.')
    elif sorteado < num:
        print('Número sorteado é menor')
    else:
        print('Número sorteado é maior')

if os.path.isfile(caminho) is False:
    print('Primeiro recorde gravado')
    arquivo = open(caminho,'w')
    arquivo.write(str(tentativas))
    arquivo.close()
else:
    arquivo = open(caminho,'r+')
    recorde = arquivo.read()
    if tentativas < (int(recorde)):
        print('Temos um NOVO RECORDE!!!')
        print('Recorde anterior: ',recorde,'tentativas.')
        arquivo.truncate()
        arquivo.seek(0)
        arquivo.write(str(tentativas))
        arquivo.close()
    else:
        print('Recorde atual: ',recorde,'tentativas.')
        