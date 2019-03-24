#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include "queue.h"

int main(void) {
    Queue *queue = NULL;
    initQueue(&queue);
    
    int op = -1;
    NumericItemP pItem;
    // bool b;

    for (;;) {
        printf("Enter operation: ");
        scanf("%d", &op);

        switch (op) {
        case 1:
            printf("Enter item to enter: ");
            scanf("%d", pItem);
            
            append(queue, pItem);
            continue;
        case 2:
            leave(queue);
            continue;
        case 3:
            pItem = seekHead(queue);
            printf("The head value of queue is: %d\n", *pItem);
            continue;
        case 4:
            pItem = seekTail(queue);
            printf("The tail value of queue is: %d\n", *pItem);
            continue;
        case 5:
            printAll(queue);
            continue;
        case 6:
            printf("Queue is %s\n", (isEmpty(queue)? "empty" : "not empty"));
            continue;
        case 7:
            clear(queue);
            continue;
        case 0:
            printf("Bye!\n");
            break;
        default:
            printf("Illegal operation: %d, valid choosen are 1~7 and 0(quit program)\n", op);
            continue;
        }
        break;
    }
    
    destroyQueue(&queue);
    return 0;
}

