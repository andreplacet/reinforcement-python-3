# Exercicio 32

from math import factorial

numero = int(input('Digite o numero que quer realizar a fatorial : '))
count = numero
fatorial = factorial(numero)

for _ in range(numero - 1):
    print(f'{count}', end=' * ')
    count -= 1
print(f'1 = {fatorial}')
