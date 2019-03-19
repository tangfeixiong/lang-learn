#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include "stack.h"

struct NodeBucket {
    char** val;
    struct NodeBucket* next;
};

void initStack (int bucketSize, Stack **stack) {
    if (bucketSize <= 0 || stack == NULL) return;
    
    *stack = (Stack *)malloc(sizeof(Stack));
    (*stack)->firstBucket = NULL;
    (*stack)->topElt = -1;
    (*stack)->bucketSize = bucketSize;
}

bool isEmpty (const Stack *stack) {
    if (stack != NULL && stack->firstBucket == NULL)
        return true;
        
    return false;
}

void push (char* val, Stack *stack) {
    assert( val != NULL);
    assert( stack != NULL);
    
    struct NodeBucket *node;
    char **buf;
    if (stack->firstBucket == NULL || stack->topElt == stack->bucketSize - 1) {
        node = (struct NodeBucket *)malloc(sizeof(struct NodeBucket));
        buf = (char **)calloc(stack->bucketSize, sizeof(char *));
        node->val = buf;
        if (stack->firstBucket != NULL)
            node->next = stack->firstBucket;
        else 
            node->next = NULL;
        stack->firstBucket = node;
        stack->topElt = -1;
    } else {
        node = stack->firstBucket;
        buf = node->val;
    }
    
    int l = strlen(val);
    char *str = (char *)malloc((l+1) * sizeof(char));
    *(str+l) = '\0';
    strcpy(str, val);
    buf[++stack->topElt] = str;
}

void pop(Stack *stack) {
    assert(stack != NULL);
    
    if (stack->firstBucket != NULL) {
        struct NodeBucket *node = stack->firstBucket;
        char **buf = node->val;
        char *str = buf[stack->topElt];
        free(str);
        buf[stack->topElt--] = NULL;
        if (stack->topElt == -1) {
            stack->firstBucket = node->next;
            stack->topElt = stack->bucketSize - 1;
            node->next = NULL;
            free(buf);
            free(node);
        } 
    }
}

int size (const Stack *stack) {
    assert(stack != NULL);
    
    struct NodeBucket *node = stack->firstBucket;
    int c = 0;
    while (node != NULL) {
        node = node->next;
        c++;
    }
    return c * stack->bucketSize + stack->topElt + 1;
}

char* top (const Stack *stack) {
    assert(stack != NULL);
    
    if (stack->firstBucket != NULL) {
        struct NodeBucket *node = stack->firstBucket;
        char **buf = node->val;
        int l = strlen(buf[stack->topElt]);
        
        char *str = (char *)malloc((l+1) * sizeof(char));
        str[l] = '\0';
        strcpy(str, buf[stack->topElt]);

        return str;        
    }
    return NULL;
}

void swap (Stack *stack) {
    assert(stack != NULL);
    assert(size(stack) > 1);
    
    struct NodeBucket *node = stack->firstBucket;
    char **buf = node->val;
    char *str1 = buf[stack->topElt];
    char *str2;
    if (stack->topElt > 0) {
        str2 = buf[stack->topElt - 1];
        buf[stack->topElt - 1] = str1;
        buf[stack->topElt] = str2;
    } else {
        buf = node->next->val;
        str2 = buf[stack->bucketSize - 1];
        buf[stack->bucketSize - 1] = str1;
        buf = node->val;
        buf[stack->topElt] = str2;
    }
}

void print (const Stack *stack) {
    if (stack == NULL) return;
    fprintf(stdout, "stack is:\n");
    if (stack->firstBucket == NULL) return;
    
    struct NodeBucket *node = stack->firstBucket;
    int c = stack->topElt + 1;
    char **buf;
    char *str;
    do {
        buf = node->val;
        for (int i = c - 1; i >= 0; i--) {
            str = buf[i];
            fprintf(stdout, "\t%s\n", str);
        }
        node = node->next;
        c = stack->bucketSize;
    } while (node != NULL);
}

void clear(Stack *stack) {
    if (stack == NULL) return;
    if (stack->firstBucket == NULL) return;
    
    struct NodeBucket *node = stack->firstBucket;
    char **buf;
    char *str;
    while (node != NULL) {
        buf = node->val;
        while (stack->topElt >= 0) {
            str = buf[stack->topElt--];
            free(str);
        }
        
        stack->firstBucket = node->next;
        stack->topElt = stack->bucketSize - 1;
        node->next = NULL;
        free(buf);
        free(node);
        node = stack->firstBucket;
    }
    stack->topElt = -1;
}

void destroyStack(Stack **stack) {
    if (stack == NULL) return;
    if (*stack == NULL) return;
    
    clear(*stack);
    free(*stack);
}