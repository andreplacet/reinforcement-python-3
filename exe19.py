# Exercicio 19

lista = []
count = 0

quant = int(input("Digite a quantiade de número que deseja digitar: "))

while quant != count:
    numero = float(input("Digite um número: "))

    while numero > 1000 or numero < 0:
        numero = float(input("Digite um número: "))

    lista.append(numero)
    count += 1

print(f'Maior: {max(lista)}\nMenor: {min(lista)}')
print(f'Soma: {max(lista) + min(lista)}')
