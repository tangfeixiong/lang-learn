
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <limits.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>

// Inspired by
// - https://stackoverflow.com/questions/22575940/getopt-not-included-implicit-declaration-of-function-getopt
// - https://stackoverflow.com/questions/2115867/is-there-a-define-for-c99
#if __STDC_VERSION__ >= 199901L
/* C99 header */
#include <getopt.h>
#endif

#include "puzzle.h"

#define ERR_PUZZLE_NOT_EXISTED 4
#define ERR_WORDLIST_NOT_EXISTED 5
#define ERR_ARGUMENT_REQUIRED 6
#define ERR_ENCOUNTERED 7
#define ERR_UNEXPECTED 7
#define ERR_UNKNOWN 7


void search_puzzle(char* puzzlepath, char* wordlistpath, int wordlen, char* solutionpath);

int main(int argc, char* argv[]) {
  int aflag = 0;
  int bflag = 0;
  char *cvalue = NULL;
  char *puzzlefilepath = NULL;
  char *wordlistfilepath = NULL;
  char *solutionfilepath = NULL;
  char *endptr, *str;
  int wordlength = 0;
  int index;
  int c;

  opterr = 0;

  while ((c = getopt (argc, argv, "abc:p:l:w:o:")) != -1)
    switch (c)
      {
      case 'a':
        aflag = 1;
        break;
      case 'b':
        bflag = 1;
        break;
      case 'c':
        cvalue = optarg;
        break;
      case 'p':
        puzzlefilepath = optarg;
        break;
      case 'l':
        {
            errno = 0;    /* To distinguish success/failure after call */
            int base = 10;
            str = optarg;
            long val = strtol(str, &endptr, base);

           if ((errno == ERANGE && (val == LONG_MAX || val == LONG_MIN))
                    || (errno != 0 && val == 0)) {
                perror("strtol");
                exit(EXIT_FAILURE);
            }
        
           if (endptr == str) {
                fprintf(stderr, "No digits were found\n");
                exit(EXIT_FAILURE);
            }
            
            if (val > WORD_LEN_MAX || val < 0) {
                fprintf(stderr, "Encountered error\n");
                return ERR_UNEXPECTED;
            }

            wordlength = val;
            break;
        }
      case 'w':
        wordlistfilepath = optarg;
        break;
      case 'o':
        solutionfilepath = optarg;
        break;
      case '?':
        if (optopt == 'c') {
          fprintf (stderr, "Option -%c requires an argument.\n", optopt);
          break;
        } else if (optopt == 'p' || optopt == 'l' || optopt == 'w' || optopt == 'o') {
            fprintf (stderr, "Usage: %s -p <puzzle_file> -l <word_length> -w <wordlist_file> [-o <solution_file>]\n", argv[0]);
            return ERR_ARGUMENT_REQUIRED;
        }
        else if (isprint (optopt)) {
          fprintf (stderr, "Unknown option `-%c'.\n", optopt);
          return ERR_UNEXPECTED;
        }
        else
          fprintf (stderr,
                   "Unknown option character `\\x%x'.\n",
                   optopt);
        // return 1;
        return ERR_UNKNOWN;
      default:
        abort ();
      }

  printf ("aflag = %d, bflag = %d, cvalue = %s\n",
          aflag, bflag, cvalue);

  for (index = optind; index < argc; index++) {
    printf ("Non-option argument %s\n", argv[index]);
  }

  if (wordlength == 0) {
            fprintf (stderr, "Usage: %s -p <puzzle_file> -l <word_length> -w <wordlist_file> [-o <solution_file>]\n", argv[0]);
            return ERR_ARGUMENT_REQUIRED;    
  }

  struct stat buffer;  
 
  if (stat(puzzlefilepath, &buffer) != 0) {
    fprintf (stderr, "Error: Puzzle file %s does not exist\n", puzzlefilepath);
    return ERR_PUZZLE_NOT_EXISTED;
  }

  if (stat(wordlistfilepath, &buffer) != 0) {
    fprintf (stderr, "Error: Wordlist file %s does not exist\n", wordlistfilepath);
    return ERR_WORDLIST_NOT_EXISTED;
  }

  if (solutionfilepath == NULL) {
    solutionfilepath = "output.txt";
    fprintf (stdout, "Will output into default solution file, aka %s\n", solutionfilepath);
  }

  search_puzzle(puzzlefilepath, wordlistfilepath, wordlength, solutionfilepath);
  return 0;
}


void search_puzzle(char* puzzlepath, char* wordlistpath, int wordlen, char* solutionpath) {
    FILE *fp, *fs;
    char str[PUZZLE_SIZE_MAX] = "";
    char *pos;
    int row = 0, col = 0;
    int len;
    char puzzle2d[PUZZLE_SIZE_MAX][PUZZLE_SIZE_MAX];
    char word[WORD_LEN_MAX] = "";

    fp = fopen(puzzlepath , "r");
    if (fp == NULL) {
        perror("Error opening puzzle file");
        exit(ERR_ENCOUNTERED);
    }
    while ( fgets (str, PUZZLE_SIZE_MAX, fp) != NULL ) {
        /* writing content to stdout */
        // puts(str);
        if ((pos = strchr(str, '\n')) != NULL)
            *pos = '\0';
//        else // last line
//            puts(str);
                        
        len = strlen(str);
        if (col == 0) 
            col = len;
        else if (col != len) {
            fprintf(stderr, "Encountered error\n");
            exit(ERR_ENCOUNTERED);            
        }

        memset(puzzle2d[row], 0, PUZZLE_SIZE_MAX);
        strcpy(puzzle2d[row], str);
        
        ++row;
        if (row > col) {
            fprintf(stderr, "Encountered error\n");
            exit(ERR_ENCOUNTERED);                        
        }

        str[0] = '\0';
    }
    fclose(fp);
    
    if (row < col) {
        fprintf(stderr, "Encountered error\n");
        exit(ERR_ENCOUNTERED);                        
    }
//    for (int i=0; i<row; i++)
//        printf("%s\n", puzzle2d[i]);

    fs = fopen(solutionpath, "w+");
    if (fs == NULL) {
        perror("Error creating or opening solution file");
        exit(ERR_ENCOUNTERED);
    }

    fp = fopen(wordlistpath , "r");
    if (fp == NULL) {
        perror("Error opening wordlist file");
        exit(ERR_ENCOUNTERED);
    }
    while ( fgets (word, WORD_LEN_MAX, fp) != NULL ) {
        /* writing content to stdout */
        // puts(word);
        if ((pos = strchr(word, '\n')) != NULL)
            *pos = '\0';
//        else // last line
//            puts(word);
                        
        len = strlen(word);
        if (len == 0) 
            continue;
        if (len != wordlen) {
            fprintf(stderr, "Encountered error\n");
            exit(ERR_ENCOUNTERED);            
        }

        struct matchedinfo* result = (struct matchedinfo*) malloc(sizeof(struct matchedinfo));
        if (searchword2d(result, row, col, (char**)puzzle2d, len, word, PRIME_NUM) == NULL) {
            fprintf(stderr, "Encountered error\n");
            exit(ERR_ENCOUNTERED);
        }
        // printf("%s;(%d,%d);%d;%d\n", word, result->row, result->column, result->direction, result->hash);
        
        int n = fprintf(fs, "%s;(%d,%d);%d\n", word, result->row, result->column, result->direction);
        if (n < 0) {
            fprintf(stderr, "Encountered error\n");
            exit(ERR_ENCOUNTERED);
        }

        free(result);
        memset(word, 0, len);
    }
    fclose(fp);
	fclose(fs);
}