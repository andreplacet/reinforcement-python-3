# Exercicio 31

from time import sleep
from os import system

while True:
    precos_produtos = []
    preco_produto = True
    n_produto = 1

    while preco_produto != 0:
        print(f'Poduto n° {n_produto}')
        preco_produto = float(input('Digite o preço do produto: '))
        precos_produtos.append(preco_produto)
        n_produto += 1

    print(f'Total: {sum(precos_produtos)}')
    dinheiro = float(input('Digite a quantida que irá pagar: '))

    while dinheiro < sum(precos_produtos):
        dinheiro = float(input('Digite a quantida que irá pagar[maior que o total da compra] : '))

    print(f'Dinheiro: R${dinheiro}')
    print(f'Troco: R${dinheiro - sum(precos_produtos)}')
    print(f'\nPróxima compra em 3 segundos...')
    sleep(3)
    system('cls')

