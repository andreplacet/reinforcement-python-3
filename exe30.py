# Exercicio 30

paes = int(input('Digite a quantidade de pães: '))
while paes > 50:
    produtos = int(input('Digite a quantidade de produtos[menos que 50]: '))

count = 1
preco_pao = float(input('Qual é o preço do pão? : '))

for j in range(paes):
    print(f'{count} = R${preco_pao * count:.2f}')
    count += 1
