# Exercicio 43

codigos = [100, 101, 102, 103, 104, 105]
comidas = ['Cachorro Quente', 'Bauru Simples', 'Bauru com ovo', 'Hamburguer', 'ChesseBurguer', 'Refrigerante']
precos = [1.20, 1.30, 1.50, 1.20, 1.30, 1.0]
codigo = True
n_pedido = 0
pedido = []

while codigo != 0:
    print(f'Pedido n°{n_pedido + 1}')
    codigo = int(input("Digite o código do alimento: "))
    if codigo == 0:
        break
    else:
        while codigo not in codigos:
            print('[Este código não corresponde a nenhum alimento.]')
            codigo = int(input('Digite o código do alimento: '))

        indice = codigos.index(codigo)
        quantidade = int(input('Digite a quantidade: '))
        valor_pedido = precos[indice] * quantidade
        pedido.append(valor_pedido)
    n_pedido += 1

pedido_nota = 0

for i in range(n_pedido - 1):
    print(f'Pedido n°{pedido_nota + 1} = R$ {pedido[pedido_nota]:.2f}')
    pedido_nota += 1
print(f'Total: R${sum(pedido):.2f}')
