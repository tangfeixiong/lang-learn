#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "palindrome.h"


int main(int argc, char* argv[]) {
    char msg[101]="";
    char* result[] = {"Not a palindrome", "Palindrome"};
    
    printf("Enter a message: ");
    // scanf("%s", msg);
    fgets(msg, 100, stdin);

    int index = isPalindrome(strlen(msg)-1, msg);
    printf("%s\n", result[index]);
}