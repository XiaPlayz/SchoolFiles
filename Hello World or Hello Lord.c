int main() {
    int S1;

    while (1) {
        printf("What year level are you?\n1. 1st year\n2. 2nd year\n3. 3rd year\n4. 4th year\nYour Choice: ");
        scanf("%d", &S1);  // Take user input as an integer

        if (S1 == 1) {
            printf("1st Year: Hello World!\n");
            printf("The rest: Hello Lord!\n");
            break;  // Exit the loop if input is 1
        } else if (S1 == 2 || S1 == 3 || S1 == 4) {
            printf("I guess you're already in Hello Lord stage.\n");
            break;
        } else {
            printf("Invalid input. Please try again.\n");
        }
    }
    
    return 0;
}
