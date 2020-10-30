# Exercicio 7

numeros = []

for _ in range(5):
    num = int(input(f'Digite o primeiro {_ + 1}º número: '))
    numeros.append(num)


print(f'O maior numero digitado foi {max(numeros)}')
