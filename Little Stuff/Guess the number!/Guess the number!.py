from random import randint
qtd = 1
pc = randint(1, 10000)
resp = int(input('Pensei em um número entre 1 e 10000.\nQue número você acha que foi?\nR: '))
while resp != pc:
    print('\n\033[31mERRADO!!!\033[m')
    if pc > resp:
        print('Meu número é maior...')
    elif resp > pc:
        print('Meu número é menor...')
    resp = int(input('Tente novamente\nR: '))
    qtd += 1
print('\n\033[32mACERTOU!!!\033[m\nEu pensei no número {}\nVocê acertou em {} tentativas'.format(pc, qtd))
