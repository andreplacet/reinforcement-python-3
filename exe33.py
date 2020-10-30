# Exercicio 23

n_temperaturas = int(input(f'Quantidade de temperaturas que irá digitar: '))
temperaturas = []
n_temperatura = 1

for i in range(n_temperaturas):
    print(f'Temperatura n° {n_temperatura}')
    temperatura = temperaturas.append(float(input('Digite a temperatura: ')))
    n_temperatura += 1

print(f'Maior temperatura = {max(temperaturas)}')
print(f'Menor temperatura = {min(temperaturas)}')
print(f'Média = {sum(temperaturas) / len(temperaturas):.1f}')
