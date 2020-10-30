# Exercicio 16

ultimo = 1
penultimo = 1

for count in range(2,502):
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    count += 1
    print(termo)
