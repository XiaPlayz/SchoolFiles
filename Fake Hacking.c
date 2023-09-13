#include <stdio.h>
#include <unistd.h>
#include <conio.h>

int main() {
    
    printf("Hacking NASA\n");

    int i;

    for (i = 10; i <= 100; i += 10) {
        printf("Progress:%d%% Done.\n", i); // Updated format string
        fflush(stdout);
        usleep(500000);
    }

    printf("Hacked Successfully.\n");
    printf("Press any key to exit...\n");
    getch();
    return 0;
}
