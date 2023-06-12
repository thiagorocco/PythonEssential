'''
    Tratamento de erros
    try ... except ... else... finally

    Try é onde o código normal é executado
    Except vai executar somente se der erro
    Else vai executar se não dar erro
    Finally vai executar independente se der erro ou não

    ** raise vai gerar um erro definido pelo programador

'''
x = 10
try:
    print(x)
except:
    print('Erro no programa')
else:
    print('Tudo certo')
finally:
    print('Fim do tratamento')