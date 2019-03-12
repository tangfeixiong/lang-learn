#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmpfunc(const void *a, const void *b) {
    return strcmp((char *)a, (char *)b);
}

int main(void) {
    char words[20][20];
    int count = 0;
    
    do {
        printf("Enter word: ");
        // scanf("%s", words[count]);
        fgets(words[count], 20, stdin);
        char* pos = strchr(words[count], '\n');
        if (pos != NULL) *pos = '\0';
        count++;
    } while (words[count-1][0] != '\0');
    
    qsort(words, count, 20, cmpfunc);
    
    printf("In sorted order:");
    for (int i = 0; i < count; i++) {
        printf(" %s", words[i]);
    }
    printf("\n");
}