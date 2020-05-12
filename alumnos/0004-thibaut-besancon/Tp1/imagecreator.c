#include <stdio.h>
#include <stdlib.h>
#define LIN 156 //*3
#define COL 50


int main ()
{
   int T[LIN][COL];
    FILE* file = fopen("image.ppm", "w");
    fputs("P6\n# Imagen ppm\n",file);
    fprintf(file,"%d %d\n",LIN/3, COL);
    fputs("255\n",file);
   srand(50); /* MODIF */

    for (int i = 0; i < LIN; i++)
   {
       for(int j=0;j<COL;j++)
       {
            T[i][j] = rand ()%255;
            fprintf(file,"%d ",T[i][j]);
       }
       fprintf(file,"\n");
   }
   fclose(file);
   return 0;
}
