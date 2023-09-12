int main() {
    printf("Hello World or Hello Lord");
    int S1;
    printf("What year level are you?\n1. 1st year\n2. 2nd year\n3. 3rd year\n4. 4th year\nYour Choice: ");
    scanf("%d", &S1);

    if (S1 == 1) {
        printf("1st Year: Hello World!\nThe rest: Hello Lord!\n");
    } else {
        printf("I guess you're already in Hello Lord stage.\n");
    }

    return 1;
}
