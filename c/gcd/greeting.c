

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    
#if defined (ENGLISH)
    printf("Insert disk 1\n");
#elif defined (FRENCH)
    printf("Inserez Le Disque 1\n");
#elif defined (SPANISH)
    printf("Inserte El Disco 1\n");
#else
    printf("no language defined.\n");
#endif

    return 0;
}