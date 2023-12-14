def cadastro():
    name = input('Qual o seu nome?: ')
    age = input('Qual a sua idade?: ')

    return name, age

print('Iniciando o cadastro...')
nome, idade = cadastro()
print('Cadastro realizado com sucesso')
print('Seu nome é: ',nome,'e você tem ',idade,'anos de idade')