#ifndef HDD_H
#define HDD_H

typedef struct CHS {
    unsigned short cyl; //10
    unsigned short head; //4
    unsigned short sec; //6
} tCHS;

typedef struct ECHS {
    unsigned short cyl; //10
    unsigned short head; //8
    unsigned short sec; //6
} tLARGE;

typedef struct IDECHS {
    unsigned short cyl; //16
    unsigned short head; //4
    unsigned short sec; //8
} tIDECHS;

typedef struct LBA {
    unsigned int lba; //32
} tLBA;

typedef struct PART {
    int activ;
    tCHS beg;
    int os;
    tCHS end;
    tLBA lba_beg;
    int size;
} tPART;

int g_lba2chs(tLBA orig, tCHS *dest);
int g_lba2large(tLBA orig, tLARGE *dest);
int g_lba2idechs(tLBA orig, tIDECHS *dest);
int g_chs2large(tCHS orig, tLARGE *dest);
int g_chs2idechs(tCHS orig, tIDECHS *dest);
int g_chs2lba(tCHS orig, tLBA *dest);
int g_large2chs(tLARGE orig, tCHS *dest);
int g_large2idechs(tLARGE orig, tIDECHS *dest);
int g_large2lba(tLARGE orig, tLBA *dest);
int g_idechs2chs(tIDECHS orig, tCHS *dest);
int g_idechs2large(tIDECHS orig, tLARGE *dest);
int g_idechs2lba(tIDECHS orig, tLBA *dest);
int a_lba2chs(tCHS geometry, tLBA orig, tCHS *dest);
int a_lba2large(tLARGE geometry, tLBA orig, tLARGE *dest);
int a_lba2idechs(tIDECHS geometry, tLBA orig, tIDECHS *dest);
int a_chs2large(tCHS geometry1, tLARGE geometry2, tCHS orig, tLARGE *dest);
int a_chs2idechs(tCHS geometry1, tIDECHS geometry2, tCHS orig, tIDECHS *dest);
int a_chs2lba(tCHS geometry1, tCHS orig, tLBA *dest);
int a_large2chs(tLARGE geometry1, tCHS geometry2, tLARGE orig, tCHS *dest);
int a_large2idechs(tLARGE geometry1, tIDECHS geometry2, tLARGE orig, tIDECHS *dest);
int a_large2lba(tLARGE geometry, tLARGE orig, tLBA *dest);
int a_idechs2chs(tIDECHS geometry1, tCHS geometry2, tIDECHS orig, tCHS *dest);
int a_idechs2large(tIDECHS geometry1, tLARGE geometry2, tIDECHS orig, tLARGE *dest);
int a_idechs2lba(tIDECHS geometry, tIDECHS orig, tLBA *dest);

#endif
