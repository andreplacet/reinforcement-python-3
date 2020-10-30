# Exercicio 25

lista = []

pessoas = int(input('Quantas pessoas para calcular a média de idade? '))

for _ in range(pessoas):
    pessoa = int(input(f'Idade da {_ + 1}º pessoa: '))
    lista.append(pessoa)

media = sum(lista) / len(lista)

print(f'{media:.0f}')
if media >= 60:
    print('média de idades maior ou igual a 60, grupo de pessoas idosas')
elif 20 <= media <= 26:
    print('média de idade entre 20 e 26 anos inclusive, grupo de pessoas adultas')
else:
    print('média inferior a vinte anos, grupo de jovens')
