#include "mt.h"
#include <stdio.h>

int main()
{
    mt_clrscr();
    int rows, cols;
    mt_getscreensize(&rows, &cols);
    rows /= 2;
    cols /= 2;
    cols -= 10;
    mt_gotoXY(cols, rows);
    printf("Valerie Funtikoffa\n");
    mt_getscreensize(&rows, &cols);
    mt_gotoXY(cols, rows);
    printf(" ");
    return 0;
}
