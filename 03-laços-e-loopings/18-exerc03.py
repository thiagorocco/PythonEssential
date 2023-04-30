'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres).
'''
nome = input("Qual seu nome [minimo 4 caracteres]: ")
idade = int(input("Sua idade: "))
salario = float(input("Salário: "))
sexo = input("Sexo ('f' para feminino ou 'm' para masculino): ")
civil = input("Estado civil (s, c, v ou d): ")

while len(nome) <= 3:
    nome = input("Seu nome deve ter mais que 3 caracteres: ")

while (idade < 0) or (idade > 150):
    idade = int(input("Voce deve ter entre 0 e 150 anos: "))

while (salario<0):
    salario = float(input("A coisa ta difícil, mas não tem salário negativo: "))

while (sexo!= 'f') and (sexo!='m'):
    sexo = input("Biologicamente, você deve ser 'f' ou 'm': ")

while (civil!='s')and(civil!='c')and(civil!='v')and(civil!='d'):
    print("Nao tem estado civil 'confuso'")
    civil = input("Deve ser s, c, v ou d: ")
