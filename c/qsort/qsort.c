#include <stdio.h>
#include <stdlib.h>

#include "qsort.h"

int* partition(int a[], int* lowele, int* highele);

void quicksort(int a[], int* lowele, int* highele) {

    int* middle;

    if (lowele >= highele)
        return;

    middle = partition(a, lowele, highele);
    quicksort(a, lowele, middle - 1);
    quicksort(a, middle + 1, highele);
}

int* partition(int a[], int* lowele, int* highele) {

    int* lo = lowele;
    int* hi = highele;
    int pivot = *hi;
    // int pivot = *lo;
    
    for (int i = 0; i < N; i++)
        printf("%p ", a+i);
    printf("---- lo: %p hi: %p pivot: %d\n", lo, hi, pivot);

    for(;;) {
        while (lo < hi && *lo <= pivot)
            lo += 1;
printf("--> lo: %p (%d) hi: %p (%d)\n", lo, *lo, hi, *hi);
        if (lo >= hi)
            break;

        // a[high--] = a[low];
        *hi = *lo;
        hi -= 1; 

        while (lo < hi && pivot <= *hi)
            hi -= 1;
printf("<-- lo: %p (%d) hi: %p (%d)\n", lo, *lo, hi, *hi);
        if (lo >= hi)
            break;

        // a[low++] = a[high];
        *lo = *hi;
        lo += 1;

    }
    
    *lo = pivot;
    // *hi = pivot;
    
    for (int i = 0; i < N; i++)
        printf("%d ", *(a+i));
    printf(" lo=hi= %p (%d)\n\n", lo, *hi);
    
    return lo;
    // return hi;
}

