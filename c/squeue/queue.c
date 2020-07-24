#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include "queue.h"

struct Node{
 char* val;
 struct Node* next;
 struct Node* prev;
};

void initSqueue (Squeue **squeue) {
    if (squeue == NULL) return;
    
    *squeue = (Squeue *)malloc(sizeof(Squeue));
    (*squeue)->first = NULL;
    (*squeue)->last = NULL;
}

bool isEmpty (const Squeue *squeue) {
    if (squeue != NULL && squeue->first == NULL && squeue->last == NULL)
        return true;
        
    return false;
}

void addFront (Squeue *squeue, char *val) {
    if (squeue != NULL) {
        struct Node *node = (struct Node *)malloc(sizeof(struct Node));
        int l = strlen(val);
        
        char *str = (char *)malloc((l + 1) * sizeof(char));
        *(str+l) = '\0';
        strcpy(str, val);
        node->val = str;
        node->next = NULL;
        node->prev = NULL;
        
        struct Node *q = squeue->first;
        if (q != NULL) {
            node->next = q;
            q->prev = node;
        } else
            squeue->last = node;
        
        squeue->first = node;
    }
}

void addBack (Squeue *squeue, char *val) {
    if (squeue != NULL) {
        struct Node *node = (struct Node *)malloc(sizeof(struct Node));
        int l = strlen(val);
        
        char *str = (char *)malloc((l + 1) * sizeof(char));
        *(str+l) = '\0';
        strcpy(str, val);
        node->val = str;
        node->next = NULL;
        node->prev = NULL;
        
        struct Node *q = squeue->last;
        if (q != NULL) {
            node->prev = q;
            q->next = node;
        } else
            squeue->first = node;
        
        squeue->last = node;
    }    
}

void leaveFront (Squeue *squeue) {
    assert(!isEmpty(squeue));
    
    struct Node *n = squeue->first;
    squeue->first = n->next;
    if (squeue->first != NULL)
        squeue->first->prev = NULL;
    if (squeue->last == n)
        squeue->last = NULL;
    
    n->next = NULL;
    n->prev = NULL;
    free(n->val);
    free(n);
}


void leaveBack (Squeue *squeue) {
    assert(!isEmpty(squeue));
    
    struct Node *n = squeue->last;
    squeue->last = n->prev;
    if (squeue->last != NULL)
        squeue->last->next = NULL;
    if (squeue->first == n)
        squeue->first = NULL;
    
    n->next = NULL;
    n->prev = NULL;
    free(n->val);
    free(n);
}

char* peekFront (const Squeue * squeue) {
    assert(!isEmpty(squeue));

    int l = strlen(squeue->first->val);

    char *str = (char *)malloc((l+1) * sizeof(char));
    *(str+l) = '\0';

    strcpy(str, squeue->first->val);
    return str;
}

char* peekBack (const Squeue * squeue) {
    assert(!isEmpty(squeue));
    
    int l = strlen(squeue->last->val);

    char *str = (char *)malloc((l+1) * sizeof(char));    
    *(str+l) = '\0';

    strcpy(str, squeue->last->val);
    return str;
}

void print (const Squeue * squeue, char direction) {
    struct Node *n;
    switch (direction) {
        case 'f':
            fprintf(stdout, "queue is:\n");
            n = squeue->first;
            while (n != NULL) {
                fprintf(stdout, "%s", n->val);
                n = n->next;
                if (n != NULL) fputc('\t', stdout);
            }
            fputc('\n', stdout);
            break;
        case 'r' :
            fprintf(stdout, "reversed queue is:\n");
            n = squeue->last;
            while (n != NULL) {
                fprintf(stdout, "%s", n->val);
                n = n->prev;
                if (n != NULL) fputc('\t', stdout);
            }            
            fputc('\n', stdout);
            break;
        default:
            fprintf(stderr, "Error, illegal direction %c\n", direction);
    }
}

void nuke (Squeue * squeue) {
    assert(!isEmpty(squeue));
    
    struct Node *q = squeue->first;
    squeue->first = NULL;
    squeue->last = NULL;
    struct Node *n;
    while (q != NULL) {
        n = q;
        q = n->next;
        if (q != NULL)
            q->prev = NULL;
        n->next = NULL;
        free(n->val);
        free(n);
    }
}

void mergeFront(Squeue* squeue, char direction) {
    assert(!isEmpty(squeue));
    
    struct Node *n = squeue->first->next;
    assert(n != NULL);
    
    int l1 = strlen(squeue->first->val);
    int l2 = strlen(n->val);
    char *str = (char *)malloc((l1+l2+1) * sizeof(char));
    *(str+l1+l2) = '\0';
    switch (direction) {
    case 'f':
        strcpy(str, squeue->first->val);
        strcpy(str+l1, n->val);
        break;
    case 'r':
        strcpy(str, n->val);
        strcpy(str+l2, squeue->first->val);
        break;
    default:
        fprintf(stderr, "Error, illegal direction %c\n", direction);
        return;
    }
    
    free(squeue->first->val);
    squeue->first->val = str;
    squeue->first->next = n->next;
    squeue->first->next->prev = squeue->first;
    n->next = NULL;
    n->prev = NULL;
    free(n->val);
    free(n);
}

void mergeBack(Squeue* squeue, char direction) {
    assert(!isEmpty(squeue));
    
    struct Node *n = squeue->last->prev;
    assert(n != NULL);
    
    int l1 = strlen(squeue->last->val);
    int l2 = strlen(n->val);
    char *str = (char *)malloc((l1+l2+1) * sizeof(char));
    *(str+l1+l2) = '\0';
    switch (direction) {
    case 'f':
        strcpy(str, n->val);
        strcpy(str+l2, squeue->last->val);
        break;
    case 'r':
        strcpy(str, squeue->last->val);
        strcpy(str+l1, n->val);
        break;
    default:
        fprintf(stderr, "Error, illegal direction %c\n", direction);
        return;
    }
    
    free(squeue->last->val);
    squeue->last->val = str;
    squeue->last->prev = n->prev;
    squeue->last->prev->next = squeue->last;
    n->next = NULL;
    n->prev = NULL;
    free(n->val);
    free(n);
}

void reverse(Squeue* squeue) {
    assert(!isEmpty(squeue));
    
    struct Node *n;
    n = squeue->first;
    squeue->first = squeue->last;
    squeue->last = n;
    struct Node *q;
    while (n != NULL) {
        q = n->next;
        n->next = n->prev;
        n->prev = q;
        n = q;
    }
}

void destroySqueue(Squeue **squeue) {
    if (squeue == NULL) return;
    if (*squeue == NULL) return;
    
    nuke(*squeue);
    free(*squeue);
}
