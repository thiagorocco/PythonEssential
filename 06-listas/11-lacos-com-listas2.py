numeros = []

for count in range(1,11):
    numeros += [count]

for count in range(len(numeros)):
    print('Números %2d:  %2d' %(count+1,numeros[count]))