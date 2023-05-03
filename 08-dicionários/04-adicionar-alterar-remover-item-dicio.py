'''
       1. Adicionar(GET+VALOR OU SETDEFAULT)C
       2. Alterar(IN+valor)
       3. Excluir(POP): 
'''

notas={'João'   :  9,
       'Maria'  : 10,
       'José': 4}


#Podemos adicionar um novo elemento com chave e valor dessa forma:
notas['Peart'] = 10
#Porém um alerta: Cuidado, pois se já existir essa chave no dicionário o valor será substituído
#É bom trabalhar assim apenas se tiver certeza que a chave não existe, use o get(key, value) para isso


#1. Forma correta de adicionar ou então usar setdefault
nome = input("Digite o nome do aluno: ")
nota = float(input("Nota dele: "))

if notas.get(nome):
    print("Ja existe o aluno ",nome)
else:
    notas[nome] = nota
print(notas)

#2. Para alterar um valor usamos "in" em um IF que verifica se já existe a chave:
nome = input("Aluno a mudar a nota: ")
nota = float(input("Nova nota     : "))

if nome in notas.keys():
    notas[nome] = nota
else:
    print("Não existe esse aluno")
print(notas)

#3. Excluir Use nome_dicionario.pop(key)

print(notas)
notas.pop('José')
print('Notas após excluir José',notas)

