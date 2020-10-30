# Exercicio 2

while True:
    user = str(input('Digite o nome de usuario: '))
    password = str(input('Digite a senha de usuario: '))
    if user == password:
        print('A senha de usuario não pode ser igual ao nome de usuario')
    else:
        print('Dados salvos com sucesso!')
        break
