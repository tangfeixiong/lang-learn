#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include "queue.h"

struct Node{
 NumericItemP item;
 struct Node* next;
};

void initQueue (Queue **queue) {
    if (queue == NULL) return;
    
    *queue = (Queue *)malloc(sizeof(Queue));
    (*queue)->first = NULL;
    (*queue)->last = NULL;
}

void append (Queue *queue, NumericItemP pVal) {
    if (queue != NULL) {
        struct Node *node = (struct Node *)malloc(sizeof(struct Node));
        node->next = NULL;
        int s = sizeof(int);
        node->item = (NumericItemP)malloc(s);
        memcpy(node->item, pVal, s);
        
        if (queue->last != NULL) {
            struct Node* q = queue->last;
            q->next = node;
        } else
            queue->first = node;
        
        queue->last = node;
    }    
}

void leave (Queue *queue) {
    assert(!isEmpty(queue));
    
    struct Node *n = queue->first;
    if (n->next != NULL) {
        queue->first = n->next;
        n->next = NULL;
    } else {
        queue->first = NULL;
        queue->last = NULL;
    }
    
    free(n->item);
    free(n);
}

NumericItemP seekHead (const Queue * queue) {
    assert(!isEmpty(queue));

    return queue->first->item;
}

NumericItemP seekTail (const Queue * queue) {
    assert(!isEmpty(queue));

    return queue->last->item;
}

void printAll (const Queue * queue) {
    struct Node *n;

    fprintf(stdout, "queue is:\n");
    n = queue->first;
    while (n != NULL) {
        fprintf(stdout, "\t%d\n", *(n->item));
        n = n->next;
    }
}

bool isEmpty (const Queue *queue) {
    if (queue != NULL && queue->first == NULL && queue->last == NULL)
        return true;
        
    return false;
}

void clear (Queue * queue) {
    if (!isEmpty(queue)) {    
        struct Node *q = queue->first;
        queue->first = NULL;
        queue->last = NULL;
        struct Node *n;
        while (q != NULL) {
            n = q;
            q = n->next;
            n->next = NULL;
            free(n->item);
            free(n);
        }
    }
}

void destroyQueue(Queue **queue) {
    if (queue == NULL) return;
    if (*queue == NULL) return;
    
    clear(*queue);
    free(*queue);
}
