#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

#include "mt.h"
#include "bc.h"
#include "hdd.h"

#define SECT_SIZE 512 

enum os_type {
    empty = 0x0, fat12 = 0x1, fat16 = 0x4, ext = 0x5, dosfat16 = 0x6, 
    ntfs = 0x7, winfat32 = 0xc, winfat16 = 0xe, swp = 0x82, nix = 0x83
} os_type;

void print_types()
{
	printf("0x00 Empty\n");
	printf("0x01 FAT12\n");
	printf("0x04 FAT16 <32M\n");
	printf("0x05 Extended\n");
	printf("0x06 MS-DOS FAT16\n");
	printf("0x07 HPFS/NTFS\n");
	printf("0x0c Win95 FAT32 (LBA.lba)\n");
	printf("0x0E Win95 FAT16\n");
	printf("0x82 Linux swap\n");
	printf("0x83 Linux\n");
  	return;
}

void show_partitions(tPART *part, int num_parts)
{
    mt_clrscr();

    bc_box(1, 1, 8, 3);
    mt_gotoXY(2, 2);
    write(1, "active", 6);

    bc_box(9, 1, 13, 3);
    mt_gotoXY(10, 2);
    write(1, "chs_beg", 7);

    bc_box(22, 1, 9, 3);
    mt_gotoXY(23, 2);
    write(1, "oc", 2);

    bc_box(31, 1, 13, 3);
    mt_gotoXY(32, 2);
    write(1, "chs_end", 7);

    bc_box(44, 1, 13, 3);
    mt_gotoXY(45, 2);
    write(1, "lba_beg", 7);

    bc_box(57, 1, 13, 3);
    mt_gotoXY(58, 2);
    write(1, "size", 4);

    for (int i = 0; i < num_parts; i++) {
        char tmp[255] = "\0";

        bc_box(1, 1 + 3 * (i + 1), 8, 3); //is this part of disk
        mt_gotoXY(2, 2 + 3 * (i + 1));   //activ (bootable)?
        sprintf(tmp, "%d", part[i].activ);
        write(1, tmp, strlen(tmp));

        bc_box(9, 1 + 3 * (i + 1), 13, 3); //begin chs
        mt_gotoXY(10, 2 + 3 * (i + 1));
        sprintf(tmp, "%d-%d-%d", part[i].beg.cyl, part[i].beg.head, part[i].beg.sec);
        write(1, tmp, strlen(tmp));

        bc_box(22, 1 + 3 * (i + 1), 9, 3); //type of partition
        mt_gotoXY(23, 2 + 3 * (i + 1));
        sprintf(tmp, "%xh", part[i].os);
        write(1, tmp, strlen(tmp));

        bc_box(31, 1 + 3 * (i + 1), 13, 3); //end chs
        mt_gotoXY(32, 2 + 3 * (i + 1));
        sprintf(tmp, "%d-%d-%d", part[i].end.cyl, part[i].end.head, part[i].end.sec);
        write(1, tmp, strlen(tmp));

        bc_box(44, 1 + 3 * (i + 1), 13, 3); //begin lba
        mt_gotoXY(45, 2 + 3 * (i + 1));
        sprintf(tmp, "%d", part[i].lba_beg.lba);
        write(1, tmp, strlen(tmp));

        bc_box(57, 1 + 3 * (i + 1), 13, 3); //size (in lba)
        mt_gotoXY(58, 2 + 3 * (i + 1));
        if (part[i].os == ext) {
            int size = 0;
            for (int j = i; j < num_parts; j++)
                size += part[j].size;
            sprintf(tmp, "%d", size);
            write(1, tmp, strlen(tmp));
        } else {
            sprintf(tmp, "%d", part[i].size);
            write(1, tmp, strlen(tmp));
        }

        mt_gotoXY(1, 1 + 3 * (i + 2));
    }
}

void enter_partitions(tPART *part, tCHS geo, int num_parts)
{
    int activ = 0;
    mt_clrscr();
    if (num_parts > 3)
        printf("will maded extenden partition\n");
    for (int i = 0; i < num_parts; i++) {
        if (!activ) {
            printf("is this part is active? (y\\n): ");
            char ans = getchar();
            if (ans == 'y') {
                part[i].activ = 1;
                activ++;
            }
        }
        int exit = 0,
            ext_flg = 0;
        while (!exit) {
            printf("enter OS type (h for help, t for table): ");
            char answ[5] = "\0";
            scanf("%s", answ);
            if (!strcmp(answ, "h")) {
                print_types();
                continue;
            }
            if (!strcmp(answ, "t")) {
                show_partitions(part, i);
                continue;
            }
            else {
                exit++;
                if (!strcmp(answ, "0x00"))
                    part[i].os = empty;
                else if (!strcmp(answ, "0x01"))
                    part[i].os = fat12;
                else if (!strcmp(answ, "0x04"))
                    part[i].os = fat16;
                else if (!strcmp(answ, "0x05")) {
                    part[i].os = ext;
                    ext_flg++;
                }
                else if (!strcmp(answ, "0x06"))
                    part[i].os = dosfat16;
                else if (!strcmp(answ, "0x07"))
                    part[i].os = ntfs;
                else if (!strcmp(answ, "0x0c"))
                    part[i].os = winfat32;
                else if (!strcmp(answ, "0xeh"))
                    part[i].os = winfat16;
                else if (!strcmp(answ, "0x82"))
                    part[i].os = swp;
                else if (!strcmp(answ, "0x83"))
                    part[i].os = nix;
                else
                    exit--;
            }
        }

        if (ext_flg) {
            part[i].lba_beg = (tLBA){part[i - 1].lba_beg.lba + 
                part[i - 1].size};
            a_lba2chs(geo, part[i].lba_beg, &part[i].beg);
            part[i].end = part[i].beg;
            continue;
        }

        if (i == 0)
            part[i].lba_beg.lba = 1;
        else {
            tLBA lba_tmp = {part[i - 1].lba_beg.lba + part[i - 1].size};
            part[i].lba_beg = lba_tmp;
        }
        
        printf("enter size: ");
        int s;
        scanf("%d", &s);
        part[i].size = s;

        a_lba2chs(geo, part[i].lba_beg, &part[i].beg);
        tLBA lba_tmp = {part[i].lba_beg.lba + part[i].size - 1};
        a_lba2chs(geo, lba_tmp, &part[i].end);
    }
}

int main()
{
    mt_clrscr();
    tCHS geo;
    printf("input c-h-s: ");
    scanf("%hd-%hd-%hd", &geo.cyl, &geo.head, &geo.sec);
    printf("input num of parts: ");
    int num_parts = 0;
    scanf("%d", &num_parts);
    getchar();
    tPART *part = (tPART*)malloc(sizeof(*part) * num_parts);
    enter_partitions(part, geo, num_parts);
    show_partitions(part, num_parts);
    return 0;
}
