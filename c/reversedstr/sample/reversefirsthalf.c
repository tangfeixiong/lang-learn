
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// #include <unistd.h>
#include <getopt.h>

#include "../source/mylibstr.h"

char* reverseFirstHalfOfString(char src[]);

int main(int argc, char* argv[]) {
  int aflag = 0;
  int bflag = 0;
  char *cvalue = NULL;
  int index;
  int c;

  opterr = 0;

  while ((c = getopt (argc, argv, "abc:")) != -1)
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
      case '?':
        if (optopt == 'c')
          fprintf (stderr, "Option -%c requires an argument.\n", optopt);
        else if (isprint (optopt))
          fprintf (stderr, "Unknown option `-%c'.\n", optopt);
        else
          fprintf (stderr,
                   "Unknown option character `\\x%x'.\n",
                   optopt);
        return 1;
      default:
        abort ();
      }

  printf ("aflag = %d, bflag = %d, cvalue = %s\n",
          aflag, bflag, cvalue);

  for (index = optind; index < argc; index++)
    // printf ("Non-option argument %s\n", argv[index]);
	fprintf(stdout, "%s\n", reverseFirstHalfOfString(argv[index]));
  return 0;
}

char* reverseFirstHalfOfString(char src[]) {
	char* dst;
	int len;
	
	len = strlen(src);
	dst = reversedSubstring(src, 0, len/2);
	
	return dst;
}