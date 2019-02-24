#include <stdio.h>
#include <stdlib.h>

void main(int argc, char* argv[]) {
    int rows = 3;
    int cols = 3;
    int i, j;
    
    if (argc > 1) {
        int v = atoi(argv[1]);
        if (v > 3) {
            rows = v;
            cols = v;
        }
    }
    
    for (j = 0; j < cols; j++) {
        for (i = 0; i < rows-j; i++) {
            printf("(%d, %d); ", i, i+j);
        }
        printf("\n");
    }

        
    for (i = 1; i < rows; i++) {
        for (j = 0; j < cols-i; j++) {
            printf("(%d, %d); ", i+j, j);
        }
        printf("\n");
    }

}