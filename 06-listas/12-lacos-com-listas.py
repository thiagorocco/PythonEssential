n = int(input("Informe o número de matérias: "))
notas = []
soma=0

for count in range(n):
    nota=float(input("Nota da matéria %2d: " % (count+1)))
    #incrementando elementos de um array com colchetes
    notas += [nota]
    soma += nota

print("Notas: ",notas)
print("Média: %.2f" % (soma/n))