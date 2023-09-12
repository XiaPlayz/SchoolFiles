int main() {
    int count;
    printf("Let's Count From one to?: ");
    scanf("%d", &count);

    for (int i = 1; i <= count; i++) {
        printf("The value of count is %d\n", i);
        
        sleep(1);
    }
    
    return 0;
}
