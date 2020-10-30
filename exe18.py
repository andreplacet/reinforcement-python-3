# Exercicio 18

lista = []
count = 0

quant = int(input("Digite a quantiade de número que deseja digitar: "))

while quant != count:
    numero = lista.append(float(input("Digite um número: ")))
    count += 1

print(f'Maior: {max(lista)}\nMenor: {min(lista)}')
print(f'Soma: {max(lista) + min(lista)}')
