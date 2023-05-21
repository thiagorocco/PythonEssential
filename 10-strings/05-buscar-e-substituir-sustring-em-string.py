'''
    endwith() - Procura o conteúdo no fim da string 
    startswith() - Procura o conteúdo no início da string
    find() - Procura o conteúdo em qualquer lugar da string
    replace() - susbtitui uma substring por outra
'''

#endwith()
texto = input("Digite o nome de um arquivo com sua extensão:" )
if texto.endswith('.txt'):
    print("É um arquivo de texto")
elif texto.endswith('.pdf'):
    print("É um arquvido do Acrobat Reader")
elif texto.endswith('.png'):
    print("É uma imagem")
else:
    print("Outro tipo de arquivo")


lista = ['Aldo','Ernesto','Francisco Luiz','Francisco José','Eduardo','José Francisco','João Francisco']
busca = 'Francisco'

#startswith()
print(f'*** Usando startswith com a busca {busca}***')
for nomes in lista:
    if nomes.startswith(busca):
        print(nomes)

#find()
print('*** Usando find ***')
for nomes in lista:
    if nomes.find(busca):
        print(nomes)