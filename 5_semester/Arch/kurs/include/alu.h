#ifndef ALU_H
#define ALU_H

int ALU(int command, int operand);

int READ(int operand);
int WRITE(int operand);

int LOAD(int operand);
int STORE(int operand);

int ADD(int operand);
int SUB(int operand);
int DIVIDE(int operand);
int MUL(int operand);

int JUMP(int operand);
int JNEG(int operand);
int JZ(int operand);
int HALT();

int NOT(int operand);
int AND(int operand);
int OR(int operand);
int XOR(int operand);
int JNS(int operand);
int JC(int operand);
int JNC(int operand);
int JP(int operand);
int JNP(int operand);
int CHL(int operand);
int SHR(int operand);
int RCL(int operand);
int RCR(int operand);
int NEG(int operand);
int ADDC(int operand);
int SUBC(int operand);
int LOGLC(int operand);
int LOGRC(int operand);
int RCCL(int operand);
int RCCR(int operand);
int MOVA(int operand);
int MOVR(int operand);
int MOVCA(int operand);
int MOVCR(int operand);
int ADDC1(int operand);
int SUBC1(int operand);

#endif 
