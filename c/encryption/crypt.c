
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

FILE *fout;

char mapping[256][2];

void encrypt(char plainText[], int inputLength) {
    if (inputLength <=0 ) {
        fprintf(stderr, "nothing should encrypt\n");
        return;
    }
   
    if (fout == NULL)
        fout = stdout;
    
    char ch;
    char cipherText[inputLength];
    for (int i = 0; i < inputLength; i++) {
        ch = '\0';
        for (int j = 0; j < 256; j++) {
            if (mapping[j][0] == plainText[i] 
                    && ((mapping[j][1] >= 'A' && mapping[j][1] <= 'Z')
                    || (mapping[j][1] >= 'a' && mapping[j][1] <= 'z'))) {
                cipherText[i] = mapping[j][1];
                ch = mapping[j][1];
                break;
            }
        }
        if (!ch) {
            fprintf(stderr, "Failed to encrypt, missing mapping. (%c, %c)\n", plainText[i], ch);
            return;
        }
    }   
    
    for (int i = inputLength - 1; i >= 0; i--)
        fputc(cipherText[i], fout);
    fputc('\n', fout);
}

void decrypt(char cipherText[], int inputLength) {
    if (inputLength <=0 ) {
        fprintf(stderr, "nothing should decrypt\n");
        return;
    }
   
    if (fout == NULL)
        fout = stdout;
    
    char ch;
    char plainText[inputLength];
    for (int i = 0; i < inputLength; i++) {
        ch = '\0';
        for (int j = 0; j < 256; j++) {
            if (mapping[j][1] == cipherText[i] 
                    && ((mapping[j][0] >= 'A' && mapping[j][0] <= 'Z')
                    || (mapping[j][0] >= 'a' && mapping[j][0] <= 'z'))) {
                plainText[inputLength - 1 - i] = mapping[j][0];
                ch = mapping[j][0];
                break;
            }
        }
        if (!ch) {
            fprintf(stderr, "Failed to decrypt, missing mapping. (%c, %c)\n", cipherText[i], ch);
            return;
        }
    }   
    
    for (int i = 0; i < inputLength; i++)
        fputc(plainText[i], fout);
    fputc('\n', fout);
}