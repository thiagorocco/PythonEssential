#1. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Informe uma letra apenas: ')

#Deixa a letra maíscula para facilitar a comparação
letra = letra.upper()

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print('Essa letra é uma vogal')
else:
    print('Essa letra é uma consoante')