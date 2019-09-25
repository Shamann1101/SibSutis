#ifndef MYTERM_H
#define MYTERM_H

enum colors {
    black = 0, red, green, yellow, blue, 
    purple, cyan, white, deflt
} colors;

int mt_clrscr();
int mt_gotoXY(int x, int y);
int mt_getscreensize(int *rows, int *cols);
int mt_setfgcolor(enum colors);
int mt_setbgcolor(enum colors);

#endif
