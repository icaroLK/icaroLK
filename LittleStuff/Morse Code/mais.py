from playsound import playsound
from time import sleep

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


frase = input('Insira uma frase: ').strip().upper()
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
                sleep(0.3)
                print(valor, end=' ')


                for q in valor:
                    if q == '•': 

                        playsound("C:/TimeTravelStuff/icaroLK/LittleStuff/Morse Code/peep.wav")

                    elif q == '-':
                        playsound("C:/TimeTravelStuff/icaroLK/LittleStuff/Morse Code/pipao.wav")
                      
                break
            count += 1

