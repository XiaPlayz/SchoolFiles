#include <stdio.h>
#include <ctype.h>
#include <unistd.h>

int main() {
    int count;
    printf("Let's Count From one to?: ");
    if (scanf("%d", &count) != 1) {
        printf("Invalid number\n");
        return 1;//If user input is not number it will automatically print Invalid Numbers
    }

    for (int i = 1; i <= count; i++) {
        printf("The value of count is %d\n", i);

        sleep(1);
    }

    return 0;
}
