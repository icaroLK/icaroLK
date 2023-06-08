dec = int(input('Insira um número em decimal: '))
cu = dec
binar = []
while cu // 2 != -1:
    binar.append(cu % 2)
    if cu // 2 == 0 and cu % 2 == 0 and cu == 0:
        break
    cu = cu // 2
bin = ((binar[::-1])[1:])
qtd = len(bin)
vez = 0
print("O número decimal '\033[34m{}\033[m' em binário é \033[34m".format(dec), end='')
while vez != qtd:
    print(bin[vez], end='')
    vez += 1
