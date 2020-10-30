# Exercicio 5

while True:
    a = int(input('Informe a quantidade do primeiro país: '))
    b = int(input('Informe a quantidade do seguindo país: '))
    progressao_a = float(input('Informe a progressão do primeiro país: '))
    progressao_b = float(input('Informe a progressão do segundo país: '))
    ano = 0

    while a <= b:
        a += a * progressao_a
        b += b * progressao_b
        ano += 1

    print(f'A ultrapassa ou iguala a B em {ano} anos')

    sair = int(input('Deseja fazer mais um calculo?\n'
                     '0 - sair\n'
                     '1 - continuar'))
    if sair == 0:
        break
