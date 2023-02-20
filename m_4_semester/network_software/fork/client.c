#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h> // read(), write(), close()

// PORT number
#define PORT 4444

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("HELP ./client message\n");
        exit(1);
    }

    // Socket id
    int clientSocket, ret;

    // Client socket structure
    struct sockaddr_in cliAddr, serverAddr;

    // char array to store incoming message
    char buffer[1024];

    // Creating socket id
    clientSocket = socket(AF_INET,
                          SOCK_STREAM, 0);

    if (clientSocket < 0) {
        printf("Error in connection.\n");
        exit(1);
    }
    printf("Client Socket is created.\n");

    // Initializing socket structure with NULL
    memset(&cliAddr, '\0', sizeof(cliAddr));

    // Initializing buffer array with NULL
    memset(buffer, '\0', sizeof(buffer));

    // Assigning port number and IP address
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(PORT);

    // 127.0.0.1 is Loopback IP
    serverAddr.sin_addr.s_addr
            = inet_addr("127.0.0.1");

    // connect() to connect to the server
    ret = connect(clientSocket,
                  (struct sockaddr *) &serverAddr,
                  sizeof(serverAddr));

    if (ret < 0) {
        printf("Error in connection.\n");
        exit(1);
    }

    printf("Connected to Server.\n");

    if (recv(clientSocket, buffer, 1024, 0) < 0) {
        printf("Error in receiving data.\n");
    } else {
        printf("Server: %s\n", buffer);
        bzero(buffer, sizeof(buffer));
    }

    int delay = atoi(argv[1]);
    for (int i = 0; i < 10 * delay; ++i) {
        if (sendto(clientSocket, argv[1], strlen(argv[1]), 0, &serverAddr, sizeof(serverAddr)) < 0) {
            perror("Sendto error\n");
            exit(1);
        }
        sleep(delay);
    }

    return 0;
}
