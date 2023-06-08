#include <stdio.h>
#include <locale.h>
#include <math.h>
int main(){
    setlocale(LC_ALL, "Portuguese");
    float a, b, c, delta, um, dois;
    printf("Valor de 'a': ");
    scanf("%f", &a);
    printf("Valor de 'b': ");
    scanf("%f", &b);
    printf("Valor de 'c': ");
    scanf("%f", &c);
    printf("\nAnalisando a função: %.0fx² + %.0fx + %.0f = 0", a, b, c);

    delta = pow(b, 2) - 4*a*c;
    printf("\n\nDelta = %.0f", delta);

    if(delta<0) printf("Delta negativo, logo não existe solução real");
    else{

        um = (- b + sqrt(delta))/(2*a);
        dois = (- b - sqrt(delta))/(2*a);


        printf("\n\nx' = %.2f", um);
        printf("\nx'' = %.2f\n\n\n", dois);
    }

return 0;
}
