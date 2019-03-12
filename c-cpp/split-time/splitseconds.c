
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include "simpletime.h"

char* split_time(char src[]);

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

  for (index = optind; index < argc; index++) {
    printf ("Non-option argument %s\n", argv[index]);
	fprintf(stdout, "%s\n", split_time(argv[index]));
    if (aflag) {
        time t = secondstohms(atoi(argv[index]));
        printf("times=%d:%d:%d\n", t.hours, t.minutes, t.seconds);
    }
  }
  return 0;
}

char t[80];

char* split_time(char src[]) {
	int len;
	int num;
	int ds, hs, ms, ss;
	
	len = strlen(src);
	if (len == 0) {
		t[0] = 0;
	    return t;
	}
	num = atoi(src);
	secondstotime(num, &ds, &hs, &ms, &ss );
	
	if (ds > 0) printf("days = %d\n", ds);
	
	sprintf(t, "times=%d:%d:%d", hs, ms, ss);
	
	return t;
}