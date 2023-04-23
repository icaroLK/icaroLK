from time import sleep

print('\033[1;37m=\033[m'*50)
print('\033[37m{:^50}\033[m'.format('DESENHANDO'))
print('\033[1;37m=\033[m'*50)
print()





while True:
    sleep(1.3)
    print('—'*23)
    print('   Escolha uma opção:\n   1 - Quadrado\n   2 - Losango\n   3 - Triângulo\n   4 - Sair')
    print('—'*23)
    esc = input('R: ').strip()[0]
    cu = int(esc)

    if cu == 1:
        cu = input('\nInsira um caractere: ').strip()[0]
        num = int(input('Insira um número (tamanho do quadrado): '))
        print()
        carac = cu + '  '

        for c in range(num):
            print('{}'.format(carac*num))

    if cu == 2:
        cu = input('Insira um caractere: ').strip()[0]
        num = int(input('Insira um número: '))
        print()
        carac = cu + ' '

        larg = 2 * num + 1
        qtd = 1
        minos = 0

        while qtd <= larg:
            print('{}'.format(' ' * (num - minos)*2), end='')
            print('{}'.format(carac*qtd))
            if qtd == larg:
                break
            qtd += 2
            minos += 1

        minos = num-1

        for c in range(larg//2):
            print('{}'.format(' ' * (num - minos)*2), end='')
            qtd -= 2
            print('{}'.format(carac*qtd))
            minos -= 1
            
    if cu == 3:
        cu = input('Insira um caractere: ').strip()[0]
        num = int(input('Insira um número (altura do triângulo): '))
        print()
        carac = cu + ' '

        larg = 2 * num + 1
        qtd = 1
        minos = 0

        while qtd < larg:
            print('{}'.format(' ' * (((num - minos)*2)-2)), end='')
            print('{}'.format(carac*qtd))
            if qtd == larg:
                break
            qtd += 2
            minos += 1

    if cu == 4:
        break
