# Exercicio 42

n25 = []
n50 = []
n75 = []
n100 = []

numero = True

while numero > 0:
    numero = float(input("Digite um número: "))
    if 0 < numero <= 25:
        n25.append(numero)
    elif 25 < numero <= 50:
        n50.append(numero)
    elif 50 < numero <= 75:
        n75.append(numero)
    elif 75 < numero <= 100:
        n100.append(numero)

print(f'[0, 25]: {len(n25)}')
print(f'[26, 50]: {len(n50)}')
print(f'[51, 75]: {len(n75)}')
print(f'[76, 100]: {len(n100)}')
