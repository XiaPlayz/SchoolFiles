#include <stdio.h>
#include <unistd.h>
#include <ctype.h>

int main() {
    printf("\nTHE PASSING SCORE OF THIS EXAM IS 7!\n");

    char answer;
    int score = 0;
    
    printf("1. How many degrees are in a circle?");
    printf("\nA. 200\nB. 260\nC. 300\nD. 360\nType here your answer: ");
    scanf(" %c", &answer);
    answer = toupper(answer); // Convert input to uppercase
    
    if (answer == 'D') {
        sleep(2);
        score++;
    } else {
        sleep(2);
    }
    
    printf("2. What do you call a group of cells?");
    printf("\nA. Organ\nB. Ecosystem\nC. Tissue\nD. Organism\nType here your answer: ");
    scanf(" %c", &answer);
    answer = toupper(answer); // Convert input to uppercase
    
    if (answer == 'C') {
        sleep(2);
        score++;
    } else {
        sleep(2);
    }
    
    printf("3. What is the chemical symbol for gold?");
    printf("\nA. Go\nB. Au\nC. Ag\nD. Gd\nType here your answer: ");
    scanf(" %c", &answer);
    answer = toupper(answer); // Convert input to uppercase
    
    if (answer == 'B') {
        sleep(2);
        score++;
    } else {
        sleep(2);
    }
    
    printf("4. What is the square root of 16?");
    printf("\nA. 2\nB. 4\nC. 8\nD. 16\nType here your answer: ");
    scanf(" %c", &answer);
    answer = toupper(answer); // Convert input to uppercase
    
    if (answer == 'A') {
        sleep(2);
        score++;
    } else {
        sleep(2);
    }
    
    printf("5. What gas do plants absorb from the atmosphere?");
    printf("\nA. Oxygen\nB. Carbon Dioxide\nC. Hydrogen\nD. Nitrogen\nType here your answer: ");
    scanf(" %c", &answer);
    answer = toupper(answer); // Convert input to uppercase
    
    if (answer == 'B') {
        sleep(2);
        score++;
    } else {
        sleep(2);
    }
    
    printf("6. What is the chemical symbol for water?");
    printf("\nA. H2O\nB. CO2\nC. O2\nD. NaCl\nType here your answer: ");
    scanf(" %c", &answer);
    answer = toupper(answer); // Convert input to uppercase
    
    if (answer == 'A') {
        sleep(2);
        score++;
    } else {
        sleep(2);
    }

    printf("7. How many sides does a triangle have?");
    printf("\nA. 3\nB. 4\nC. 5\nD. 6\nType here your answer: ");
    scanf(" %c", &answer);
    answer = toupper(answer); // Convert input to uppercase
    
    if (answer == 'A') {
        sleep(2);
        score++;
    } else {
        sleep(2);
    }

    printf("8. What is 2 multiplied by 5?");
    printf("\nA. 6\nB. 7\nC. 8\nD. 10\nType here your answer: ");
    scanf(" %c", &answer);
    answer = toupper(answer); // Convert input to uppercase
    
    if (answer == 'D') {
        sleep(2);
        score++;
    } else {
        sleep(2);
    }

    printf("9. Which planet is known as the Red Planet?");
    printf("\nA. Earth\nB. Mars\nC. Jupiter\nD. Saturn\nType here your answer: ");
    scanf(" %c", &answer);
    answer = toupper(answer); // Convert input to uppercase
    
    if (answer == 'B') {
        sleep(2);
        score++;
    } else {
        sleep(2);
    }

    printf("10. How many continents are there on Earth?");
    printf("\nA. 4\nB. 5\nC. 6\nD. 7\nType here your answer: ");
    scanf(" %c", &answer);
    answer = toupper(answer); // Convert input to uppercase
    
    if (answer == 'D') {
        sleep(2);
        score++;
    } else {
        sleep(2);
    }
    printf("Your total score is %d/10\n", score);
	if (score >= 6 ) {
	   printf("Congratulations, You passed the test");
	} else {
	   printf("Ohhh, You failed the test");
	}
	
    return 0;
}