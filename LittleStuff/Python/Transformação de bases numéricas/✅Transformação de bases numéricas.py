print('\033[1;97m_\033[m'*52)
print("\033[1;97m=\033[m"*6, "\033[1;97mCALCULADORA DE TRANSFORMAÇÕES DE BASES\033[m", "\033[1;97m=\033[m"*6)
print('\033[1;97m_\033[m'*52)

resp = int(input('\n\033[97m[1]\033[m Decimal pra \033[35mTUDO\033[m'
                 "\n\033[97m[2]\033[m Base 'n' pra \033[32mDECIMAL\033[m\n\nR: "))

if resp == 1:
    dec = int(input('Insira um número em decimal: '))
    print('\n\033[1;97mDECIMAL = {}\033[m\n'.format(dec))

    cu = dec
    binar = []
    while True:
        binar.append(cu % 2)
        if cu // 2 == 0 and cu % 2 == 0 and cu == 0:
            break
        cu = cu // 2
    bin = ((binar[::-1])[1:])
    qtd = len(bin)
    vez = 0
    print("\033[mBinário = \033[34m".format(dec), end='')
    while vez != qtd:
        print(bin[vez], end='')
        vez += 1

    cu = dec
    binar = []
    while True:
        binar.append(cu % 3)
        if cu // 3 == 0 and cu % 3 == 0 and cu == 0:
            break
        cu = cu // 3
    bin = ((binar[::-1])[1:])
    qtd = len(bin)
    vez = 0
    print("\n\033[mTernário = \033[34m".format(dec), end='')
    while vez != qtd:
        print(bin[vez], end='')
        vez += 1

    base = 4
    cu = dec
    binar = []
    while True:
        binar.append(cu % base)
        if cu // base == 0 and cu % base == 0 and cu == 0:
            break
        cu = cu // base
    bin = ((binar[::-1])[1:])
    qtd = len(bin)
    vez = 0
    print("\n\033[mQuaternário = \033[34m".format(dec), end='')
    while vez != qtd:
        print(bin[vez], end='')
        vez += 1

    base = 5
    cu = dec
    binar = []
    while True:
        binar.append(cu % base)
        if cu // base == 0 and cu % base == 0 and cu == 0:
            break
        cu = cu // base
    bin = ((binar[::-1])[1:])
    qtd = len(bin)
    vez = 0
    print("\n\033[mPental = \033[34m".format(dec), end='')
    while vez != qtd:
        print(bin[vez], end='')
        vez += 1

    base = 6
    cu = dec
    binar = []
    while True:
        binar.append(cu % base)
        if cu // base == 0 and cu % base == 0 and cu == 0:
            break
        cu = cu // base
    bin = ((binar[::-1])[1:])
    qtd = len(bin)
    vez = 0
    print("\n\033[mSenário = \033[34m".format(dec), end='')
    while vez != qtd:
        print(bin[vez], end='')
        vez += 1

    base = 7
    cu = dec
    binar = []
    while True:
        binar.append(cu % base)
        if cu // base == 0 and cu % base == 0 and cu == 0:
            break
        cu = cu // base
    bin = ((binar[::-1])[1:])
    qtd = len(bin)
    vez = 0
    print("\n\033[mSeptuário = \033[34m".format(dec), end='')
    while vez != qtd:
        print(bin[vez], end='')
        vez += 1

    base = 8
    cu = dec
    binar = []
    while True:
        binar.append(cu % base)
        if cu // base == 0 and cu % base == 0 and cu == 0:
            break
        cu = cu // base
    bin = ((binar[::-1])[1:])
    qtd = len(bin)
    vez = 0
    print("\n\033[mOctal = \033[34m".format(dec), end='')
    while vez != qtd:
        print(bin[vez], end='')
        vez += 1

    cu = dec
    hexa = []
    while True:
        if cu % 16 == 10:
            hexa.append('A')
        elif cu % 16 == 11:
            hexa.append('B')
        elif cu % 16 == 12:
            hexa.append('C')
        elif cu % 16 == 13:
            hexa.append('D')
        elif cu % 16 == 14:
            hexa.append('E')
        elif cu % 16 == 15:
            hexa.append('F')
        else:
            hexa.append(cu % 16)
        if cu // 16 == 0 and cu % 16 == 0 and cu == 0:
            break
        cu = cu // 16

    hex = ((hexa[::-1])[1:])
    qtd = len(hex)
    vez = 0
    print("\n\033[mHexadecimal = \033[34m".format(dec), end='')
    while vez != qtd:
        print(hex[vez], end='')
        vez += 1

elif resp == 2:
    base = int(input('\nInsira uma base entre 2 e 10: '))
    num = int(input('Insira um número na base {}: '.format(base)))
    dec = str(num)
    tamanho = len(dec) - 1
    vez = 0
    cu = []
    pos = -1
    resp = 0
    while vez != tamanho + 2:
        if dec[0] != '0':
            cu = base ** (tamanho - vez)
            pos += 1

            if pos == tamanho + 1:
                break

            if dec[pos] == '1':
                resp += cu

            if dec[pos] == '2':
                resp += (cu * 2)

            if dec[pos] == '3':
                resp += (cu * 3)

            if dec[pos] == '4':
                resp += (cu * 4)

            if dec[pos] == '5':
                resp += (cu * 5)

            if dec[pos] == '6':
                resp += (cu * 6)

            if dec[pos] == '7':
                resp += (cu * 7)

            if dec[pos] == '8':
                resp += (cu * 8)

            if dec[pos] == '9':
                resp += (cu * 9)

            if dec[pos] == '10':
                resp += (cu * 10)
            vez += 1
    print(''
          '\nBase {}: \033[36m{}\033[m'
          '\n  ='
          '\nBase decimal: \033[1;35m{}\033[m'.format(base, num, resp))
