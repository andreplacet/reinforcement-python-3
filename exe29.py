# Exercicio 29

produtos = int(input('gite a quantidade de produtos: '))
while produtos > 50:
    produtos = int(input('Digite a quantidade de produtos[menos que 50]: '))


precos = []
n_produto = 0
count = 0

for i in range(produtos):
    print(f'Produto n°{n_produto + 1}')
    preco = precos.append(float(input('Digite o preço do produto: ')))
    n_produto += 1

n_produto = 0

for j in range(produtos):
    print(f'Produto N°{n_produto + 1} = {precos[count]}')
    count += 1
    n_produto += 1
