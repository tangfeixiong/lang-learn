#include <stdbool.h>

//struct NodeBucket {
// char** val;
// struct NodeBucket* next;
//};

struct NodeBucket;

typedef struct {
    struct NodeBucket* firstBucket;
    int topElt;
    int bucketSize;
} Stack;

void initStack (int bucketSize, Stack **stack);
bool isEmpty (const Stack *stack);
void push (char* val, Stack *stack);
void pop(Stack *stack);
int size (const Stack *stack);
char* top (const Stack *stack);
void swap (Stack *stack);
void print (const Stack *stack);
void clear(Stack *stack);
void destroyStack(Stack **stack);