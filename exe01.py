# Exercicio 1

while True:
    num = int(input('Digite um número de 1 a 10: '))
    if num in (1, 2, 4, 5, 6, 7, 8, 9, 10):
        print(f'Voce digitou o número {num}')
        break
    else:
        print('Número invalido, tente novamente!')
