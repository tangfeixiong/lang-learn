#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int isPalindrome(int len, char* msg) {
    char words[100];
    int c, size = 0, offset;
    
    if (len <= 1)
        return 0;
    
    for (int i = 0; i < len; i++) {
        c = (int)*(msg+i);
       while (!((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'))) {
            if (size == 0)
                return 0;
            i++;
            c = (int)*(msg+i);
        }
       for (offset = 1; i + offset < len; offset++) {
            c = (int)*(msg+i+offset);
            if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <='z')) 
                continue;
            else
                break;
        }
        // words[size] = (char*)malloc((offset+1) * sizeof(char));
        memcpy(words+size, msg+i, offset);
        size += offset;
        i += offset;
    }
    for (int i = size; i < 100; i++)
        *(words+i)='\0';
    printf("%s\n", words);
    
    for (int i = 0; i < size/2; i++) {
        int d = (int)*(words+i)-(int)*(words+size-1-i);
        printf("%c, %c, %d\n", *(words+i), *(words+size-1-i), d);
        if (!(d == 0 || d == (d > 0 ? 'a' - 'A' : 'A' - 'a')))
            return 0;
    }
    
    return 1;
}
