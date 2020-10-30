# Exercicio 13

base = int(input("Base: "))
expoente = int(input("Expoente: "))

potencia = 1

for count in range(expoente):
    potencia *= base
    count += 1

print(f'{base} ^ {expoente} = {potencia}')
