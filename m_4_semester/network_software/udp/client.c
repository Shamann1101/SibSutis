#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h> // read(), write(), close()

#define BUFLEN 81

int main(int argc, char *argv[]) {
    int sock, length, msgLength;
    struct sockaddr_in serverAddress, clientAddress;
    struct hostent *hp, *gethostbyname();
    char buf[BUFLEN];

    if (argc < 4) {
        printf("HELP ./client host port message\n");
        exit(1);
    }

    if ((sock = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("Can\t get socket\n");
        exit(1);
    }

    bzero((char *) &serverAddress, sizeof(serverAddress));
    serverAddress.sin_family = AF_INET;
    hp = gethostbyname(argv[1]);
    bcopy(hp->h_addr, &serverAddress.sin_addr, hp->h_length);
    serverAddress.sin_port = htons(atoi(argv[2]));

    bzero((char *) &clientAddress, sizeof(clientAddress));
    clientAddress.sin_family = AF_INET;
    clientAddress.sin_addr.s_addr = htonl(INADDR_ANY);
    clientAddress.sin_port = 0;

    if (bind(sock, &clientAddress, sizeof(clientAddress))) {
        perror("Can\t get port");
        exit(1);
    }

    printf("CLIENT: Ready to transfer\n");

    int delay = atoi(argv[3]);
    for (int i = 0; i < 10 * delay; ++i) {
        if (sendto(sock, argv[3], strlen(argv[3]), 0, &serverAddress, sizeof(serverAddress)) < 0) {
            perror("Sendto error\n");
            exit(1);
        }
        length = sizeof(serverAddress);
        bzero(buf, sizeof(BUFLEN));
        if ((msgLength = recvfrom(sock, buf, BUFLEN, 0, &serverAddress, &length)) < 0) {
            perror("Recvfrom error\n");
            exit(1);
        }
        printf("SERVER: Message: %s\n\n", buf);
        sleep(delay);
    }

    printf("CLIENT: Success sent\n");
    close(sock);
}