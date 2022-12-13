#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
void main()
{
    char nom[40], gen;
    float estatura;
    int edad;
    printf("Dame tu nombre");
    gets(nom);
    printf("Genero[f/m]:");
    fflush(stdin); // limpia la memoria
    gen = getchar();
    printf("edad:");
    scanf("%d", &edad);
    printf("Estatura");
    scanf("%f" & estatura);
    system("cls");// Limpia la pantalla
    printf("Los datos son \n");
    printf("Nombre: %S \n", nom);
    printf("Generos:%c\n", gen);
    printf("Edad> %d \n", edad);
    printf("Estatura:%.2f \n"estatura);
    system("PAUSE");

}