from random import choice
import os



def trocar(msg, pos, carac):
    txt = list(msg)
    txt[pos] = carac
    new = ''.join(txt)
    return new





palavras = [
    "Abacate", "Banana", "Cachorro", "Dado", "Elefante", "Futebol","Gato", "Hambúrguer", "Isopor", "Jacaré", "Kiwi", "Limão", "Maçã","Nariz", "Óculos", "Pão" "Queijo", "Rato", "Sorvete", "Tigre", "Unicórnio", "Vaca", "Xícara", "Zebra", "Avestruz","Bolo","Camiseta", "Dinossauro", "Espelho", "Foguete","Girafa","Hipopótamo", "Igreja", "Janela", "Kanguru","Lanterna","Macaco", "Navio", "Ovelha", "Picolé", "Queimadura""Rosa","Sapato", "Tatuagem", "Uva", "Violino", "Xadrez","Zumbi","Árvore", "Bruxa"]
word = choice(palavras).lower()


print(word)
tam = len(word)
print(tam)

print("\n\033[37;1mJOGO Da FORCA\033[m")






qtd_erro = 0


palp = [ ]
pau = []


print("Escolha as letras certas!!!\n")

print('''
 _____
|     |
|
|
|
|''')

# print(" _____\n|     |\n|     1\n|    324 \n|    5 6 \n|")


penes = " _____\n|     |\n|     1\n|    324 \n|    5 6 \n|"
if qtd_erro > 0:
    if qtd_erro == 1:
        penes.replace("1", "O")
        print(penes)



for c in range(tam):
    if c == 0:
        print("|", end=' ')
    pau.append("_")
    print("_", end=" ")

pala = "".join(pau)
print()


count = 0


while True:
    count += 1
    if count == len(word)+1:
        break

    if len(palp) > 0:
        print(f"Seus palpites: {palp}")




    resp = input("\nInsira seu papite: ").strip().lower()[0]
    palp.append(resp)

    foi = 0

    for p, teste in enumerate(word):
        if teste == resp:
            foi = 1
            pala = trocar(pala, p, resp)
            

    if foi != 1:
        foi = 2

        
    if foi == 1:
        print("\nParabéns você acertou!!!")
        if qtd_erro > 0:
            if qtd_erro == 1:
                um = penes.replace("1", "O").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "")
                print(um)
            elif qtd_erro == 2:
                dois = penes.replace("1", "O").replace("2", " |").replace("3", "").replace("4", "").replace("5", "").replace("6", "")
                print(dois)
            elif qtd_erro == 3:
                tres = penes.replace("1", "O").replace("2", "|").replace("3", "/").replace("4", "").replace("5", "").replace("6", "")
                print(tres)
            elif qtd_erro == 4:
                quatro = penes.replace("1", "O").replace("2", "|").replace("3", "/").replace("4", "\ ").replace("5", "").replace("6", "")
                print(quatro)
            elif qtd_erro == 5:
                cinco = penes.replace("1", "O").replace("2", "|").replace("3", "/").replace("4", "\ ").replace("5", "/ ").replace("6", "")
                print(cinco)
    print(pala)
    if "_" not in pala:
        break

    if foi == 2:
        print("Erraste!!!")
        qtd_erro += 1
        if qtd_erro > 0:
            if qtd_erro == 1:
                um = penes.replace("1", "O").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "")
                print(um)
            elif qtd_erro == 2:
                dois = penes.replace("1", "O").replace("2", " |").replace("3", "").replace("4", "").replace("5", "").replace("6", "")
                print(dois)
            elif qtd_erro == 3:
                tres = penes.replace("1", "O").replace("2", "|").replace("3", "/").replace("4", "").replace("5", "").replace("6", "")
                print(tres)
            elif qtd_erro == 4:
                quatro = penes.replace("1", "O").replace("2", "|").replace("3", "/").replace("4", "\ ").replace("5", "").replace("6", "")
                print(quatro)
            elif qtd_erro == 5:
                cinco = penes.replace("1", "O").replace("2", "|").replace("3", "/").replace("4", "\ ").replace("5", "/ ").replace("6", "")
                print(cinco)
            elif qtd_erro == 6:
                seis = penes.replace("1", "O").replace("2", "|").replace("3", "/").replace("4", "\ ").replace("5", "/").replace("6", "\ ")
                print(seis)
                print("\n\nSuas tentativas acabaram :( \n\033[31mVocê perdeu\033[m")
                break
if foi == 2:
    print("Ruim em???")
    print(f"A palavra era: {word}")
        
if foi == 1:
    print("GANHOU PORRAAAAAAAAAA")































# print('''
#  _____
# |     |
# |     O
# |    /|\ 
# |    / \ 
# |
# ''')