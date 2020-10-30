# Exercicio 3

nome = ''
idade = 0
salario = 0
sexo = 'sexo'
estado_civil = ''

while len(nome) <= 3:
    print('(seu nome deve conter pelo menos tres caracteres)')
    nome = str(input('Digite seu nome: '))
while idade <= 0 and idade < 150:
    print('(sua idade deve estar no intervalo entre 1 e 150 anos)')
    idade = int(input('Digite sua idade: '))
while salario <= 0:
    print('(informe um valor mais que R$ 0.00)')
    salario = float(input('Digite seu salario: '))
while sexo[0] not in ('m', 'f'):
    print('(use M para masculino e F para feminino)')
    sexo = str(input('Informe seu sexo [M]asculino / [F]eminino: ')).lower()
while estado_civil not in ('s', 'c', 'v'):
    print('(use S para solteiro C para casado e V para viúvo)')
    estado_civil = str(input('Informe seu estadio civil [S]olteiro / [C]asado / [V]iuvo: ')).lower()

print(f'Nome: {nome.capitalize()}\n'
      f'Idade: {idade}\n'
      f'Salario: {salario:.2f}\n'
      f'Sexo: {sexo[0].upper()}\n'
      f'Estado civil: {estado_civil.upper()}')
