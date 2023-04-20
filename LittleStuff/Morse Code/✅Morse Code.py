from playsound import playsound
from time import sleep

def titulo(msg):
    print('\033[1;37m—\033[m'*50)
    print('\033[37m{:^50}\033[m'.format(msg))
    print('\033[1;37m—\033[m'*50)

alfbt = [{'A': '•-'}, 
         {'B': '-•••'}, 
         {'C': '-•-•'},
         {'D': '-••'},
         {'E': '•'},
         {'F': '••-•'},
         {'G': '--•'},
         {'H': '••••'},
         {'I': '••'},
         {'J': '•---'},
         {'K': '-•-'},
         {'L': '•-••'},
         {'M': '--'},
         {'N': '-•'},
         {'O': '---'},
         {'P': '•--•'},
         {'Q': '--•-'},
         {'R': '•-•'},
         {'S': '•••'},
         {'T': '-'},
         {'U': '••-'},
         {'V': '•••-'},
         {'W': '•--'},
         {'X': '-••-'},
         {'Y': '-•--'},
         {'Z': '--••'},
         ]





titulo('MORSE CODE')

#verificador de digitação certa
while True:
    resp = input('\n1 - Phrase to morse + beep\n2 - Morse to phrase\nR: ')
    try:
        resp = int(resp)
        if resp > 2 or resp < 1:
            print('\n\033[31mERROR\033[m\nPlease. Insert a valid option')
        else:
            break
    except:
        print('\n\033[31mERROR\033[m\nPlease. Insert a number')

if resp == 1:

    while True:
        som = input('Deseja ouvir os beeps? [S/N]: ').strip().title()[0]
        if som == 'S':
            pass
            break
        elif som == 'N':
            pass
            break
        else:
            print('Digite novamente')


    frase = input('\nInsira uma frase: ').strip().upper()
    len(frase)


    for c, l in enumerate(frase):
        if l == ' ':
            print('/ ', end='')
        else:
            count = 0
            while True:
                c
                key = list(alfbt[count].keys())[0]
                #print(key)
                if l == key:
                    valor = list(alfbt[count].values())[0]
       #             sleep(0.3)
                    print(valor, end=' ')

                    if som == 'S':
                        sleep(0.3)
                        for q in valor:
                            if q == '•': 

                                playsound("C:/TimeTravelStuff/icaroLK/LittleStuff/Morse Code/peep.wav")

                            elif q == '-':
                                playsound("C:/TimeTravelStuff/icaroLK/LittleStuff/Morse Code/pipao.wav")
                    break
                count += 1

if resp == 2:
    sent = input('\nInsira uma frase em código morse: ').strip()
    frase = sent.replace('.', '•').split()
    print('Frase em código morse: \033[33m{}\033[m\nFrase traduzida: \033[34m'.format(sent), end='')
#    print(frase) vendo se ta certo só
    for c in frase:
        if c == '/':
            print(' ', end='')
        else:
            count = 0
            while True:
                valor = list(alfbt[count].values())[0]
                if c == valor:
                    key = (list(alfbt[count].keys())[0]).lower()
                    print(key, end='')
                    break
                count += 1
    print('\033[m')
