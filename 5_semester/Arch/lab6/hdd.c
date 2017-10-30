#include <stdio.h>

#include "hdd.h"

int g_lba2chs(tLBA orig, tCHS *dest)
{
    dest->cyl = orig.lba / 15 / 63;
    dest->head = orig.lba / 15 % 63;
    dest->sec = orig.lba % 63 + 1;
    return 0;
}

int g_lba2large(tLBA orig, tLARGE *dest)
{
    dest->cyl = orig.lba / 63 / 255;
    dest->head = orig.lba / 63 % 255;
    dest->sec = orig.lba % 255 + 1;
    return 0;
}

int g_lba2idechs(tLBA orig, tIDECHS *dest)
{
    dest->cyl = orig.lba / 16 / 256;
    dest->head = orig.lba / 16 % 256;
    dest->sec = orig.lba % 256 + 1;
    return 0;
}

int g_chs2large(tCHS orig, tLARGE *dest)
{
    tLBA tmp;
    g_chs2lba(orig, &tmp);
    g_lba2large(tmp, dest);
    return 0;
}

int g_chs2idechs(tCHS orig, tIDECHS *dest)
{
    tLBA tmp;
    g_chs2lba(orig, &tmp);
    g_lba2idechs(tmp, dest);
    return 0;
}

int g_chs2lba(tCHS orig, tLBA *dest)
{
    dest->lba = (orig.head + 15 * orig.cyl) * 63 + orig.sec - 1;
    return 0;
}

int g_large2chs(tLARGE orig, tCHS *dest)
{
    tLBA tmp;
    g_large2lba(orig, &tmp);
    g_lba2chs(tmp, dest);
    return 0;
}

int g_large2idechs(tLARGE orig, tIDECHS *dest)
{
    tLBA tmp;
    g_large2lba(orig, &tmp);
    g_lba2idechs(tmp, dest);
    return 0;
}

int g_large2lba(tLARGE orig, tLBA *dest)
{
    dest->lba = (orig.head + 256 * orig.cyl) * 63 + orig.sec - 1;
    return 0;
}

int g_idechs2chs(tIDECHS orig, tCHS *dest)
{
    tLBA tmp;
    g_idechs2lba(orig, &tmp);
    g_lba2chs(tmp, dest);
    return 0;
}

int g_idechs2large(tIDECHS orig, tLARGE *dest)
{
    tLBA tmp;
    g_idechs2lba(orig, &tmp);
    g_lba2large(tmp, dest);
    return 0;
}

int g_idechs2lba(tIDECHS orig, tLBA *dest)
{
    dest->lba = (orig.head + 15 * orig.cyl) * 255 + orig.sec - 1;
    return 0;
}

int a_lba2chs (tCHS geometry, tLBA orig, tCHS *dest)
{
	int tmp;
	dest->cyl = (orig.lba / geometry.sec) / geometry.head;
    if (dest->cyl > geometry.cyl) {
        dest->cyl = geometry.cyl;
        dest->head = geometry.head;
        dest->sec = geometry.sec;
        return 0;
    }
	tmp = orig.lba % (geometry.head * geometry.sec);
	dest->head = tmp / geometry.sec;
	dest->sec = tmp % geometry.sec + 1;
	return 0;
}
