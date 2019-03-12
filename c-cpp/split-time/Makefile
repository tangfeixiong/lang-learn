
CC=gcc
CFLAGS=-I. -Wall
DEPS = simpletime.h
OBJ = seconds.o splitseconds.o 
BIN = splitseconds

INCDIR =../include
ODIR=.

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

$(BIN): $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ $(OBJ) $(BIN) *.out 
