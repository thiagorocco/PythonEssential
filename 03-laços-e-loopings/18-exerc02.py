'''
Faça um programa que leia um nome de usuário e a sua senha e
não aceite a senha igual ao nome do usuário, mostrando uma 
mensagem de erro e voltando a pedir as informações.
'''

controle  = True
usuario = input('Informe o nome do usuário: ')

while controle == True:
    
    senha = input('Informe uma senha: ')

    if usuario == senha:
        print('Senha não pode ser igual ao nome do usuário. Por favor digite outra senha.')
    else:
        controle = False
print('Operação concluída com sucesso')
    