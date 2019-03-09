#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    int amount = 0;
    int d20, d10, d5, d1;
    
    
    printf("Enter a dollar amount: ");
    scanf("%d", &amount);
    
    d20 = amount / 20;
    amount %= 20;
    
    d10 = amount / 10;
    amount %= 10;
    
    d5 = amount / 5;
    amount %= 5;
    
    d1 = amount / 1;
    
    printf("\n$20 bills: %d\n$10 bills: %d\n$5 bills: %d\n$1 bills: %d\n", d20, d10, d5, d1);
    
    return 0;
}