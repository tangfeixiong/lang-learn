
#include <stdlib.h>
#include <string.h>

char empty[] = {'\0'};

char* reversedString(char* dest, char orig[]) {
	int len, half;
	int idx = 0;
	char ch;
	
	len = strlen(orig);
	if ( len == 0 ) {
		dest = empty;
	    return empty;
    }
	
	strcpy(dest, orig);
	half = len/2;
	while (idx < half) {
		ch = *(dest+idx);
		dest[idx] = dest[len-1-idx];
		dest[len-1-idx] = ch;
		idx++;
	}
	return dest;
}

char* reversedSubstring(char src[], int start, int num) {
	char* rs;
	char* dst;
	int len;
	
	len = strlen(src);
	
	if ( start >= len || start + num > len ) {
		return NULL;
	}
	
	rs = (char*) malloc(len+1);
	rs[len] = 0;
	reversedString(rs, src);
	if ( rs == empty ) {
	    return rs;
    }
	
	dst = (char*) malloc(num+1);
    memcpy(dst, rs+len-start-num, num);
    dst[num] = 0;
	return dst;
}

