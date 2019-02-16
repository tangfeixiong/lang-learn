
CC=gcc
CFLAGS=-I. -Wall
DEPS = simpletime.h
OBJ = seconds.o splitseconds.o 

INCDIR =../include
ODIR=.

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

splitseconds: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ 
