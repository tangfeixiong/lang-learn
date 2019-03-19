#include <stdio.h>
#include <stdlib.h>
#include "linked_list.h"

struct node *add_to_list(struct node *list, int n, char marker){
	struct node *new_node;
	new_node = malloc(sizeof(struct node));

	if(new_node == NULL){
		printf("Error: malloc failed in add_to_list\n");
		exit(EXIT_FAILURE);
	}

	new_node->value = n;
	new_node->marker = marker;
	new_node->next = list;

	return new_node;
}

// Recursively to match node
struct node *find_last(struct node *list, int n) {
    if (list == NULL) return NULL;
    
    struct node *result = find_last(list->next, n);
    if (result != NULL) return result;
    
    if (list->value == n) {
        result = list;
        return result;
    }
        
    return NULL;
}
