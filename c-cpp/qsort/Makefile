
CC=gcc
CFLAGS=-I. -Wall -std=c99
DEPS = qsort.h
OBJ = qsort.o quicksort.o
BIN = quicksort

INCDIR =../include
ODIR=.

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

$(BIN): $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

.PHONY: clean $(BIN)

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ $(OBJ) *.out $(BIN)
