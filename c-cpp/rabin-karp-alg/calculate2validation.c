
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

char puzzle[5][5]={
{'a', 'h', 'e', 'l', 'w'},
{'h', 'e', 'l', 'l', 'o'},
{'g', 'b', 'l', 'f', 'k'},
{'c', 'i', 'k', 'm', 'l'},
{'j', 'd', 'g', 'o', 'd'}    
};

char word[4][3] = {
{'w', 'o', 'k'},
{'d', 'o', 'g'},
{'b', 'a', 't'}, 
{'e', 'l', 'k'} 
};

int main(int argc, char* argv[]) {
    int p = 101;
    int x = 3;
    int i, j, k, l;
    long h;
    int direction = -1;
    long hash[5][5];
    char line[5];
    int rows = 5, cols = 5; 
    
    if (argc > 1) {
        int v = atoi(argv[1]);
        if (v > 0 && v <= 8) {
            direction = v;
        } else {
            printf("Usage: %s [direction]\n", argv[0]);
            printf("\tdirection value is number ranged 1|2|3|4|5|6|7|8\n");
            return 1;
        }
    }
    
    if (direction == 1 || direction == -1) {
        printf("calculate from left to right:\n");
        for (i=0; i<5; i++) {
            h = 0;
            for (j=0; j<5; j++) {
                if (j<=5-3) {
                    if (j == 0 && h == 0) {                    
                        h += (int)puzzle[i][j] * p * p + (int)puzzle[i][j+1] * p + (int)puzzle[i][j+2];
                    } else {
                        h = (h - (int)puzzle[i][j-1] * p * p) * p + (int)puzzle[i][j+2];
                    }
                } else 
                    h = 0;
                printf("(%d, %d, %ld); ", i, j, h);
            }
            printf("\n");
        }
        
        printf("--- x variable\n");
        for (i=0; i<5; i++) {
            h = 0;
            for (j=0; j<5; j++) {
                if (j+x<=5) {
                    if (j == 0 && h == 0) {
                        for (k = 0; k < x; k++)
                            h += (int)puzzle[i][j+k] * pow(p, x-1-k);
                    } else {
                        h = (h - (int)puzzle[i][j-1] * pow(p, x-1)) * p + (int)puzzle[i][j+x-1];
                    }
                } else 
                    h = 0;
                printf("(%d, %d, %ld); ", i, j, h);
            }
            printf("\n");
        }
    }
     
    if (direction == 2 || direction == -1) {   
        printf("calculate from right to left:\n");
        for (i=0; i<5; i++) {
            h = 0;
            for (j=0; j<5; j++) {
                if (j<=5-3) {
                    if (j == 0 && h == 0) {                    
                        h += (int)puzzle[i][4-j] * p * p + (int)puzzle[i][4-(j+1)] * p + (int)puzzle[i][4-(j+2)];
                    } else {
                        h = (h - (int)puzzle[i][4-(j-1)] * p * p) * p + (int)puzzle[i][4-(j+2)];
                    }
                } else 
                    h = 0;
                printf("(%d, %d, %ld); ", i, 4-j, h);
            }
            printf("\n");
        }
        
        printf("--- x variable, store calculation then output\n");
        for (i=0; i<5; i++) {
            h = 0;
            for (j=0; j<5; j++) {
                if (j+x<=5) {
                    if (j == 0 && h == 0) {
                        for (k = 0; k < x; k++)
                            h += (int)puzzle[i][4-(j+k)] * pow(p, x-1-k);
                    } else {
                        h = (h - (int)puzzle[i][4-(j-1)] * pow(p, x-1)) * p + (int)puzzle[i][4-(j+x-1)];
                    }
                } else 
                    h = 0;
                hash[i][4-j] = h;
            }
        }
        
        for (i=0; i<5; i++) {
            for (j=0; j<5; j++)
                printf("(%d, %d, %ld); ", i, j, hash[i][j]);
            printf("\n");
        }
    }
    
    // to see topleft.c
    if (direction == 5 || direction == -1) {    
        printf("calculate from top left to bottom right:\n");
        for (j = 0; j < cols; j++) {
            for (i = 0; i < rows-j; i++) {
                // printf("(%d, %d); ", i, i+j);
                line[i] = puzzle[i][i+j];
            }
            // printf("\n");

            h = 0;
            for (l=0; l<i; l++) {
                if (l+x<=i) {
                    if (l == 0 && h == 0) {
                        for (k = 0; k < x; k++)
                            h += (int)line[l+k] * pow(p, x-1-k);
                    } else {
                        h = (h - (int)line[l-1] * pow(p, x-1)) * p + (int)line[l+x-1];
                    }
                } else 
                    h = 0;
                // printf("(%d, %d, %ld); ", i, j, h);
                hash[l][l+j] = h;
            }
            // printf("\n");                   
        }
        
        for (i = 1; i < rows; i++) {
            for (j = 0; j < cols-i; j++) {
                // printf("(%d, %d); ", i+j, j);
                line[j] = puzzle[i+j][j];
            }
            // printf("\n");

            h = 0;
            for (l=0; l<j; l++) {
                if (l+x<=j) {
                    if (l == 0 && h == 0) {
                        for (k = 0; k < x; k++)
                            h += (int)line[l+k] * pow(p, x-1-k);
                    } else {
                        h = (h - (int)line[l-1] * pow(p, x-1)) * p + (int)line[l+x-1];
                    }
                } else 
                    h = 0;
                // printf("(%d, %d, %ld); ", i, j, h);
                hash[i+l][l] = h;
            }
            // printf("\n");                   
        }
        
        for (i=0; i<5; i++) {
            for (j=0; j<5; j++)
                printf("(%d, %d, %ld); ", i, j, hash[i][j]);
            printf("\n");
        }        
    }
    
    if (direction == 6 || direction == -1) {
        printf("calculate from bottom right to top left:\n");
        for (j = 0; j < cols; j++) {
            for (i = 0; i < 5; i++) line[i] = '\0';        
            for (i = 0; i < rows-j; i++) {
                // printf("(%d, %d); ", i, i+j);
                line[i] = puzzle[i][i+j];
            }
            // printf("\n");

            l = i;
            h = 0;
            for (i = l - 1; i >= 0; i--) {
                if (i + 1 >= x) {
                    if (i == l - 1 && h == 0) {
                        for (k = 0; k < x; k++)
                            h = h * p + (int)line[i-k];
                    } else {
                        h = (h - (int)line[i+1] * pow(p, x-1)) * p + (int)line[i-x+1];
                    }
                } else 
                    h = 0;
                hash[i][i+j] = h;
            }
        }

        for (i = 1; i < rows; i++) {
            for (j = 0; j < 5; j++) line[j] = '\0';
            for (j = 0; j < cols-i; j++) {
                // printf("(%d, %d); ", i+j, j);
                line[j] = puzzle[i+j][j];
            }
            // printf("\n");

            l = j;
            h = 0;
            for (j = l - 1; j >= 0; j--) {
                if (j+1 >= x) {
                    if (j == l - 1 && h == 0) {
                        for (k = 0; k < x; k++)
                            h = h * p + (int)line[j-k];
                    } else {
                        h = (h - (int)line[j+1] * pow(p, x-1)) * p + (int)line[j-x+1];
                    }
                } else 
                    h = 0;
                // printf("(%d, %d, %ld); ", i, j, h);
                hash[i+j][j] = h;
            }
            // printf("\n");                   
        }
        
        for (i=0; i<5; i++) {
            for (j=0; j<5; j++)
                printf("(%d, %d, %ld); ", i, j, hash[i][j]);
            printf("\n");
        }        
    }
    
    // to see bottomleft.c
    if (direction == 7 || direction == -1) {
        printf("calculate from bottom left to top right:\n");
        for (j = 0; j < cols; j++) {
            for (i = 0; i < 5; i++) line[i] = '\0';
            for (i = 0; i < rows-j; i++) {
                // printf("(%d, %d); ", rows-1-i, i+j);
                line[i] = puzzle[rows-1-i][i+j];
            }
            // printf("\n");
            
            l = rows - j;
            h = 0;
            for (i = 0; i < l; i++) {
                if (i + x <= l) {
                    if (i == 0 && h == 0)
                        for (k = 0; k < x; k++)
                            h = h * p + (int)line[i+k];
                   else
                        h = (h - (int)line[i-1] * pow(p, x-1)) * p + (int)line[i+x-1];
                } else 
                    h = 0;
                hash[rows-1-i][i+j] = h;
            }
        }
    
            
        for (i = 1; i < rows; i++) {
            for (j = 0; j < 5; j++) line[j] = '\0';
            for (j = 0; j < cols-i; j++) {
                // printf("(%d, %d); ", rows-1-(i+j), j);
                line[j] = puzzle[rows-1-(i+j)][j];
            }
            // printf("\n");

            l = cols-i;
            h = 0;
            for (j = 0; j < l; j++) {
                if (j + x <= l) {
                    if (j == 0 && h == 0)
                        for (k = 0; k < x; k++)
                            h = h * p + (int)line[j-k];
                   else
                        h = (h - (int)line[j+1] * pow(p, x-1)) * p + (int)line[j+x-1];
                } else 
                    h = 0;
                hash[rows-1-(i+j)][j] = h;
            }
        }
        
        for (i=0; i<rows; i++) {
            for (j=0; j<cols; j++)
                printf("(%d, %d, %ld); ", i, j, hash[i][j]);
            printf("\n");
        }        
    }       
       
    
    if (direction == 8 || direction == -1) {
        printf("calculate from top right to bottom left:\n");
        for (j = 0; j < cols; j++) {
            for (i = 0; i < 5; i++) line[i] = '\0';
            for (i = 0; i < rows-j; i++) {
                // printf("(%d, %d); ", rows-1-i, i+j);
                line[i] = puzzle[rows-1-i][i+j];
            }
            // printf("\n");
            
            l = rows - j;
            h = 0;
            for (i = l - 1; i >= 0; i--) {
                if (i + 1 >= x) {
                    if (i == l - 1 && h == 0)
                        for (k = 0; k < x; k++)
                            h = h * p + (int)line[i-k];
                   else
                        h = (h - (int)line[i+1] * pow(p, x-1)) * p + (int)line[i-x+1];
                } else 
                    h = 0;
                hash[rows-1-i][i+j] = h;
            }
        }
    
            
        for (i = 1; i < rows; i++) {
            for (j = 0; j < 5; j++) line[j] = '\0';
            for (j = 0; j < cols-i; j++) {
                // printf("(%d, %d); ", rows-1-(i+j), j);
                line[j] = puzzle[rows-1-(i+j)][j];
            }
            // printf("\n");

            l = cols-i;
            h = 0;
            for (j = l - 1; j >= 0; j--) {
                if (j + 1 >= x) {
                    if (j == l - 1 && h == 0)
                        for (k = 0; k < x; k++)
                            h = h * p + (int)line[j-k];
                   else
                        h = (h - (int)line[j+1] * pow(p, x-1)) * p + (int)line[j-x+1];
                } else 
                    h = 0;
                hash[rows-1-(i+j)][j] = h;
            }
        }
        
        for (i=0; i<rows; i++) {
            for (j=0; j<cols; j++)
                printf("(%d, %d, %ld); ", i, j, hash[i][j]);
            printf("\n");
        }        
    }       
    
    if (direction == 3 || direction == -1) {
        printf("calculate from top to bottom:\n");
        for (j = 0; j < cols; j++) {
            h = 0;
            for (i = 0; i < rows; i++) {
                if (i + x <= rows) {
                    if (i == 0 && h == 0)
                        for (k = 0; k < x; k++)
                            h = h * p + (int)puzzle[i+k][j];
                   else
                        h = (h - (int)puzzle[i-1][j] * pow(p, x-1)) * p + (int)puzzle[i+x-1][j];
                } else 
                    h = 0;
                hash[i][j] = h;
            }
        }
        
        
        for (i=0; i<rows; i++) {
            for (j=0; j<cols; j++)
                printf("(%d, %d, %ld); ", i, j, hash[i][j]);
            printf("\n");
        }        
    }

    
    if (direction == 4 || direction == -1) {
        printf("calculate from bottom to top:\n");
        for (j = 0; j < cols; j++) {
            h = 0;
            for (i = rows - 1; i >= 0; i--) {
                if (i + 1 >= x) {
                    if (i == rows-1 && h == 0)
                        for (k = 0; k < x; k++)
                            h = h * p + (int)puzzle[i-k][j];
                   else
                        h = (h - (int)puzzle[i+1][j] * pow(p, x-1)) * p + (int)puzzle[i-x+1][j];
                } else 
                    h = 0;
                hash[i][j] = h;
            }
        }
                
        for (i=0; i<rows; i++) {
            for (j=0; j<cols; j++)
                printf("(%d, %d, %ld); ", i, j, hash[i][j]);
            printf("\n");
        }        
    }
    
}