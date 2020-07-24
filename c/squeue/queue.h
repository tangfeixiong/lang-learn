#include <stdbool.h>

/*
typedef int bool;
#define true 1
#define false 0
*/

struct Node;

typedef struct{
 struct Node* first;
 struct Node* last;
} Squeue;

void initSqueue (Squeue **squeue);
bool isEmpty (const Squeue *squeue);
void addFront (Squeue *squeue, char *val);
void addBack (Squeue *squeue, char *val);
void leaveFront (Squeue *squeue);
void leaveBack (Squeue *squeue);
char* peekFront (const Squeue * squeue);
char* peekBack (const Squeue *squeue);
void print (const Squeue * squeue, char direction);
void nuke (Squeue * squeue);
void mergeFront(Squeue* squeue, char direction);
void mergeBack(Squeue* squeue, char direction);
void reverse(Squeue* squeue);
void destroySqueue(Squeue **squeue);