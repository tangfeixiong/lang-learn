#include <stdio.h>

void print_error( const char *message ) {
	static int n = 1;
	printf("Error %d: %s\n", n++, message);
}

int main() {
	print_error( "Test 1" );
	print_error( "Test 2" );
	print_error( "Test 3" );

	return 0;
}
