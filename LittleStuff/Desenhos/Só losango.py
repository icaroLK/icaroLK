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
    
