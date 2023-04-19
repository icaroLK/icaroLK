from time import sleep
tabuleiro = ('''
      |      |      
   1  |   2  |   3  
______|______|______
      |      |      
   4  |   5  |   6   
______|______|______
      |      |
   7  |   8  |   9
      |      | 
''')
print("="*8, "\033[97mJOGO DA VELHA\033[m", "="*8)
sleep((0.3))
jog1 = str(input('Insira o nome do primeiro jogador: ')).title().strip()
jog2 = str(input('Insira o nome do segundo jogador: ')).title().strip()
print("\n{} jogará primeiro e será o '\033[1:32mX\033[m'\n"
      "{} jogará por segundo e será o '\033[1:34mO\033[m'".format(jog1, jog2))
sleep(1)
print(tabuleiro)

j1 = str(input('\n\033[97mPRIMEIRA RODADA\033[m\n'
               'Vez de {}\nEscolha uma casa: '.format(jog1))).strip()
tabuleiro = tabuleiro.replace(j1, '\033[1:32mX\033[m')
print(tabuleiro)
j2 = str(input('\n\033[97mSEGUNDA RODADA\033[m\n'
               'Vez de {}\nEscolha uma casa: '.format(jog2))).strip()
tabuleiro = tabuleiro.replace(j2, '\033[1:34mO\033[m')
print(tabuleiro)

j1 = str(input('\n\033[97mTERCEIRA RODADA\033[m\n'
               'Vez de {}\nEscolha uma casa: '.format(jog1))).strip()
tabuleiro = tabuleiro.replace(j1, '\033[1:32mX\033[m')

print(tabuleiro)

j2 = str(input('\n\033[97mSEGUNDA RODADA\033[m\n'
               'Vez de {}\nEscolha uma casa: '.format(jog2))).strip()
tabuleiro = tabuleiro.replace(j2, '\033[1:34mO\033[m')
print(tabuleiro)

