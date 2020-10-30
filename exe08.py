# Exercicio 8

numeros = []

for _ in range(5):
    num = int(input(f'Digite o primeiro {_ + 1}º número: '))
    numeros.append(num)


print(f'A soma dos números digitados é: {sum(numeros)}\n'
      f'A media {sum(numeros) / len(numeros)}')
