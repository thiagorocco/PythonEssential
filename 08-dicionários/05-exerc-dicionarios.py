from nis import match


print('*** PROGRAMA CONTROLE DE NOTAS E ALUNOS ***')
print('** Informe uma das opções abaixo: **')
print()
print('0. Sair')
print('1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)')
print('2. Inserir aluno e nota')
print('3. Alterar a nota de um aluno')
print('4. Consultar nota de um aluno específico')
print('5. Apagar um aluno da lista')
print('6. Dar a média da turma')

dia = 'Sábado'

match dia:
    case 'Sábado' | 'Domingo':
        print('Fim de semana')
    case _:
        print('Dia útil')
