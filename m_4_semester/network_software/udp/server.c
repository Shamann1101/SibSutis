#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>

#define BUFLEN 81

int main() {
    int sock, length, msgLength;
    struct sockaddr_in serverAddress, clientAddress;
    char buf[BUFLEN];

    if ((sock = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("Server can\'t open UDP socket\n");
        exit(1);
    }

    bzero((char *) &serverAddress, sizeof(serverAddress));
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_addr.s_addr = htonl(INADDR_ANY);
    serverAddress.sin_port = 0;

    if (bind(sock, &serverAddress, sizeof(serverAddress))) {
        perror("Bind error\n");
        exit(1);
    }

    length = sizeof(serverAddress);
    if (getsockname(sock, &serverAddress, &length)) {
        perror("Getsockname error\n");
        exit(1);
    }

    printf("SERVER: port number - % d\n", ntohs(serverAddress.sin_port));

    for (;;) {
        length = sizeof(clientAddress);
        bzero(buf, sizeof(BUFLEN));
        if ((msgLength = recvfrom(sock, buf, BUFLEN, 0, &clientAddress, &length)) < 0) {
            perror("Recvfrom error\n");
            exit(1);
        }
        if (sendto(sock, buf, strlen(buf), 0, &clientAddress, sizeof(clientAddress)) < 0) {
            perror("Sendto error\n");
            exit(1);
        }

        printf("SERVER: client IP: %s\n", inet_ntoa(clientAddress.sin_addr));
        printf("SERVER: client PORT: %d\n", ntohs(clientAddress.sin_port));
        printf("SERVER: Message length - %d\n", msgLength);
        printf("SERVER: Message: %s\n\n", buf);
    }
}
