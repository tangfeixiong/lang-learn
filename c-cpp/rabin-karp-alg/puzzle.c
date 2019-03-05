
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "puzzle.h"

#define SIZE 10


// Grid node of Rabin Karp hash
// Fields:
// - l: 2D hash array calculated into horizontal right
// - r: horizontal left
// - t: vertical down
// - b: vertical up
// - tl: top left to bottom right diagonal
// - br: bottom right to top left diagonal
// - bl: bottom left to top right
// - tr: top right to bottom left
struct rabinkarphash {
    int left;
    int right;
    int top;
    int bottom;
    int topleft;
    int bottomright;
    int bottomleft;
    int topright;    
};

// Cached Rabin Karp hash by prime
// Fields:
// - p: prime
// - rkhash: 8 direction hash values calculated into grid
struct hashgrid {
    int p;
    struct rabinkarphash** rkhash;
};

// Cached Rabin Karp hash by searched word length
// Fields:
// - x: word length
// - struct rabinkarphash2d: 2nd level cache by prime
struct item2d {
	int x;
	struct hashgrid* grid[SIZE];
};

struct item2d* cache2D[SIZE];

// inspired by 
// - https://stackoverflow.com/questions/101439/the-most-efficient-way-to-implement-an-integer-based-power-function-powint-int
int ipow(int base, int exp)
{
    int result = 1;
    for (;;)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        if (!exp)
            break;
        base *= base;
    }

    return result;
}

// Calculate Rabin-Karp hash
// parameters:
// - l: length of buf, also length of returned hash array
// - hash: calculated hash array, 1st dimension is calculated from left to right, 2nd is vise versa
// - buf: char sequence to calculate
// - p: prime number
// - x: word len
// return:
// - if succeeded, point to hash array. or NULL when existing internal error.
int** calculateRabinKarpHash(int l, int hash[2][PUZZLE_SIZE_MAX], char buf[], int p, int x) {
	int i, j;

    // printf("%d, %p, %p, %s, %d, %d\n", l, hash[0], hash[1], buf, p, x );
        
	for (i = 0; i < l; i++) {
		hash[0][i] = 0;
        hash[1][l-1-i] = 0;
		if (i + x <= l) {
		    if (i == 0)
			    for (j = 0; j < x; j++) {
				    hash[0][i] = hash[0][i] * p + (int)*(buf+i+j);
                    hash[1][l-1-i] = hash[1][l-1-i] * p + (int)*(buf+l-1-i-j);
                }
            else {
		        hash[0][i] = (hash[0][i-1] - (int)*(buf+i-1) * ipow(p, x-1)) * p + (int)*(buf+i-1+x);
                hash[1][l-1-i] = (hash[1][l-i] - (int)*(buf+l-i) * ipow(p, x-1)) * p + (int)*(buf+l-i-x);
            }
        }
	}
    
	return (int**)hash;
}

struct matchedinfo* searchword2d(struct matchedinfo* result, int rows, int cols, char puzzle2d[PUZZLE_SIZE_MAX][PUZZLE_SIZE_MAX], int x, char* word, int p) {
	int ha[2][PUZZLE_SIZE_MAX];
    char buf[PUZZLE_SIZE_MAX];
    int i, j;
    int s;
    
    if (rows == 0 || cols == 0 || rows != cols)
        return NULL;
    s = rows;
    if (x == 0 || word == NULL || p <= 1)
        return NULL;
    
    int xindex = x % SIZE;
    struct item2d *item = NULL;
    int pindex = p % SIZE;
    struct hashgrid *grid = NULL;
    
    if (cache2D[xindex] != NULL && cache2D[xindex]->x == x)
            item = cache2D[xindex];
    if (item == NULL) {
        item = (struct item2d*) malloc(sizeof(struct item2d));
        item->x = x;
        cache2D[xindex] = item;
    } else
        grid = item->grid[pindex];
            
    if (grid == NULL || grid->p != p) {
        grid = (struct hashgrid*) malloc(sizeof(struct hashgrid));
        grid->p = p;
        item->grid[pindex] = grid;       
    
        grid->rkhash = (struct rabinkarphash **)malloc(rows * sizeof(struct rabinkarphash *)); 
        for (i=0; i<rows; i++) 
            grid->rkhash[i] = (struct rabinkarphash *)malloc(cols * sizeof(struct rabinkarphash)); 
    
        
        // calculate both of left and right
        for (i = 0; i < rows; i++) {
            for (j = 0; j < cols; j++) {
                buf[j] = puzzle2d[i][j];
                ha[0][j] = 0;
                ha[1][j] = 0;
            }
            buf[j] = '\0';
            calculateRabinKarpHash(cols, ha, buf, p, x);
            for (j = 0; j < cols; j++) {
                grid->rkhash[i][j].left = ha[0][j];
                grid->rkhash[i][j].right = ha[1][j];
            }
        }
                        
        // calculate both of top-left and bottom-right
        // half of right up
        for (j = 0; j < s; j++) {
            for (i = 0; i < s-j; i++) {
                buf[i] = puzzle2d[i][i+j];
                ha[0][i] = 0;
                ha[1][i] = 0;
            }
            calculateRabinKarpHash(s-j, ha, buf, p, x);
            for (i = 0; i < s-j; i++) {
                grid->rkhash[i][i+j].topleft = ha[0][i];
                grid->rkhash[i][i+j].bottomright = ha[1][i];
            }
        }
        // half of left down
        for (i = 1; i < s; i++) {
            for (j = 0; j < s-i; j++) {
                buf[j] = puzzle2d[i+j][j];
                ha[0][j] = 0;
                ha[1][j] = 0;
            }
            calculateRabinKarpHash(s-i, ha, buf, p, x);
            for (j = 0; j < s-i; j++) {
                grid->rkhash[i+j][j].topleft = ha[0][j];
                grid->rkhash[i+j][j].bottomright = ha[1][j];
            }
        }
        
        // calculate both of bottom-left and top-right
        // half of right down
        for (j = 0; j < s; j++) {
            for (i = 0; i < s-j; i++) {
                buf[i] = puzzle2d[s-1-i][i+j];
                ha[0][i] = 0;
                ha[1][i] = 0;
            }
            calculateRabinKarpHash(s-j, ha, buf, p, x);
            for (i = 0; i < s-j; i++) {
                grid->rkhash[s-1-i][j].bottomleft = ha[0][i];
                grid->rkhash[s-1-i][j].topright = ha[1][i];
            }
        }
        // half of left up        
        for (i = 1; i < s; i++) {
            for (j = 0; j < s-i; j++) {
                buf[j] = puzzle2d[s-1-(i+j)][j];
                ha[0][j] = 0;
                ha[1][j] = 0;
            }
            calculateRabinKarpHash(s-i, ha, buf, p, x);
            for (j = 0; j < s-i; j++) {
                grid->rkhash[s-1-(i+j)][j].bottomleft = ha[0][j];
                grid->rkhash[s-1-(i+j)][j].topright = ha[1][j];
            }
        }
        
        // calculate both of top and bottom
        for (j = 0; j < cols; j++) {
            for (i = 0; i< rows; i++) {
                buf[i] = puzzle2d[i][j];
                ha[0][i] = 0;
                ha[1][i] = 0;
            }
            calculateRabinKarpHash(rows, ha, buf, p, x);
            for (i = 0; i < rows; i++) {
                grid->rkhash[i][j].top = ha[0][i];
                grid->rkhash[i][j].bottom = ha[1][i];
            }
        }
    }
    
    // hash of word
    calculateRabinKarpHash(x, ha, word, p, x);
    result->word = (char *)malloc(x * sizeof(char) + 1);
    *(result->word+x) = '\0';
    memcpy(result->word, word, x);
    result->hash = ha[0][0];
    
    // searching
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            if (result->hash == grid->rkhash[i][j].left)
                result->direction = 1;
            else if (result->hash == grid->rkhash[i][j].right)
                result->direction = 2;
            else if (result->hash == grid->rkhash[i][j].top)
                result->direction = 3;
            else if (result->hash == grid->rkhash[i][j].bottom)
                result->direction = 4;
            else if (result->hash == grid->rkhash[i][j].topleft)
                result->direction = 5;
            else if (result->hash == grid->rkhash[i][j].bottomright)
                result->direction = 6;
            else if (result->hash == grid->rkhash[i][j].bottomleft)
                result->direction = 7;
            else if (result->hash == grid->rkhash[i][j].topright)
                result->direction = 8;
            else {
                result->matched = 0;
                result->row = 0;
                result->column = 0;
                result->direction = 0;
            }
            if (result->direction > 0) {
                result->matched++;
                result->row = i;
                result->column = j;
                return result;
            }
        }
    }
    
    return result;
}
