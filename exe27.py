# Exercicio 27

turmas = int(input('Quantas turmas?: '))
alunos_turmas = []
turma = 1

for i in range(turmas):
    print(f'turma {turma}')
    alunos = int(input('Alunos da turma : '))
    while alunos > 40:
        print(f'turma {turma} (uma turma só pode ter 40 alunos)')
        alunos = int(input('Alunos da turma : '))
    turma += 1
    alunos_turmas.append(alunos)

media = sum(alunos_turmas) / len(alunos_turmas)
print(f'A media e igual a: {media:.1f}')
