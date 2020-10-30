# Exercicio 21

n = int(input("Verificar numeros primos ate: "))

mult = 0

for count in range(2, n):
    if n % count == 0:
        print("Múltiplo de",count)
        mult += 1

if mult == 0:
    print(f'O número {n} é um numeor primo')
else:
    print('O número {n} não é um numero primo')
