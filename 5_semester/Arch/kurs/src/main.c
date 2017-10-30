#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/time.h>

#include "../include/gui.h"
#include "../include/mt.h"
#include "../include/rk.h"
#include "../include/sc.h"

struct itimerval nval, oval;

void sighandler(int signum)
{
    if (signum == SIGALRM)
        CU();
}

int main()
{
    signal(SIGALRM, sighandler);

    nval.it_interval.tv_sec = 0;
    nval.it_interval.tv_usec = 400000;
    nval.it_value.tv_sec = 0;
    nval.it_value.tv_usec = 200000;
    setitimer(ITIMER_REAL, &nval, &oval);

    init();

    simple_computer();

    write(1, "\e[0m", 4);
    rk_mytermrestore();
    mt_clrscr();
    return 0;
}
