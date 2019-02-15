CC=gcc
CFLAGS=-I. -Wall -std=c99
DEPS = source/mylibstr.h
OBJ = sample/reversefirsthalf.o source/reversedstr.o 

.DEFAULT_GOAL := reversefirsthalf

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

reversefirsthalf: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

clean:
	rm -rf source/*.o sample/*.o ./reversefirsthalf
	rm -rf include/ lib/ bin/
	
install: clean reversefirsthalf
	mkdir include
	cp ./source/mylibstr.h include/
	mkdir bin
	cp ./reversefirsthalf bin/
	
.PHONY: bin clean install all