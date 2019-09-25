#include <stdio.h>
#include "../include/alu.h"
#include "../include/sc.h"
#include "../include/gui.h"

int ALU(int command, int operand)
{
    if (command == 10)
        return READ(operand);
    else if (command == 11)
        return WRITE(operand);
    else if (command == 20)
        return LOAD(operand);
    else if (command == 21)
        return STORE(operand);
    else if (command == 30)
        return ADD(operand);
    else if (command == 31)
        return SUB(operand);
    else if (command == 32)
        return DIVIDE(operand);
    else if (command == 33)
        return MUL(operand);
    else if (command == 40)
        return JUMP(operand);
    else if (command == 41)
        return JNEG(operand);
    else if (command == 42)
        return JZ(operand);
    else if (command == 43)
        return HALT();
    else if (command == 51)
        return NOT(operand);
    else if (command == 52)
        return AND(operand);
    else if (command == 53)
        return OR(operand);
    else if (command == 54)
        return XOR(operand);
    else if (command == 55)
        return JNS(operand);
    else if (command == 56)
        return JC(operand);
    else if (command == 57)
        return JNC(operand);
    else if (command == 58)
        return JP(operand);
    else if (command == 59)
        return JNP(operand);
    else if (command == 60)
        return CHL(operand);
    else if (command == 61)
        return SHR(operand);
    else if (command == 62)
        return RCL(operand);
    else if (command == 63)
        return RCR(operand);
    else if (command == 64)
        return NEG(operand);
    else if (command == 65)
        return ADDC(operand);
    else if (command == 66)
        return SUBC(operand);
    else if (command == 67)
        return LOGLC(operand);
    else if (command == 68)
        return LOGRC(operand);
    else if (command == 69)
        return RCCL(operand);
    else if (command == 70)
        return RCCR(operand);
    else if (command == 71)
        return MOVA(operand);
    else if (command == 72)
        return MOVR(operand);
    else if (command == 73)
        return MOVCA(operand);
    else if (command == 74)
        return MOVCR(operand);
    else if (command == 75)
        return ADDC(operand);
    else if (command == 76)
        return SUBC(operand);
    sc_regSet(COMMAND_ERR, 1);
    return -1;
}

int READ(int operand)
{
    input_plz(--operand);
    return 0;
}

int WRITE(int operand)
{
    output(--operand);
    return 0;
}

int LOAD(int operand) 
{
    int value = 0;
    sc_memoryGet(--operand, &value);
    sc_accumSet(value);
    return 0;
}

int STORE(int operand)
{
    int a = 0;
    sc_accumGet(&a);
    sc_memorySet(--operand, a);
    return 0;
}

int ADD(int operand)
{
    int a = 0;
    sc_memoryGet(--operand, &a);
    int b = 0;
    sc_accumGet(&b);
    b += a;
    sc_accumSet(b);
    return 0;
}

int SUB(int operand)
{
    int a = 0;
    sc_memoryGet(--operand, &a);
    int b = 0;
    sc_accumGet(&b);
    b -= a;
    sc_accumSet(b);
    return 0;
}

int DIVIDE(int operand)
{
    int a = 0;
    sc_memoryGet(--operand, &a);
    int b = 0;
    sc_accumGet(&b);
    if (a == 0)
        sc_regSet(ZERO_ERR, 1);
    b /= a;
    sc_accumSet(b);
    return 0;
}

int MUL(int operand)
{
    int a = 0;
    sc_memoryGet(--operand, &a);
    int b = 0;
    sc_accumGet(&b);
    b *= a;
    sc_accumSet(b);
    return 0;
}

int JUMP(int operand)
{
    sc_instSet(--operand);
    return 0;
}

int JNEG(int operand)
{
    int tmp = 0;
    sc_accumGet(&tmp);
    if (tmp <= 0)
        sc_instSet(--operand);
    return 0;
}

int JZ(int operand)
{
    int tmp = 0;
    sc_accumGet(&tmp);
    if (tmp == 0)
        sc_instSet(--operand);
    return 0;
}

int HALT()
{
    sc_regSet(FREQ_ERR, 1);
    sc_instSet(0);
    return 0;
}

int NOT(int operand)
{
    int a = 0;
    sc_accumGet(&a);
    int flg = 0;
    if (a < 0) {
        a *= -1;
        flg++;
    }
    int b = 0;
    for (int i = 0; i < 8; i++) {
        if (!(a & (1 << i)))
            b |= 1 << i;
    }
    if (flg)
        b *= -1;
    sc_commandEncode(0, b, &a);
    sc_memorySet(--operand, a);
    return 0;
}

int AND(int operand)
{
    int a = 0;
    sc_accumGet(&a);
    int value = 0;
    sc_memoryGet(--operand, &value);
    int b = 0,
        tmp = 0;
    sc_commandDecode(value, &tmp, &b);
    int c = 0;
    for (int i = 0; i < 8; i++) 
        if ((a & (1 << i)) & (b & (1 << i)))
            c |= 1 << i;
    sc_accumSet(c);
    return 0;
}

int OR(int operand)
{
    int a = 0;
    sc_accumGet(&a);
    int value = 0;
    sc_memoryGet(--operand, &value);
    int b = 0,
        tmp = 0;
    sc_commandDecode(value, &tmp, &b);
    int c = 0;
    for (int i = 0; i < 8; i++)
        if ((a & (1 << i)) | (b & (1 << i)))
            c |= 1 << i;
    sc_accumSet(c);
    return 0;
}

int XOR(int operand)
{
    int a = 0;
    sc_accumGet(&a);
    int value = 0;
    sc_memoryGet(operand, &value);
    int b = 0,
        tmp = 0;
    sc_commandDecode(value, &tmp, &b);
    int c = 0;
    for (int i = 0; i < 8; i++)
        if ((a & (1 << i)) ^ (b & (1 << i)))
            c |= 1 << i;
    sc_accumSet(c);
    return 0;
}

int JNS(int operand)
{
    int tmp = 0;
    sc_accumGet(&tmp);
    if (tmp > 0)
        sc_instSet(--operand);
    return 0;
}

int JC(int operand)
{
    int tmp = 0;
    sc_accumGet(&tmp);
    if (tmp > 127 || tmp < -127)
        sc_instSet(--operand);
    return 0;
}

int JNC(int operand)
{
    int tmp = 0;
    sc_accumGet(&tmp);
    if (tmp > -128 || tmp < 128)
        sc_instSet(--operand);
    return 0;
}

int JP(int operand)
{
    int tmp = 0;
    sc_accumGet(&tmp);
    if (!(tmp % 2))
        sc_instSet(--operand);
    return 0;
}

int JNP(int operand)
{
    int tmp = 0;
    sc_accumGet(&tmp);
    if (tmp % 2)
        sc_instSet(operand);
    return 0;
}

int CHL(int operand)
{
    return 0;
}

int SHR(int operand)
{
    return 0;
}

int RCL(int operand)
{
    return 0;
}

int RCR(int operand)
{
    return 0;
}

int NEG(int operand)
{
    int a = 0,
        tmp = 0,
        value = 0;
    sc_memoryGet(--operand, &value);
    sc_commandDecode(value, &tmp, &a);
    sc_accumSet(!(a >= 0));
    return 0;
}

int ADDC(int operand)
{
    return 0;
}

int SUBC(int operand)
{
    return 0;
}

int LOGLC(int operand)
{
    return 0;
}

int LOGRC(int operand)
{
    return 0;
}

int RCCL(int operand)
{
    return 0;
}

int RCCR(int operand)
{
    return 0;
}

int MOVA(int operand)
{
    int tmp = 0;
    sc_memoryGet(--operand, &tmp);
    int dist = 0;
    sc_accumGet(&dist);
    sc_memorySet(dist, tmp);
    return 0;
}

int MOVR(int operand)
{
    int from = 0;
    sc_accumGet(&from);
    int tmp = 0;
    sc_memoryGet(from, &tmp);
    sc_memorySet(operand, tmp);
    return 0;
}

int MOVCA(int operand)
{
    int dist1 = 0;
    sc_accumGet(&dist1);
    int dist2 = 0;
    sc_memoryGet(dist1, &dist2);
    int tmp = 0;
    sc_memoryGet(operand, &tmp);
    sc_memorySet(dist2, tmp);
    return 0;
}

int MOVCR(int operand)
{
    int dist1 = 0;
    sc_accumGet(&dist1);
    int dist2 = 0;
    sc_memoryGet(dist1, &dist2);
    int tmp = 0;
    sc_memoryGet(dist2, &tmp);
    sc_memorySet(operand, tmp);
    return 0;
}

int ADDC1(int operand)
{
    return 0;
}

int SUBC2(int operand)
{
    return 0;
}

