print('\033[1;97m=\033[m'*26)
print('     \033[97mTERMOS DE UMA PA\033[m     ')
print('\033[1;97m=\033[m'*26)

pri = int(input('\nPrimeiro termo: '))
raz = int(input('A razão da PA: '))
qtde = int(input('Quantidade de termos: '))

dec = pri + (qtde - 1) * raz

for c in range(pri, dec + raz, raz):
    print('{}'.format(c), end=" / ")
print('\033[31mFim\033[m')
