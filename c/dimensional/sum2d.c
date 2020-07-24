#include <stdio.h>

#define LEN 10

int sum_two_dimensional_array(int a[][LEN], int n){
	
	int i, sum = 0;
    int *ptr = (int *)a;
	
	for (i = 0; i < n * LEN; i++) {
            printf("%d ", *(ptr+i));
			sum += *(ptr+i);
    }
    printf("\n");
			
	return sum;
}

int main(){
	int numbers[2][LEN] = {{1,2,3,4,5,6,7,8,9,10},
				{2,3,4,5,6,7,8,9,10,11}};

	printf("The sum of all elements of the array is: %d\n", sum_two_dimensional_array(numbers, 2));

	return 0;
}