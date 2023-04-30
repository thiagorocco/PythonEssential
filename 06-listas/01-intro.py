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
print(eu)