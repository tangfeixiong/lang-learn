#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "stack.h"

int main (int argc, char* argv[]) {
    Stack *s = NULL;
    initStack (3, &s);
    push("alpha", s);
    printf("This prints \"alpha\":\n");
    printf("%s\n", top(s));
    push("beta", s);
    printf("This prints \"beta\":\n");
    printf("%s\n", top(s));
    push ("gamma", s);
    printf("This prints \"gamma\":\n");
    printf("%s\n", top(s));
    push ("delta", s);
    printf("This prints \"delta\":\n");
    printf("%s\n", top(s));
    printf("This will print the whole stack with a tab before each element:\"delta gamma beta alpha\" across 4 lines, preceded by \"stack is:\" on a line on its own\n");
    print(s);
    clear(s);
    printf("This will print an empty stack so just \"stack is:\"\n");
    print(s);
    push ("alice", s);
    printf("This will print a stack that only contains \"alice\"\n");
    print(s);
    pop (s);
    printf("This will print an empty stack so just \"stack is:\"\n");
    print(s);
    push ("bob", s);
    push ("bob", s);
    printf("This will print the whole stack with a tab before each element:\"bob bob\" across 2 lines, preceded by \"stack is:\" on a line on its own\n");
    ;
    print(s);
    push("mike", s);
    printf("This will print the whole stack with a tab before each element:\"mike bob bob\" across 3 lines, preceded by \"stack is:\" on a line on its own\n");
    ;
    print(s);
    swap(s);
    printf("This will print the whole stack after swapping first two with a tab before each element:\"bob mike bob\" across 3 lines, preceded by \"stack is:\" on a line on its own\n");
    ;
    print(s);
    clear(s);
    printf("This will print an empty stack so just \"stack is:\"\n");
    print(s);
    destroyStack(&s); //we will always call this for any stack we test with so make sure it is implemented correctly to free any allocated memory
    return 0;
}