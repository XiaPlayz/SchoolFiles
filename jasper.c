#include <stdio.h>
#include <stdlib.h>

int main() {
    char givenname[20], lastname[20];
    char age_input[10];
    int age = 0;

    printf("Enter your given name:\t");
    scanf("%s", givenname);
    printf("Enter your last name:\t");
    scanf("%s", lastname);
    
    while (1) {
        printf("Please enter your age:\t");
        scanf("%s", age_input);
        
        age = atoi(age_input);
        
        if (age == 0 && age_input[0] != '0') {
            printf("Invalid answer. Please try again.\n");
            continue;
        }
        
        if (age >= 18) {
            printf("Congrats %s! You are an adult.\n", givenname);
        } else if (age < 18 && age >= 0) {
            printf("Ohh %s, You're still a child.\n", givenname);
        } else {
            printf("Invalid input. Please try again.\n");
            continue;
        }
        
        break;
    }

    return 0;
}
