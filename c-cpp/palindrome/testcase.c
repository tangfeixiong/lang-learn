#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#include "palindrome.h"

int main(int argc, char** argv) {
    char* tests[8]={
        "He lived as a devil, eh?",
        "Madam, I am Adam.",
        "a!",
        "aA",
        "aA!!!",
        "abA!",
        "a111A",
        "aB  bA"
    };
    
    int result;
    
    for (int i = 0; i < 8; i++) {
        result = isPalindrome(strlen(tests[i]), tests[i]);
        if (result == 0 || result == 1)
            printf("Test passed. The result info is %s\n", result == 0 ? "Not a palindrome" : "Palindrome" );
        else
            printf("Test failed! The result number is %d\n", result);
    }
    
}