#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
#include <time.h>

void main(){
    setlocale(LC_ALL, "Portuguese");
    int resp, count, qtd;
    printf("Insira um \"range\" para o jogo: ");
    scanf("%i", &qtd);
    fflush(stdin);


    srand(time(NULL));
    int n = rand() % qtd + 1;
//  printf("Eu gerei o n�mero: %i", n);

    printf("\nEu pensei em um n�mero entre 1 e %i\nQue n�mero voc� acha que foi?\nR: ", qtd);
    scanf("%i", &resp);
    fflush(stdin);

    while (resp != n){
        printf("\nErrado!");
        if(n>resp) printf("\nMeu n�mero � maior...");
        else if(n<resp) printf("\nMeu n�mero � menor...");

        printf("Tente novamente\nR: ");
        scanf("%i", &resp);
        fflush(stdin);
        count ++;
    }
    printf("\nACERTOU!!!");
    printf("\nVoc� acertou em %i tentativas", count+1);

}
