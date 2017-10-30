#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>

#include "../include/gui.h"
#include "../include/sc.h"
#include "../include/mt.h"
#include "../include/rk.h"
#include "../include/bc.h"

int *alph = NULL;

void print_mem()
{
    int freq_flg = 0,
        ins_cnt = 0;
    sc_regGet(FREQ_ERR, &freq_flg);
    if (!freq_flg) {
        sc_instGet(&ins_cnt);
        x = ins_cnt % 10;
        y = ins_cnt / 10;
    }
    for (int i = 0; i < 100; i++) {
        mt_gotoXY(2 + 6 * (i / 10), 2 + (i % 10));
        if (x > 9)
            x = 0;
        if (x < 0)
            x = 9;
        if (y > 9)
            y = 0;
        if (y < 0)
            y = 9;
        if (i / 10 == y && i % 10 == x)
            mt_setbgcolor(red);
        int command = 0, operand = 0, value = 0;
        sc_memoryGet(i, &value);
        char tmp1[10];
        if (value & (1 << 14) && value > 0) {
            sc_commandDecode(value, &command, &operand);
            if (command < 16 && operand < 16)
                sprintf(tmp1, "0%x:0%x", command, operand);
            else if (command < 16 && operand >= 16)
                sprintf(tmp1, "0%x:%x", command, operand);
            else if (command >= 16 && operand < 16)
                sprintf(tmp1, "%x:0%x", command, operand);
            else
                sprintf(tmp1, "%x:%x", command, operand);
        } else {
            int tmp = value,
                i = 3;
            if (value < 0)
                i--;
            for ( ; i >= 0 && tmp > 10; i--)
                tmp /= 10;
            if (i == 0)
                sprintf(tmp1, "%d", value);
            else if (i == 1)
                sprintf(tmp1, "0%d", value);
            else if (i == 2)
                sprintf(tmp1, "00%d", value);
            else if (i == 3)
                sprintf(tmp1, "000%d", value);
        }
        write(1, tmp1, strlen(tmp1));
        mt_setbgcolor(deflt);
    }
}

void print_accum()
{
    mt_gotoXY(71, 2);
    char mda[] = "    ";
    write(1, mda, strlen(mda));
    mt_gotoXY(71, 2);
    int acc = 0;
    sc_accumGet(&acc);
    char tmp[4];
    sprintf(tmp, "%d", acc);
    write(1, tmp, strlen(tmp));
}

void print_instcnt()
{
    mt_gotoXY(71, 5);
    int inst = 0;
    sc_instGet(&inst);
    char tmp[4];
    sprintf(tmp, "%d", inst);
    write(1, tmp, strlen(tmp));
}

void print_operation()
{
    int value = 0,
        command = 0,
        operand = 0,
        pos = y * 10 + x;
    char tmp[5] = "\0";
    sc_memoryGet(pos, &value);
    sc_commandDecode(value, &command, &operand);
    mt_gotoXY(69, 8);
    char mda[] = "               ";
    write(1, mda, strlen(mda));
    mt_gotoXY(66, 8);
    sprintf(mda, "%d: ", pos);
    write(1, mda, strlen(mda));
    if (value & (1 << 14) && value > 0) {
        if (command == 10)
            write(1, "READ : ", 7);
        else if (command == 11)
            write(1, "WRITE : ", 8);
        else if (command == 20)
            write(1, "LOAD : ", 7);
        else if (command == 21)
            write(1, "STORE : ", 8);
        else if (command == 30)
            write(1, "ADD : ", 6);
        else if (command == 31)
            write(1, "SUB : ", 6);
        else if (command == 32)
            write(1, "DIVIDE : ", 9);
        else if (command == 33)
            write(1, "MUL : ", 6);
        else if (command == 40)
            write(1, "JUMP : ", 7);
        else if (command == 41)
            write(1, "JNEG : ", 7);
        else if (command == 42)
            write(1, "JZ : ", 5);
        else if (command == 43)
            write(1, "HALT : ", 7);
        else if (command == 51)
            write(1, "NOT : ", 6);
        else if (command == 52)
            write(1, "AND : ", 6);
        else if (command == 53)
            write(1, "OR : ", 5);
        else if (command == 54)
            write(1, "XOR : ", 6);
        else if (command == 55)
            write(1, "JNS : ", 6);
        else if (command == 56)
            write(1, "JC : ", 5);
        else if (command == 57)
            write(1, "JNC : ", 6);
        else if (command == 58)
            write(1, "JP : ", 5);
        else if (command == 59)
            write(1, "JNP : ", 6);
        else if (command == 60)
            write(1, "CHL : ", 6);
        else if (command == 61)
            write(1, "SHR : ", 6);
        else if (command == 62)
            write(1, "RCL : ", 6);
        else if (command == 63)
            write(1, "RCR : ", 6);
        else if (command == 64)
            write(1, "NEG : ", 6);
        else if (command == 65)
            write(1, "ADDC : ", 7);
        else if (command == 66)
            write(1, "SUBC : ", 7);
        else if (command == 67)
            write(1, "LOGLC : ", 8);
        else if (command == 68)
            write(1, "LOGRC : ", 8);
        else if (command == 69)
            write(1, "RCCL : ", 7);
        else if (command == 70)
            write(1, "RCCR : ", 7);
        else if (command == 71)
            write(1, "MOVA : ", 7);
        else if (command == 72)
            write(1, "MOVR : ", 7);
        else if (command == 73)
            write(1, "MOVCA : ", 8);
        else if (command == 74)
            write(1, "MOVCR : ", 8);
        else if (command == 75)
            write(1, "ADDC : ", 7);
        else if (command == 76)
            write(1, "SUBC : ", 7);
        sprintf(tmp, "%d", operand);
    } else {
        sprintf(tmp, "%d", value);
    }
    write(1, tmp, strlen(tmp));
}

void print_flg()
{
    char tmp1[] = "OZMFC";
    mt_gotoXY(67, 11);
    for (int i = 0; i < 5; i++) {
        int value;
        sc_regGet(1 << i, &value);
        if (value)
            mt_setfgcolor(red);
        char tmp2[3];
        sprintf(tmp2, "%c ", tmp1[i]);
        write(1, tmp2, strlen(tmp2));
        mt_setfgcolor(deflt);
    }
}

void print_membc()
{
    int value, command, operand;
    sc_memoryGet(10 * y + x, &value);
    sc_commandDecode(value, &command, &operand);
    if (value & (1 << 14)) {
        int big[] = {alph[command / 16 * 2], alph[command / 16 * 2 + 1]};
        bc_printbigchar(big, 2 + 10 * 0, 14, deflt, deflt);
        int big1[] = {alph[command % 16 * 2], alph[command % 16 * 2 + 1]};
        bc_printbigchar(big1, 2 + 10 * 1, 14, deflt, deflt);
        int big2[] = {alph[16 * 2], alph[16 * 2 + 1]};
        bc_printbigchar(big2, 2 + 10 * 2, 14, deflt, deflt);
        int big3[] = {alph[operand / 16 * 2], alph[operand / 16 * 2 + 1]};
        bc_printbigchar(big3, 2 + 10 * 3, 14, deflt, deflt);
        int big4[] = {alph[operand % 16 * 2], alph[operand % 16 * 2 + 1]};
        bc_printbigchar(big4, 2 + 10 * 4, 14, deflt, deflt);
    } else {
        if (value > 0) {
            int big2[] = {alph[16 * 2], alph[16 * 2 + 1]};
            bc_printbigchar(big2, 2 + 10 * 0, 14, deflt, deflt);
        } else
            value *= -1;
        int big[] = {alph[value / 16 / 16 / 16 * 2], alph[value / 16 / 16 / 16 * 2 + 1]};
        bc_printbigchar(big, 2 + 10 * 1, 14, deflt, deflt);
        int big1[] = {alph[value / 16 / 16 * 2], alph[value / 16 / 16 * 2 + 1]};
        bc_printbigchar(big1, 2 + 10 * 2, 14, deflt, deflt);
        int big3[] = {alph[value / 16 * 2], alph[value / 16 * 2 + 1]};
        bc_printbigchar(big3, 2 + 10 * 3, 14, deflt, deflt);
        int big4[] = {alph[value % 16 * 2], alph[value % 16 * 2 + 1]};
        bc_printbigchar(big4, 2 + 10 * 4, 14, deflt, deflt);
    }
}

void print_keys()
{
    bc_box(51, 13, 33, 10);
    mt_gotoXY(52, 13);
    const char tmp[] = " Keys: ";
    write(1, tmp, strlen(tmp));
    const char *tmp1[] = {"l - load", "s - save", "r - run", "t - step",
        "i - reset", "F5 - accumulator", "F6 - instructionCounter"};
    for (int i = 0; i < 7; i++) {
        mt_gotoXY(52, 14 + i);
        write(1, tmp1[i], strlen(tmp1[i]));
    }
}

void load_mem()
{
    bc_box(20, 6, 20, 5);
    mt_gotoXY(24, 7);
    write(1, "Load\n", strlen("load\n"));
    char tmp[255] = "\0";
    mt_gotoXY(21, 9);
    read(1, tmp, 255);
    tmp[strlen(tmp) - 1] = '\0';
    if (sc_memoryLoad(tmp)) {
        bc_box(20, 6, 20, 5);
        mt_gotoXY(23, 7);
        write(1, "Failed to open\n", strlen("Failed to open\n"));
        mt_gotoXY(29, 9);
        mt_setbgcolor(red);
        write(1, "OK", strlen("OK"));
        mt_setbgcolor(deflt);
        mt_gotoXY(30, 9);
        read(1, tmp, 1);
    }
    refresh();
}

void save_mem()
{
    bc_box(20, 6, 20, 5);
    mt_gotoXY(23, 7);
    write(1, "Save to\n", strlen("Save to\n"));
    char tmp[255] = "\0";
    mt_gotoXY(21, 9);
    read(1, tmp, 255);
    tmp[strlen(tmp) - 1] = '\0';
    if (sc_memorySave(tmp)) {
        bc_box(20, 6, 20, 5);
        mt_gotoXY(23, 7);
        write(1, "Failed to save\n", strlen("Failed to open\n"));
        mt_gotoXY(29, 9);
        mt_setbgcolor(red);
        write(1, "OK", strlen("OK"));
        mt_setbgcolor(deflt);
        mt_gotoXY(30, 9);
        read(1, tmp, 1);
    }
    refresh();
}

void input_plz(int pos)
{
    rk_mytermrestore(); //чтобы ввод работал
    sc_regSet(FREQ_ERR, 1);
    bc_box(20, 6, 20, 5);
    mt_gotoXY(21, 7);
    write(1, "Input value (dec)\n", strlen("Input value (dec)\n"));
    char tmp[10] = "\0";
    mt_gotoXY(21, 9);
    read(1, tmp, 10);
    int mda = atoi(tmp);
    sc_memorySet(pos, mda);
    refresh();
    sc_regSet(FREQ_ERR, 0);
    rk_mytermsave();
}

void output(int pos)
{
    sc_regSet(FREQ_ERR, 1);
    bc_box(20, 6, 20, 5);
    mt_gotoXY(23, 7);
    int value;
    sc_memoryGet(pos, &value);
    char tmp[10] = "\0";
    sprintf(tmp, "%d", value);
    write(1, tmp, strlen(tmp));
    mt_gotoXY(29, 9);
    mt_setbgcolor(red);
    write(1, "OK", strlen("OK"));
    mt_setbgcolor(deflt);
    mt_gotoXY(30, 9);
    read(1, tmp, 1);
    sc_regSet(FREQ_ERR, 0);
}

void set_accum()
{
    bc_box(20, 6, 20, 5);
    mt_gotoXY(23, 7);
    write(1, "Set accum to\n", strlen("Sav tocum to\n"));
    char tmp[5] = "\0";
    mt_gotoXY(21, 9);
    read(1, tmp, 5);
    int new_acc = atoi(tmp);
    sc_accumSet(new_acc);
    refresh();
}

void set_instcnt()
{
    bc_box(20, 6, 26, 5);
    mt_gotoXY(22, 7);
    write(1, "Set instructionCounter to\n", strlen("Set instructionCounter to\n"));
    char tmp[5] = "\0";
    mt_gotoXY(21, 9);
    read(1, tmp, 5);
    tmp[strlen(tmp) - 1] = '\0';
    int new_inst = atoi(tmp);
    sc_instSet(new_inst);
    refresh();
}

void set_mem()
{
    bc_box(20, 6, 26, 5);
    mt_gotoXY(22, 7);
    write(1, "Set memory(dec) to\n", strlen("Set memory(dec) to\n"));
    char tmp[11] = "\0";
    mt_gotoXY(21, 9);
    read(1, tmp, 10);
    tmp[strlen(tmp) - 1] = '\0';
    int tmp1 = atoi(tmp);
    sc_memorySet(10 * y + x, tmp1);
    refresh();
}

void init()
{
    int fd = open("font", O_RDWR, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH);
    int cnt = 0;
    alph = (int*) malloc(sizeof(int) * 2 * 17);
    if (bc_bigcharread(fd, alph, 17, &cnt) == -1 && cnt < 17) {
        fprintf(stderr, "failed to load font\n");
        exit(EXIT_FAILURE);
    }

    sc_regSet(OVERFLOW, 0);
    sc_regSet(ZERO_ERR, 0);
    sc_regSet(OUT_OF_MEMORY, 0);
    sc_regSet(FREQ_ERR, 1);
    sc_regSet(COMMAND_ERR, 0);
    sc_memoryInit();
    sc_instSet(0);
    sc_accumSet(0);

    mt_clrscr();
}

void refresh()
{
    bc_box(1, 1, 61, 12);
    mt_gotoXY(30, 0);
    char tmp[] = " Memory ";
    write(1, tmp, sizeof(tmp));
    bc_box(62, 1, 22, 3);
    mt_gotoXY(66, 1);
    char tmp1[] = " accumulator ";
    write(1, tmp1, sizeof(tmp1));
    bc_box(62, 4, 22, 3);
    mt_gotoXY(63, 4);
    char tmp2[] = " instructionCounter ";
    write(1, tmp2, sizeof(tmp2));
    bc_box(62, 7, 22, 3);
    mt_gotoXY(68, 7);
    char tmp3[] = " Operation ";
    write(1, tmp3, sizeof(tmp3));
    bc_box(62, 10, 22, 3);
    mt_gotoXY(69, 10);
    char tmp4[] = " Flags ";
    write(1, tmp4, strlen(tmp4));
    bc_box(1, 13, 50, 10);
    print_keys();
    interface();
}

void key_handler(int *exit)
{
    int freq_flg;
    sc_regGet(FREQ_ERR, &freq_flg);
    enum keys key = none;
    rk_readkey(&key);

    if (key == r) {
        int tmp;
        sc_regGet(FREQ_ERR, &tmp);
        tmp = (tmp == 1) ? 0 : 1;
        sc_regSet(FREQ_ERR, tmp);
    }

    if (!freq_flg)
        return;
    if (key == q)
        *exit = 1;
    if (key == l)
        load_mem();
    if (key == s)
        save_mem();
    if (key == up)
        x--;
    if (key == down)
        x++;
    if (key == left)
        y--;
    if (key == right)
        y++;
    if (key == i) {
        init();
        x = 0, y = 0;
        refresh();
    }
    if (key == f5)
        set_accum();
    if (key == f6)
        set_instcnt();
    if (key == t) {
        sc_regSet(FREQ_ERR, 0);
        CU();
        interface();
        sc_regSet(FREQ_ERR, 1);
    }
    if (key == enter)
        set_mem();
    if (key == space)
        sc_instSet(y * 10 + x);
}

void interface()
{
    print_mem();
    print_accum();
    print_instcnt();
    print_operation();
    print_flg();
    print_membc();
}

void simple_computer()
{
    int exit = 0;
    int cnt = 0;
    x = y = 0;
    refresh();
    while (!exit) {
        interface();
        key_handler(&exit);
        if (cnt == 5) {
            mt_clrscr();
            refresh();
            cnt = 0;
        }
        cnt++;
    }
}
