# Exercicio 12

num = 0

while num <= 0 and num <= 10:
    print('Tabuada')
    num = int(input('Digite um número: '))
    for _ in range(11):
        print(f'{num} X {_} = {num * _}')