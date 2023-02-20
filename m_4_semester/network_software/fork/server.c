#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

// PORT number
#define PORT 4444

int main() {
    // Server socket id
    int sockfd, ret;

    // Server socket address structures
    struct sockaddr_in serverAddr;

    // Client socket id
    int clientSocket;

    // Client socket address structures
    struct sockaddr_in cliAddr;

    // Stores byte size of server socket address
    socklen_t addr_size;

    // Child process id
    pid_t childpid;

    // Creates a TCP socket id from IPV4 family
    sockfd = socket(AF_INET, SOCK_STREAM, 0);

    // Error handling if socket id is not valid
    if (sockfd < 0) {
        printf("Error in connection.\n");
        exit(1);
    }

    printf("Server Socket is created.\n");

    // Initializing address structure with NULL
    memset(&serverAddr, '\0',
           sizeof(serverAddr));

    // Assign port number and IP address
    // to the socket created
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(PORT);

    // 127.0.0.1 is a loopback address
    serverAddr.sin_addr.s_addr
            = inet_addr("127.0.0.1");

    // Binding the socket id with
    // the socket structure
    ret = bind(sockfd,
               (struct sockaddr *) &serverAddr,
               sizeof(serverAddr));

    // Error handling
    if (ret < 0) {
        printf("Error in binding.\n");
        exit(1);
    }

    // Listening for connections (upto 10)
    if (listen(sockfd, 10) == 0) {
        printf("Listening...\n\n");
    }

    int cnt = 0;
    int read_size, length, msgLength;
    char buffer[1024], client_message[2000];
    signal(SIGCHLD, reaper);
    while (1) {

        // Accept clients and
        // store their information in cliAddr
        clientSocket = accept(sockfd, (struct sockaddr *) &cliAddr, &addr_size);

        // Error handling
        if (clientSocket < 0) {
            exit(1);
        }

        // Displaying information of
        // connected client
        printf("Connection accepted from %s:%d\n", inet_ntoa(cliAddr.sin_addr), ntohs(cliAddr.sin_port));

        // Print number of clients
        // connected till now
        printf("Clients connected: %d\n\n", ++cnt);

        // Creates a child process
        switch ((childpid = fork())) {
            case 0:

                // Closing the server socket id
                close(sockfd);

                // Send a confirmation message
                // to the client
                send(clientSocket, "hi client", strlen("hi client"), 0);

                for (;;) {
                    length = sizeof(cliAddr);
                    if ((msgLength = recvfrom(clientSocket, buffer, 1024, 0, &cliAddr, &length)) < 0) {
                        perror("Recvfrom error\n");
                        exit(1);
                    } else if (msgLength == 0) {
                        printf("SERVER: client disconnected\n");
                        cnt--;
                        close(clientSocket);
                        exit(0);
                    }

                    printf("SERVER: client IP: %s\n", inet_ntoa(cliAddr.sin_addr));
                    printf("SERVER: client PORT: %d\n", ntohs(cliAddr.sin_port));
                    printf("SERVER: Message length - %d\n", msgLength);
                    printf("SERVER: Message: %s\n\n", buffer);
                }
            default:
                close(clientSocket);
                break;
            case -1:
                perror("Signal error\n");
                exit(1);
        }
    }

    // Close the client socket id
    return 0;
}

void reaper(int sig) {
    int status;
    while (wait3(&status, WNOHANG, (struct rusage *) 0) >= 0);
}
