# Exercicio 22

num = int(input("Digite um numero: "))
lista = []
if (num % 2 != 0) and  num == 2:
    print("O numero é primo")
else:
    for i in range(num):
        if num % (i + 1 == 0):
            lista.append(i + 1)
print(f"Os numeros que são divisiveis por {num} são {lista}", end=" ")
