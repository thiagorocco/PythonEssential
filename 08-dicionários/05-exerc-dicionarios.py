''''
Uma escola te contratou para fazer um software em Python.
Eles querem que você crie um script que exiba o seguinte menu:

0. Sair
1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)
2. Inserir aluno e nota
3. Alterar a nota de um aluno
4. Consultar nota de um aluno específico
5. Apagar um aluno da lista
6. Dar a média da turma

Onde a professora que vai fornecer o nome e nota dos alunos. 
Quantos ela quiser. Quantas vezes quiser.
Implemente esse script usando um dicionário.
'''
import os
import platform

syop = platform.system()
op = ''
nome = ''
nota = 0.0
soma = 0
media = 0

notas = {
        'Andreia'   : 7.5,
        'Breno'     : 8.4,
        'Carla'     : 9.7,
        'Danilo'    : 8.3,
        'Eduardo'   : 7.2
        }

def limparTela():
    if syop == 'Windows':
        os.system('cls')
    elif syop == 'Linux':
        os.system('clear')

def listarAlunos(listaCompleta=True):
    limparTela()
    if listaCompleta:
        print('LISTA DE ALUNOS E NOTAS:\n')
        print('ALUNOS\t\t\tNOTAS')
        for nome in notas.keys():
            print(f"{nome}\t\t\t{notas[nome]}")
        input('Pressione alguma tecla para continuar ...')
    else:
        print('LISTA DE ALUNOS:')
        print('ALUNOS')
        for nome in notas.keys():
            print(f"{nome}")
        input('Pressione alguma tecla para continuar ...')

def cadastrarAluno():
    limparTela()
    nome = input('Informe o nome do novo aluno: ')
    nota = float(input('Informe a nota do novo aluno: '))

    if notas.get(nome):
        print('Já existe um aluno cadastrado com esse nome')
        print('Veja a lista abaixo e tente novamente com outro nome:')
        listarAlunos()
    else:
        notas[nome] = nota
        print('Cadastro efetuado com sucesso')
        input('Pressione alguma tecla para continuar ...')

def alterarNota():
    limparTela()
    listarAlunos()
    nome = input('Informe o nome do aluno que deseja alterar a nota: ')
    if nome in notas.keys():
        nota = float(input('Informe a nova nota: '))
        notas[nome] = nota
        print('Nota alterada com sucesso!')
        input('Pressione alguma tecla para continuar ...')
    else:
        print('Não existe aluno cadastrado com esse nome!')
        input('Pressione alguma tecla para continuar ...')

def notaIndividual():
    limparTela()
    listarAlunos(False)
    nome = input('Qual dos alunos deseja consultar a nota?: ')

    if nome in notas.keys():
        print('Nome: ',nome,' - Nota: ',notas[nome])
        input('Pressione alguma tecla para continuar ...')
    else:
        print('Não existe aluno com esse nome.')
        input('Pressione alguma tecla para continuar ...')

def removerAluno():
    limparTela()
    listarAlunos(False)
    nome = input('Qual dos alunos deseja EXCLUIR?: ')
    if nome in notas.keys():
        op = input(f'Tem certeza que deseja excluir o aluno {nome}? Digite novamente o nome dele: ')
        if op == nome:
            notas.pop(nome)
            print('Aluno',nome,'excluído com sucesso')
            input('Pressione alguma tecla para continuar ...')
        else:
            print('Exclusão cancelada.')
            input('Pressione alguma tecla para continuar ...')
    else:
        print('Não há alunos a excluir com esse nome')
        input('Pressione alguma tecla para continuar ...')

def mediaNotas():
    limparTela()
    soma = 0
    media = 0
    for nome in notas.keys():
        soma += notas[nome]

    media = soma/len(notas)

    print("A média de notas da turma = %.2f" % media)    
    input('Pressione alguma tecla para continuar ...')  

def menu():
    global op
    while op != '0':
        limparTela()
        print('*** PROGRAMA CONTROLE DE NOTAS E ALUNOS ***')
        print('** Informe uma das opções abaixo: **')
        print()
        print('0. Sair')
        print('1. Exibir lista de alunos com suas notas')
        print('2. Inserir aluno e nota')
        print('3. Alterar a nota de um aluno')
        print('4. Consultar nota de um aluno específico')
        print('5. Apagar um aluno da lista')
        print('6. Dar a média da turma')
        print()
        op = input('===>> Digite a opção desejada: ')

        if op == '0':
            print('Encerrando o programa')   
        elif op == '1':
            listarAlunos()
        elif op == '2':
            cadastrarAluno()
        elif op == '3':
            alterarNota()
        elif op == '4':
            notaIndividual()
        elif op == '5':
            removerAluno()
        elif op == '6':
            mediaNotas()
        else:
            print('Opção incorreta. Tente novamente.')
menu()
