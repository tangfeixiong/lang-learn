
#include <stdio.h>
#include <stdlib.h>

#include "qsort.h"

int lomuto_partition(int a[], int low, int high);
void lomuto_quicksort(int a[], int low, int high);

int main(void) {
    int v = 0;

    int a[N], i;

    printf("Enter %d numbers to be sorted: ", N);
    for(i = 0; i < N; i++)
        scanf("%d", &a[i]);

    if (v)
        lomuto_quicksort(a, 0, N - 1); // Lomuto partition scheme
    else
        quicksort(a, &a[0], &a[N-1]);

    printf("In sorted order: ");
    for (i = 0; i < N; i++)
        printf("%d ", a[i]);

    printf("\n");

    return 0;
    
}


void lomuto_quicksort(int a[], int low, int high){

    int partition;

    if (low >= high)
        return;

    partition = lomuto_partition(a, low, high);
    lomuto_quicksort(a, low, partition - 1);
    lomuto_quicksort(a, partition + 1, high);
}

int lomuto_partition(int a[], int low, int high){

    int pivot = a[high];

    int i = low;
    int v;
    for(int j = low; j < high; j++){
        if (a[j] < pivot) {
            v = a[i];
            a[i] = a[j];
            a[j] = v;
            i++;
        }
    }
    a[high] = a[i];
    a[i] = pivot;
    
    for (int j = 0; j < N; j++)
        printf("%d ", a[j]);
    printf("\n");

    return i;
}