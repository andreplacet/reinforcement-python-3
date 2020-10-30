# Exercicio 20
import math

import math

num = int(input("Digite um numero menor que 16: "))

while num > 16:
    print("Numero invalido")
    num = int(input("Digite um numero menor que 16: "))

print(f"o fatorial de {num} é {math.factorial(num)}")

resposta = input("Deseja calcular novamente? s/n: ").lower()

while resposta == "s":
    num = int(input("Digite um numero menor que 16: "))
    while num > 16:
        print("Numero invalido")
        num = int(input("Digite um numero menor que 16: "))
    print(f"o fatorial de {num} é {math.factorial(num)}")
    resposta = input("Deseja calcular novamente? s/n: ").lower()