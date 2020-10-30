# Exercicio 28

quant_cds = int(input('Digite a quantidade de CDs: '))
cds = []
n_cd = 1

for i in range(quant_cds):
    print(f'CD número  {n_cd}')
    valor_cd = cds.append(float(input('Digite o valor do CD: ')))
    n_cd += 1

media = sum(cds) / len(cds)
print(f'A media para cada CD é: {media:.2f}')
