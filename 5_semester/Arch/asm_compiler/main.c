#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "sc.h"

FILE *input = NULL;

void load_file(const char *filename)
{
    if ((input = fopen(filename, "r")) == NULL) {
        fprintf(stderr, "Cannot open file: no such file\n");
        exit(EXIT_FAILURE);
    }
    return;
}

void translating(const char *filename)
{
    int i, 
        flg = 0;
    for (i = 0; !feof(input); i++) {
        int intstr = 0;
        if (!fscanf(input, "%d", &intstr)) {
            flg = 1;
            break;
        }
        char command[10] = "\0";
        int cmd = 0,
            operand = 0,
            value = 0;
        fscanf(input, "%s", command);
        if (feof(input))
            break;
        if (!strcmp(command, "READ")) 
            cmd = 10;
        else if (!strcmp(command, "WRITE")) 
            cmd = 11;
        else if (!strcmp(command, "LOAD")) 
            cmd = 20;
        else if (!strcmp(command, "STORE")) 
            cmd = 21;
        else if (!strcmp(command, "ADD")) 
            cmd = 30;
        else if (!strcmp(command, "SUB")) 
            cmd = 31;
        else if (!strcmp(command, "DIVIDE")) 
            cmd = 32;
        else if (!strcmp(command, "MUL")) 
            cmd = 33;
        else if (!strcmp(command, "JUMP")) 
            cmd = 40;
        else if (!strcmp(command, "JNEG")) 
            cmd = 41;
        else if (!strcmp(command, "JZ")) 
            cmd = 42;
        else if (!strcmp(command, "HALT")) 
            cmd = 43;
		else if (!strcmp(command, "="))
		    cmd = 1;
        else if (atoi(command) || command[0] == '0') {
            sc_memorySet(intstr, atoi(command));
            continue;
        } else {
            flg = 2;
            break;
        }

        if (!fscanf(input, "%d", &operand)) {
            flg = 3;
            break;
        }

        if (sc_commandEncode(cmd, operand, &value)) {
        	
			if (cmd == 1) {
		      sc_memorySet(--intstr, operand);
		      continue;
			}
		    
            flg = 4;
            break;
        }
        sc_memorySet(intstr, value);
    }
    if (!flg)
        sc_memorySave(filename);
    if (flg == 1) 
        fprintf(stderr, "line %d: expected num of line\n", ++i);
    if (flg == 2)
        fprintf(stderr, "line %d: wrong command\n", ++i);
    if (flg == 3)
        fprintf(stderr, "line %d: wrong operand\n", ++i);
    if (flg == 4)
        fprintf(stderr, "line %d: wrong command or operand\n", ++i);
}

int main(int argc, const char **argv)
{
	argc = 3;
	
	argv[0] = "sat";
	argv[1] = "fact.sa"; 
	argv[2] = "fact.o";
	
    if (argc < 3) {
        fprintf(stderr, "Usage: %s input.sa output.o\n", argv[0]);
        exit(EXIT_FAILURE);
    }
    sc_memoryInit();
    load_file(argv[1]);
    translating(argv[2]);
    return 0;
}
