
CC=gcc
CFLAGS=-I. -Wall -std=c99
DEPS = palindrome.h
OBJ = palindrome.o demo.o

INCDIR =../include
ODIR=.

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

demo: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

.PHONY: clean test

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ $(OBJ) *.o *.out

test: palindrome.o
	rm -f testcase
	gcc -o testcase $^ testcase.c $(CFLAGS)
	./testcase