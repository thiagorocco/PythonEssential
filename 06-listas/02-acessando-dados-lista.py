nome = input("Qual seu nome: ")
idade = int(input("Qual sua idade: "))
altura = float(input("Qual sua altura: "))
peso = float(input("Qual seu peso: "))

op= int(input("Estado civil:\n1.Casado\n2.Solteiro\n"))

if op==1:
    op = True
else:
    op = False

eu = [nome,idade,altura,peso,op]

#Nunca mais conte 1,2,3,... e sim 0,1,2,...
print('Nome: ',eu[0])
print('Idade: ',eu[1])
print('Altura: ',eu[2])
print('Peso: ',eu[3])
print('Casado: ',eu[4])