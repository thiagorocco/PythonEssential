'''
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até 
que o usuário informe um valor válido.
'''
controle = False

while controle == False:
    numero = float(input('Informe um número entre 0 e 10: '))
    if numero <=10 and numero >=0:
        controle = True
        print('Número informado: ',numero)
    else:
        print('Número informado:', numero,'.Informe um número entre 0 e 10')
