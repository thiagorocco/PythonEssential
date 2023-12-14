#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def digitos(number):
    if number < 10:
       print('This number has only 1 digit')
    elif number < 100:   
       print('This number has 2 digits')
    elif number < 1000:   
       print('This number has 3 digits')
    elif number < 10000:   
       print('This number has 4 digits')
    elif number < 100000:   
       print('This number has 5 digits')
    elif number < 1000000:   
       print('This number has 6 digits')
    else:
       print('This number more than 6 digits')


number = int(input('Informe um número inteiro: '))
digitos(number)
