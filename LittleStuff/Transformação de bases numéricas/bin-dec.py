num = int(input('Insira um número em \033[34mbinário\033[m: '))
dec = str(num)
tamanho = len(dec)-1
vez = 0
cu = []
pos = -1
resp = 0
while vez != tamanho+2:
    if dec[0] == '1':
        cu = 2 ** (tamanho - vez)
        pos += 1
        if pos == tamanho+1:
            break
        if dec[pos] == '1':
            resp += cu
        vez += 1

print('{}\033[34m₂\033[m = {}\033[32m₁₀\033[m'.format(num, resp))
