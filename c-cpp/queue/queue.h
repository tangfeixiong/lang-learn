
#include <stdbool.h>

/*
typedef int bool;
#define true 1
#define false 0
*/

typedef int* NumericItemP;

struct Node;

typedef struct{
 struct Node* first;
 struct Node* last;
} Queue;

void initQueue (Queue **queue);
void append (Queue *queue, NumericItemP pVal);
void leave (Queue *queue);
NumericItemP seekHead (const Queue *queue);
NumericItemP seekTail (const Queue *queue);
void printAll (const Queue * queue);
bool isEmpty (const Queue * queue);
void clear (Queue * queue);
void destroyQueue(Queue **queue);