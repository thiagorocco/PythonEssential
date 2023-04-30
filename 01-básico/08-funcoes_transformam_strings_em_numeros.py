#Funções int() e float()
#Função input() transforma automaticamente tudo que o usuário digita em string

string=input("Digite uma string: ")
print( type(string) )

inteiro=input("Digite um inteiro: ")
print( type(inteiro) )

decimal=input("Digite um float: ")
print( type(decimal) )

var1 = int(inteiro)
print(type(var1))

var2 = float(decimal)
print(type(var2))

#usando int() e float() na função input()
var3 = int(input('Digite um inteiro: '))
var4 = float(input('Digite um decimal: '))

print('var3 = ',var3,' e ',type(var3))
print('var4 = ',var4,' e ',type(var4))