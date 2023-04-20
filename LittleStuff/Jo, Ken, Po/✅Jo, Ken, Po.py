from random import randint
from time import sleep
qtde = 0

while True:
    print("="*6, "\033[97mPEDRA, PAPEL OU TESOURA\033[m", "="*6)
    itens = ('\033[31mpedra\033[m', '\033[1;97mpapel\033[m', '\033[34mtesoura\033[m')
    comp = randint(0, 2)

    x = int(input('''\nEscolha uma opção:
[0] = \033[31mpedra\033[m
[1] = \033[1;97mpapel\033[m
[2] = \033[34mtesoura\033[m
\nQual é sua jogada: '''))

    print('\nJO')
    sleep(0.3)
    print('KEN')
    sleep(0.3)
    print('PÔ!!!\n')
    sleep(0.3)

    print("\033[1;97m_\033[m" *25)
    print('O computador jogou {}'.format(itens[comp]))
    print('Você jogou {}'.format(itens[x]))
    print("\033[1;97m_\033[m" *25)

    if x == 0:
        if comp == 0:
            print('\n\033[1;33mEMPATE\033[m')
        if comp == 1:
            print('\n\033[1;31mVOCÊ PERDEU\033[m')
            break
        if comp == 2:
            print('\n\033[1;32mVOCÊ GANHOU\033[m')

    if x == 1:
        if comp == 0:
            print('\n\033[1;32mVOCÊ GANHOU\033[m')
        if comp == 1:
            print('\n\033[1;33mEMPATE\033[m')
        if comp == 2:
            print('\n\033[1;31mVOCÊ PERDEU\033[m')
            break

    if x == 2:
        if comp == 0:
            print('\n\033[1;31mVOCÊ PERDEU\033[m')
            break
        if comp == 1:
            print('\n\033[1;32mVOCÊ GANHOU\033[m')
        if comp == 2:
            print('\n\033[1;33mEMPATE\033[m')

    qtde += 1
    print('\nVamos jogar novamente...')
print(f'\nVocê obteve \033[32m{qtde}\033[m vitórias consecutivas')