#include <stdio.h>
#include <string.h>

#define MAX_SIZE 20

int get_extension(const char *file_name);

int main(int argc, char* argv[]){
	
	//simplifying things and not doing any argument validation
    printf("The index value of the extension of the input file is: %d\n", get_extension(argv[1]));
}

int get_extension(const char *file_name) {
    static char* ext[] = {
        ".txt", ".out", ".bkp", ".dot", ".tx"
    };
    
    char name[MAX_SIZE + 1];
        
    strcpy(name, file_name);
    
    for (int i = 0; i < 5; i++) {
        int l = strlen(ext[i]);
        char* substr = name + strlen(name) - l;
        printf("%s %d %s\n", ext[i], l, substr);
        if (strcmp(ext[i], substr) == 0)
            return i;
    }
    return -1;
}
