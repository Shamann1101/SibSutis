#ifndef RK_H
#define RK_H

#include <termios.h>

struct termios def;
struct termios custom;

enum keys {
    up, down, left, right, f5, f6, q, l, s, i, t, r, enter, space, none
} keys;

int rk_readkey(enum keys *key);
int rk_mytermsave();
int rk_mytermrestore();
int rk_mytermregime(int regime, int vtime, int vmin, int echo, int sigint);

#endif
