#include <iostream>
#include <vector>
#include <signal.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <pthread.h>
#include <sys/socket.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <libgen.h>

using namespace std;

/* Represents a client connection and its associated thread */
struct client_session {
    int sock;
    struct sockaddr addr;
    socklen_t addrlen;
    pthread_t thread;
};

/* Server socket */
int server;

/* List of client connections and their associated threads */
vector<client_session *> sessions;
pthread_mutex_t sessions_mutex;

/* Reads a line from a TCP socket */
string recv_line(int sock) {
    char c;
    string buf;
    for (size_t i = 0; buf.size() >= 2 ? buf.compare(buf.size() - 2, 2, "\r\n") : 1; i++) {
        if (recv(sock, &c, 1, 0) < 1) break;
        buf.push_back(c);
    }
    return buf;
}

/* Sends a string through a TCP socket */
ssize_t send_line(int sock, const char *str) {
    size_t len = strlen(str);
    return send(sock, str, len, 0);
}

/* Closes a client socket and removes it from the connection list */
void close_connection(int sock) {
    size_t i;
    pthread_mutex_lock(&sessions_mutex);
    for (i = 0; i < sessions.size(); i++) {
        if (sessions[i]->sock == sock) break;
    }
    if (i == sessions.size()) {
        return;
    };
    shutdown(sessions[i]->sock, SHUT_RDWR);
    close(sessions[i]->sock);
    sessions.erase(sessions.begin() + i);
    pthread_mutex_unlock(&sessions_mutex);
}

/* Closes all client sockets and threads and exits */
void shutdown_webserver(int) {
    size_t i;
    pthread_mutex_lock(&sessions_mutex);
    cout << "Shutting down " << sessions.size() << " connections..." << endl;
    for (i = 0; i < sessions.size(); i++) {
        shutdown(sessions[i]->sock, SHUT_RDWR);
        close(sessions[i]->sock);
        pthread_cancel(sessions[i]->thread);
        delete sessions[i];
    }
    pthread_mutex_unlock(&sessions_mutex);
    pthread_mutex_destroy(&sessions_mutex);
    shutdown(server, SHUT_RDWR);
    close(server);
    exit(0);
}

/* Unescape URL */
string unescape_pathname(const char *path) {
    char c;
    string s;
    for (size_t i = 0; path[i]; i++) {
        if (path[i] == '%') {
            sscanf(&(path[++i]), "%02hhx", &c);
            s += c;
            while (isdigit(path[i])) i++;
            i--;
        } else s += path[i];
    }
    return s;
}

/* Handles HTTP connection */
void *handle_connection(void *arg) {
    char ip[64];
    char response[512];
    FILE *p;
    client_session *cs = (client_session *) arg;
    int sock = cs->sock;
    string header, file, mimetype(64, 0), dir;

    /* Read HTTP header */
    do {
        header += recv_line(sock);
    } while (header.compare(header.size() - 4, 4, "\r\n\r\n"));

    /* Unescape URL path */
    if (header.compare(0, 4, "GET ") == 0 || header.compare(0, 5, "HEAD ") == 0)
        file = unescape_pathname(
                header.substr(
                        header.find(' ') + 2,
                        header.find(' ', header.find(' ') + 1) - (header.find(' ') + 2)
                ).c_str()
        );

    struct stat st;
    cout << inet_ntop(AF_INET, &(cs->addr), ip, cs->addrlen) << " -> /" << file << endl;
    if (file.empty()) file = ".";

    /* File not found */
    if (stat(file.c_str(), &st) == -1) {
        send_line(sock, "HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\n\r\n");
        goto handle_connection_done;

        /* Forbidden */
    } else if (access(file.c_str(), R_OK) == -1) {
        send_line(sock, "HTTP/1.1 403 Forbidden\r\nContent-Length: 0\r\n\r\n");
        goto handle_connection_done;

        /* Check for index.html if directory */
    } else if (S_ISDIR(st.st_mode)) {
        dir = file;
        file = string(dirname(&dir[0])).append("/index.html");
        if (stat(file.c_str(), &st) == -1) {
            send_line(sock, "HTTP/1.1 404 Not Found\r\nContent-Length: 0\r\n\r\n");
            goto handle_connection_done;
        }
    }

    /* Determine mimetype */
    p = popen(string("/usr/bin/file --mime-type ").append(file).c_str(), "r");
    fgets(&mimetype[0], 64, p);
    pclose(p);
    mimetype.erase(0, mimetype.find(' ') + 1);
    mimetype.erase(mimetype.find('\n'), 1);

    /* Send response header */
    sprintf(response,
            "HTTP/1.1 200 OK\r\n"
            "Content-Length: %lu\r\n"
            "Content-Type: %s\r\n\r\n",
            st.st_size, mimetype.c_str()
    );
    send_line(sock, response);

    /* Send file contents */
    if (header.compare(0, 4, "GET ") == 0) {
        FILE *f = fopen(file.c_str(), "r");
        setbuffer(f, response, 512);
        int c;
        char ch;
        for (;;) {
            c = fgetc(f);
            if (c == -1) break;
            ch = c;
            if (send(sock, &c, 1, 0) < 1) break;
        }
        fclose(f);
    }

    handle_connection_done:
    close_connection(sock);
    delete cs;
    return 0;
}

int main(int argc, char **argv) {
    if (argc != 3) {
        cout <<
             "Webserver\n"
             "Usage: " << argv[0] << " PORT DIRECTORY\n"
                                     "Use CTRL-C to shutdown webserver.\n";
        return 1;
    }

    chdir(argv[2]);

    pthread_mutex_init(&sessions_mutex, 0);

    /* Bind CTRL-C to shutdown_webserver */
    struct sigaction sa;
    memset(&sa, 0, sizeof(sa));
    sa.sa_handler = shutdown_webserver;
    sigaction(SIGINT, &sa, 0);

    /* Query localhost */
    struct addrinfo hints, *ai;
    memset(&hints, 0, sizeof(hints));
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_protocol = IPPROTO_TCP;
    hints.ai_flags = AI_PASSIVE;
    getaddrinfo(0, argv[1], &hints, &ai);

    /* Create server socket */
    server = socket(ai->ai_family, ai->ai_socktype, ai->ai_protocol);

    /* Bind server socket */
    if (bind(server, ai->ai_addr, ai->ai_addrlen) == -1) {
        perror("bind");
        exit(1);
    }

    /* Set server socket to listen for connections */
    if (listen(server, 4) == -1) {
        perror("listen");
        exit(1);
    }
    freeaddrinfo(ai);

    client_session *cs;
    for (;;) {
        cs = new client_session;

        /* Accept connection */
        cs->sock = accept(server, &(cs->addr), &(cs->addrlen));

        /* Shutdown webserver if failed to accept connection */
        if (cs->sock == -1) raise(SIGINT);

        /* Start and detach client connection thread */
        pthread_create(&(cs->thread), 0, handle_connection, cs);
        pthread_detach(cs->thread);

        /* Add to connections list */
        pthread_mutex_lock(&sessions_mutex);
        sessions.push_back(cs);
        pthread_mutex_unlock(&sessions_mutex);
    }
}
