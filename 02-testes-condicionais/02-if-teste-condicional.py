idade = int(input('Informe a sua idade: '))

# É necessário haver a indentação, que nada mais é que dar o espaçamento dentro do if.

if idade >= 18:
    print('Perfeito, você é maior de idade')
    
    sexo = (input('Sexo: M/F: '))

    if(sexo == 'M' or sexo =='m'):
        print('Sexo Masculino')
    else:
        if(sexo == 'F' or sexo=='f'):
            print('Sexo Feminino')
        else:
            print('Sexo indefinido')        
else:
    print('Sinto muito, mas você é menor de idade e preciso de um responsável')