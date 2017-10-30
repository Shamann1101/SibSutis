#ifndef SC_H
#define SC_H

#include <stdio.h>

#define OVERFLOW 0x1
#define ZERO_ERR 0x2
#define OUT_OF_MEMORY 0x4 
#define FREQ_ERR 0x8 
#define COMMAND_ERR 0x10

#define OK 0
#define OOM -1
#define OPEN_ERR -2
#define WRITE_ERR -3
#define READ_ERR -4
#define WRONG_VALUE -5
#define WRONG_REGISTER -6
#define WRONG_OPERAND -7
#define WRONG_COMMAND -8

int memory[100], 
    reg_flag, 
    inst_cnt,
    accum, 
    run_flg;

int sc_memoryInit();
int sc_memorySet(int address, int value);
int sc_memoryGet(int address, int *value);
int sc_memorySave(const char *filename);
int sc_memoryLoad(const char *filename);
int sc_regInit();
int sc_regSet(int regist, int value);
int sc_regGet(int regist, int *value);
int sc_commandEncode(int command, int operand, int *value);
int sc_commandDecode(int value, int *command, int *operand);
int sc_instGet(int *value);
int sc_instSet(int value);
int sc_accumGet(int *value);
int sc_accumSet(int value);

#endif
