# Exercicio 15

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b


n = int(input("Digite o termo que queira descobrir na sequência Fibonacci: "))
fib(n)
