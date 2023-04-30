'''
A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo.
'''
n = int(input('Informe o número de termos da série Fibonacci'))
anterior = 1
atual = 1
proximo = 0
aux = 0

for count in range(1,n+1):
    if count <= 2:
        print(atual)
    else:
        proximo = atual + anterior
        print(proximo)
        anterior = atual
        atual = proximo