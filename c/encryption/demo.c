#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>


extern void encrypt(char plainText[], int inputLength);
extern void decrypt(char cipherText[], int inputLength);

extern FILE *fout;

extern char mapping[256][2];

void configmapping(char* mappingfilepath);

int main(int argc, char* argv[]) {
    char* mappingfile = NULL;
    char* inputfile = NULL;
    char* cryptopt = NULL;
    int encryptionmode = 0;
    
    for (int i = 1; i < argc; i++) {
        if (*argv[i] == '-' && *(argv[i]+1) == 't' && strlen(argv[i]) == 2) {
            i += 1;
            if (i < argc && *argv[i] != '-')
                mappingfile = argv[i];
        } else if (*argv[i] == '-' && *(argv[i]+1) == 'i' && strlen(argv[i]) == 2) {
            i += 1;
            if (i < argc && *argv[i] != '-')
                inputfile = argv[i];
        } else if (*argv[i] == '-' && *(argv[i]+1) == 'm' && strlen(argv[i]) == 2) {
            i += 1;
            if (i < argc && *argv[i] != '-')
                cryptopt = argv[i];
        } else {
            fprintf(stderr, "Usage: %s -t <mappingfile> -m <encryption mode> -i <inputfile>\n", argv[0]);
            return 7;
        }
    }
    
    if (cryptopt == NULL) {
        fprintf(stderr, "Encryption mode must be specified\n");
        return 7;
    }
    encryptionmode = atoi(cryptopt);
    if (!(encryptionmode == 1 || encryptionmode == 2)) {
        fprintf(stderr,
            "You entered %d. Sorry, your mode must be 1 for encryption or 2 for decryption\n",
            encryptionmode);
        return 6;
    }

    struct stat buffer;  
     
    if (mappingfile == NULL) {
        fprintf(stderr, "Mapping file must be required\n");
        return 7;
    }

    if (stat(mappingfile, &buffer) != 0) {
        fprintf (stderr, "Error: Mapping file %s does not exist\n", mappingfile);
        return 3;
    }
    
    configmapping(mappingfile);
//    for (int i = 0; i < 256; i++) {
//        if (mapping[i][0] == 0 || mapping[i][1] == 0)
//            printf("%d: %d, %d\n", i, mapping[i][0], mapping[i][1]);
//        else 
//            printf("%d: %c, %c\n", i, mapping[i][0], mapping[i][1]);
//    }
    
    if (inputfile == NULL) {
        fprintf(stderr, "Input file must be required\n");
        return 7;
    }

    if (stat(inputfile, &buffer) != 0) {
        fprintf (stderr, "Error: Input word file %s does not exist\n", inputfile);
        return 5;
    }

    fout = stdout;    
    FILE *fin = fopen(inputfile, "r");
    char str[1000] = "";
    char *pos;
    if (fin == NULL) {
        perror("Error opening input file");
        exit(1);
    }
    while ( fgets (str, 1000, fin) != NULL ) {
        /* writing content to stdout */
        // puts(str);
        if ((pos = strchr(str, '\n')) != NULL)
            *pos = '\0';
        if (encryptionmode == 1)
            encrypt(str, strlen(str));
        else
            decrypt(str, strlen(str));        
    }
    fclose(fin);
    
    return 0;
}

void configmapping(char* mappingfilepath) {
    char str[100];
    char *pos;
    char c;
    int n, v;
    
    FILE *fs = fopen(mappingfilepath , "r");
    if (fs == NULL) {
        perror("Error opening mapping file");
        exit(3);
    }
    while ( fgets (str, 100, fs) != NULL ) {
        /* writing content to stdout */
        // puts(str);
        if ((pos = strchr(str, '\n')) != NULL)
            *pos = '\0';
//        else // last line
//            puts(str);
                        
        c = '\0';
        n = -1;
        v = 0;
        for (int i = 0; i < strlen(str); i++) {
            c = *(str + i);
            if (c >= 'A' && c <= 'Z') {
                if (n == -1) n = 26 + c - 'A';
            } else if (c >= 'a' && c <= 'z') {
                if (n == -1) n = c - 'a';
            } else
                continue;

            if (v != 0 && v != 1){
                fprintf(stderr, "Error: The format of mapping file %s is incorrect\n", mappingfilepath);
                exit(4);
            }
            
            if (mapping[n][v]){
                fprintf(stderr, "Error: The format of mapping file %s is incorrect\n", mappingfilepath);
                exit(4);
            }
            
            mapping[n][v] = c;
            v += 1;
        }

        memset(str, '\0', 100);
    }
    fclose(fs);
}