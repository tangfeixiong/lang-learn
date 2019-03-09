
CC=gcc
CFLAGS=-I. -Wall -std=c99
DEPS = 
OBJ = crypt.o demo.o 
BIN = demo

INCDIR =.
ODIR=.

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

.PHONY: bin

bin: $(OBJ)
	$(CC) -o $(BIN) $^ $(CFLAGS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ $(OBJ) $(BIN)
