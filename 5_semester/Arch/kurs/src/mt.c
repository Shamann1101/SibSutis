#include "../include/mt.h"
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <sys/ioctl.h>


int mt_clrscr()
/*
 * производит очистку и перемещение курсора в левый верхний угол экрана
 */
{
    write(1, "\E[H\E[J", strlen("\E[H\E[J"));
    return 0;
}

int mt_gotoXY(int x, int y)
/*
 * перемещает курсор в указанную позицию. Первый параметр номер строки, второй - номер столбца
 */
{
    char buf[15];
    int rows, cols;
    mt_getscreensize(&rows, &cols);
    if ((0 < x < cols) && (0 < y < rows)) {
        sprintf(buf, "\E[0%d;%dH", y, x);
        write(1, buf, strlen(buf));
    } else
        return -1;
    return 0;
}

int mt_getscreensize(int *rows, int *cols)
/*
 * определяет размер экрана терминала (количество строк и столбцов)
 */
{
    struct winsize {
        unsigned short ws_row;
        unsigned short ws_cols;
        unsigned short ws_xpixel;
        unsigned short ws_ypixel;
    } ws;
    if (!ioctl(1, TIOCGWINSZ, &ws)) {
        *rows = ws.ws_row;
        *cols = ws.ws_cols;
        return 0;
    } else {
        write(2, "Error getting size\n", strlen("Error getting size\n"));
        return -1;
    }
}

int mt_setfgcolor(enum colors colors)
/*
 * устанавливает цвет последующих выводимых символов. В качестве параметра передаѐтся константа
 * из созданного Вами перечислимого типа colors , описывающего цвета терминала
 */
{
    if ((int)colors < 0 || (int)colors > deflt)
        return -1;
    if ((int)colors == deflt) {
        write(1, "\e[0m", strlen("\e[0m"));
        return 0;
    }
    int color = (int)colors;
    char buf[8];
    sprintf(buf, "\E[3%dm", color);
    write(1, buf, strlen(buf));
    return 0;
}

int mt_setbgcolor(enum colors colors)
/*
 * устанавливает цвет фона последующих выводимых символов. В качестве параметра передаѐтся
 * константа из созданного Вами перечислимого типа colors , описывающего цвета терминала
 */
{
    if ((int)colors < 0 || (int)colors > deflt)
        return -1;
    if ((int)colors == deflt) {
        write(1, "\e[0m", strlen("\e[0m"));
        return 0;
    }
    int color = (int)colors;
    char buf[8];
    sprintf(buf, "\E[4%dm", color);
    write(1, buf, strlen(buf));
    return 0;
}

