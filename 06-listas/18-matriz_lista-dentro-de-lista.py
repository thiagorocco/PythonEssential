#Preenchendo elementos de uma lista e de uma matriz com um único elemento através do for in
lista = [0 for i in range(4)]
matriz = [[1 for i in range(4)]for j in range(4)]
print(lista)
print(matriz)

#Preenchendo elementos de uma matriz
count = 1
for linha in range(4):
    for coluna in range(4):
        matriz[linha][coluna] = count
        count += 1

#Exibir listas de uma matriz por linha
for linha in range(4):
    print('')
    for coluna in range(4):
        print("%4d" % matriz[linha][coluna], end='')
print()
