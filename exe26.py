# Exercicio 26

resultado = []

qtd_eleitores = int(input('Quanto eleitores vão votar? '))

for _ in range(qtd_eleitores):
    voto = int(input(f'Para votar no cadidato 1 use a legenda 12\n'
                     f'Para votar no candidato 2 use a legenda 22\n'
                     f'Para votar no candidato 3 use a legenda 33\n'
                     f'--> '))
    resultado.append(voto)

resultado_1 = resultado.count(12)
resultado_2 = resultado.count(22)
resultado_3 = resultado.count(32)

if resultado_1 > resultado_2 and resultado_1 > resultado_3:
    print('O vencedor foi o candidato 1')
elif resultado_2 > resultado_1 and resultado_2 > resultado_3:
    print('O vencedor foi o candidato 2')
else:
    print('O vencedor foi o candidato 3')
