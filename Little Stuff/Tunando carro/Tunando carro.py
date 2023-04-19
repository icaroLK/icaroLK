from time import sleep
p = float(input('Insira o valor do carro: R$'))
resp = str(input('\nTemos acessórios adicionais opcionais, gostaria de ve-los? ')).lower().replace('ã', 'a')
qtde = 0


if 'nao' in resp:
    print('O preço final do carro ficou \033[32mR${:.2f}\033[m'.format(p))

else:
    print('''
[1] = ar condicionado (\033[33mR$1000\033[m)
[2] = direção-hidraulica (\033[33mR$1000\033[m)
[3] = alarme (\033[33mR$1000\033[m)
[4] = caixa de som (\033[33mR$1000\033[m)''')

soun = str(input('\nGostaria de incluir algum? ')).lower().replace('ã', 'a')

print(' ')

if 'nao' in soun:
    print('O preço final do carro ficou \033[32mR${:.2f}\033[m'.format(p))

else:
    for qual in range(1, 5):
        bct = str(input('Gostaria de incluir o \033[34m{}\033[m? '.format(qual))).lower().replace('ã', 'a')
        if 'sim' in bct or 's' in bct:
            qtde = qtde + 1

print('\nIncluindo {} itens a sua sacola...'.format(qtde))
sleep(1.2)
print('O valor total dos acessórios ficou: \033[32mR${:.2f}\033[m'.format(qtde*1000))
print('\nVALOR FINAL: \033[32mR${}\033[m'.format(p+qtde*1000))
