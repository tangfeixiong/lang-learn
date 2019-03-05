
#define PUZZLE_SIZE_MAX 200
#define WORD_LEN_MAX 100
#define PRIME_NUM 101

struct matchedinfo {
    char* word;
	int hash;
	int matched;
	int row;
	int column;
	int direction;
};

extern struct matchedinfo* searchword2d(struct matchedinfo* result, 
        int rows, int cols, char puzzle[PUZZLE_SIZE_MAX][PUZZLE_SIZE_MAX], int wordlen, char* word, int prime);