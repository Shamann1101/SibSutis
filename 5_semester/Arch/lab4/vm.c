#include "vm.h"

int sc_memoryInit()
{
    for (int i = 0; i < 100; i++)
        memory[i] = 0;
    sc_regSet(OUT_OF_MEMORY, 0);
    return OK;
}

int sc_memorySet(int address, int value)
{
    if (address >= 0 && address < 100) {
        memory[address] = value;
        return OK;
    } else {
        sc_regSet(OUT_OF_MEMORY, 1);
        return OOM;
    }
}

int sc_memoryGet(int address, int *value)
{
    if (address >= 0 && address < 100) {
        *value = memory[address];
        return OK;
    } else {
        sc_regSet(OUT_OF_MEMORY, 1);
        return OOM;
    }
}

int sc_memorySave(char *filename)
{
    int code = OK;
    FILE *file = fopen(filename, "w");
    if (!file) 
        code = OPEN_ERR;
    if (!fwrite(memory, sizeof(int), 100, file)) 
        code = WRITE_ERR;
    fclose(file);
    return code;
}

int sc_memoryLoad(char *filename)
{
    FILE *file = fopen(filename, "r");
    if (file == NULL)
        return OPEN_ERR;
    sc_memoryInit();
    if (!fread(memory, sizeof(int), 100, file)) 
        return READ_ERR;
    fclose(file);
    return OK;
}

int sc_regInit()
{
    reg_flag = 0;
    return OK;
}

int sc_regSet(int regist, int value)
{
    if (regist >= 0x01 && regist <= 0x10) {
        if (value == 0)
            reg_flag &= ~regist;
        else if (value == 1)
            reg_flag |= regist;
        else 
            return WRONG_VALUE;
    } else 
        return WRONG_REGISTER;
    return OK;
}

int sc_regGet(int regist, int *value)
{
    if (regist >= 0x01 && regist <= 0x10)
        *value = (reg_flag & regist) > 0 ? 1 : 0;
    else 
        return WRONG_REGISTER;
    return OK;
}

int sc_commandEncode(int command, int operand, int *value)
{
    if (command >= 10 && command <= 76) {
        if (operand >= 0 && operand < 128)
            *value = (command << 7) | operand;
        else 
            return WRONG_OPERAND;
    } else {
        return WRONG_COMMAND;
    }
    return OK;
}

int sc_commandDecode(int value, int *command, int *operand)
{
    *command = (value >> 7);
    *operand = value & (~(*command << 7));
    if (*command >= 10 && *command <= 76) {
        if (*operand >= 0 && *operand < 128) {
            return OK;
        } else {
            *operand = 0;
            return WRONG_OPERAND;
        }
    } else {
        *command = 0;
        return WRONG_COMMAND;
    }
}
