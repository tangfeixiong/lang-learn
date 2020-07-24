
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#include "gcd.h"

int main(int argc, char** argv) {
    int tests[][2] = {
        { 12, 28 },
        { 48, 16 },
        { 0, 10 },
        { 1, INT_MAX},
        { -1, 10 },
        { INT_MIN, 1}
    };
    
    int l = sizeof(tests) / (sizeof(int) * 2);
    // printf("%d\n", l);
    
    for (int i = 0; i < l; i++) {
        int result = gcd(tests[i][0], tests[i][1]);
        switch (result) {
            case -1:
            case 0:
                printf("Test failed! compute not ready with numbers %d and %d\n", tests[i][0], tests[i][1]);
                break;
            default:
                printf("Test passed. The gcd of %d and %d is %d.\n", tests[i][0], tests[i][1], result);
        }
    }

    printf(">>>Test with no recursive\n");
    
    for (int i = 0; i < l; i++) {
        int result = gcd2(tests[i][0], tests[i][1]);
        switch (result) {
            case -1:
            case 0:
                printf("Test failed! compute not ready with numbers %d and %d\n", tests[i][0], tests[i][1]);
                break;
            default:
                printf("Test passed. The gcd of %d and %d is %d.\n", tests[i][0], tests[i][1], result);
        }
    }
    
}