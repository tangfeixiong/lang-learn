
CC=gcc
CFLAGS=-I. -Wall -std=c99
DEPS = palindrome.h
OBJ = palindrome.o

INCDIR =../include
ODIR=.

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

palindrome: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

.PHONY: clean test

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ a.out *.o

test: $(OBJ)
	gcc -o testcase $^ testcase.c $(CFLAGS)