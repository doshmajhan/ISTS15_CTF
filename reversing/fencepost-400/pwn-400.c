#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include "pwnable_harness.h"

void get_flag() {
    printf("Roses are red, Harambe is ded. Mr skeletal doots and pepe is dank. I'll be here all week.\n");
    return;
}

void handler(int sock) {
    int is_admin = -1;
    char user_pass[32];
    char password[] = "roses-r-red-harambe-is-ded";

    printf("=== Welcome to the RC3 Secure CTF Login ===\n");
    printf("=== Please enter the correct password below ===\n");

    do {
        printf("Password: ");
        scanf("%s", user_pass);
        user_pass[strlen(user_pass) + 1] = '\0';
        printf("FLAG: %d\n", is_admin); // TODO REMOVE
    } while ( is_admin != 0 && strcmp(user_pass, password) != 0);

    if (is_admin == 0) {
        get_flag();
    }
}

int main(int argc, char *argv[]) {
    server_options opts = {
		.user = "ctfuser",
		.chrooted = 1,
		.port = 2091,
		.time_limit_seconds = 300
	}; 
    return server_main(argc, argv, opts, &handler);
}
