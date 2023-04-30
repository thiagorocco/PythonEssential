alunos = 0

while alunos < 1:
    alunos=int(input("Numeros de alunos na turma: "))
    if alunos < 1:
        print('Deve haver ao menos 01 aluno na turma!!! Informe outro número')

count=1
soma = 0.0

while count <= alunos:
    #print("Nota do aluno ", count, ":")
    nota = float(input('Nota do aluno %.0f:' %count))
    soma += nota
    count += 1

print("Media da turma: ", (soma/alunos) )