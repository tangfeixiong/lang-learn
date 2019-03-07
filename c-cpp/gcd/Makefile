
CC=gcc
CFLAGS=-I. -Wall -std=c99
DEPS = gcd.h
OBJ = gcd.o testcase.o

INCDIR =../include
ODIR=.

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

test: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)
	./$@

.PHONY: clean test

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ a.out $(OBJ)
