from composicaoClasses import Cliente

cliente1 = Cliente('Luiz',32)
cliente1.insere_endereco('Belo Horizonte','MG')
print(cliente1.nome)
cliente1.lista_enderecos()
#Ao executar o del aqui, o método __del__ lá da classe não será executado
del cliente1
print()

cliente2 = Cliente('Maira',55)
cliente2.insere_endereco('Salvador','BA')
print(cliente2.nome)
cliente2.insere_endereco('Rio de Janeiro','RJ')
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João',19)
cliente3.insere_endereco('São Paulo','SP')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
