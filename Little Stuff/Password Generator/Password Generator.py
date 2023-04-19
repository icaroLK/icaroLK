#  A senha deve ter mínimo 8 e máximo 15 caracteres.
#  A senha deve ter pelo menos uma letra maiúscula.
#  A senha deve ter pelo menos uma letra minúscula.
#  A senha deve ter pelo menos um símbolo. Ex: * ! # $ % & + - / : ; = ? @ \ |
#  A senha deve ter pelo menos um número.
from random import randint, choice


def prettylist(a):
    for c in range(len(a)):
        # para não deixar colado é so colocar um espaço dentro do end=''
        print(a[c], end='')


def titulo(msg):
    print('\033[1;37m=\033[m'*50)
    print('\033[37m{:^50}\033[m'.format(msg))
    print('\033[1;37m=\033[m'*50)


titulo('PASSWORD GENERATOR')
numeros = '0123456789'
alphaP = 'abcdefghijklmnopqrstuvwxyz'
alphaG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
especial = '*!#$%&+-/:;=?@|'
opcoes = [numeros, alphaP, alphaG, especial]
prontas = []
qtd = int(input('Quantidade de caracteres [8-15]: '))
vezes = int(input('Quantidade de senhas: '))

for c in range(vezes):
    verific = [0, 0, 0, 0]
    cu = 0
    senha = []

    while True:
        altern = randint(0, 3)
        senha.append(choice(opcoes[altern]))
        verific[altern] += 1

        if len(senha) == qtd:
            if all(count >= 1 for count in verific):
                prontas.append(senha)
                break
            else:
                senha = []
                verific = [0, 0, 0, 0]


print('\033[1m—\033[m'*(16+qtd))

for i, v in enumerate(prontas):
    print(f'   {i+1}° senha: ', end='')
    print('\033[1;34m', end='')
    prettylist(v)
    print('\033[m', end='')
    print()

print('\033[1m—\033[m'*(16+qtd))
