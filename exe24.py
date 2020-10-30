# Exercicio 24

repeticoes = int(input('Quantas notas deseja adicionar? '))
lista = []

for _ in range(repeticoes):
    nota = float(input(f'Nota {_ + 1}º '))
    lista.append(nota)

media = sum(lista) / len(lista)

print(f'A média das notas informadas é de: {media:.2f}')
