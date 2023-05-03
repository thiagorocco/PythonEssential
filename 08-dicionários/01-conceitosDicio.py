'''
    São sequência de dados do tipo desordenados, pois não são numerados por índice.
    Ao invés de índice, temos chaves.

    Se nas listas usamos colchetes [ ], nas tuplas usamos parêntesis ( )
    nos dicionários iremos usar chaves { },

    São mutáveis assim como as listas

    São usados para mapeamento, pois mapeiam sua chave com seu valor.
'''
#Observe que não existe uma sequência lógica ou óbvia das chaves que seriam os índices
meuCachorro = {'raca':'bulldog','idade':3,'nome':'Totó'}

#Outro exemplo:
loginSenha = {
    'joao'      :   'rush',
    'maria'     :   'yes',
    'afonso'    :   'apocalipse' 
}

login = input('Qual o seu login: ')
senha = input('Senha: ')

if loginSenha[login] == senha:
    print('Acesso autorizado')
else:
    print('Senha incorreta!!!')