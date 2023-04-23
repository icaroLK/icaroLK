'''Não ipomtra em qaul odrem as lteras de uma plvarala esāto, a úncia cosia ipmotarnte é que a piremria e útmlia etejasm no lguar creto. Itso é poqrue nós não lmeos cdaa ltera isladoa, mas a plravaa cmoo um tdoo.'''

'''Não importa em qual ordem as letras de uma palavra estão, a única coisa importante é que a primeira e a última estejam no lugar certo. Isto é porque nós não lemos cada letra isolada, mas a palavra como um todo.'''



from random import shuffle

listadas = []

base = input('Insira um texto: ').strip().replace(
    ',', ' ,').replace('.', ' .').split()


for c in range(len(base)):
    hablas = []

    if len(base[c]) <= 3:
        listadas.append(base[c])

    if len(base[c]) > 3:
        temp = base[c][1:-1]
        for h in range(len(temp)):
            hablas.append(temp[h])

        shuffle(hablas)

        emb = ''.join(hablas)
        penis = base[c][0] + emb + base[c][-1]
        listadas.append(penis)

print('\nO texto com as letras das palavras embaralhadas fica: \033[34m')
for c in range(len(listadas)):

    if c+1 >= len(listadas):
        print(listadas[c], '\033[m')

    else:

        if listadas[c+1] == ',':
            print(listadas[c], end='')

        elif listadas[c+1] == '.':
            print(listadas[c], end='')
        else:
            print(listadas[c], end=' ')
print()