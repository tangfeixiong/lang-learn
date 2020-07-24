
CC=gcc
CFLAGS=-I. -Wall -std=c99
DEPS = puzzle.h
OBJ = puzzle.o rksearch.o 

INCDIR =.
ODIR=.

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

.PHONY: bin

bin: $(OBJ)
	$(CC) -o rksearch $^ $(CFLAGS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ topleft bottomleft calculategrid calc2validation output.txt
	
.PHONY: test
test:
	gcc -o topleft topleft.c
	gcc -o bottomleft bottomleft.c
	gcc calculategrid.c -lm -o calculategrid
	gcc calc2validation.c -lm -o calc2validation
