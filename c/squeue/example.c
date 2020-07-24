#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "queue.h"

int main(void) {
    Squeue *s1 = NULL;
    initSqueue (&s1);
    
    addFront (s1, "alpha");
    addFront (s1, "beta");
    addFront (s1, "gamma");
    addBack (s1, "delta");
    printf("This prints \"gamma beta alpha delta\" across four lines with a tab before each element, and preceded by \"stack is:\" on its own line:\n");
    print (s1, 'f');
    printf("This prints \"delta alpha beta gamma\" across four lines with a tab before each element, and preceded by \"stack is:\" on its own line:\n");
    print (s1, 'r');
    mergeFront(s1, 'f');
    printf("This prints \"gammabeta alpha delta\" across three lines with a tab before each element, and preceded by \"stack is:\" on its own line:\n");
    print(s1, 'f');
    mergeBack(s1, 'r');
    printf("This prints \"gammabeta deltaalpha\" across two lines with a tab before each element, and preceded by \"stack is:\" on its own line:\n");
    print(s1, 'f');
 leaveFront (s1);
 printf("This prints \"alphadelta\" in one line with a tab before each element, and preceded by \"stack is:\" on its own line:e\n");
 print(s1, 'f');
    addFront(s1, "zeta");
    addFront(s1, "eta");
    leaveBack (s1);
    printf("This prints \"eta zeta\" across two lines with a tab before each element, and preceded by \"stack is:\" on its own line:\n");
    print(s1, 'f');
    printf("This prints \"eta zeta\" in one line \n");
    printf("%s %s\n", peekFront(s1), peekBack(s1));
    printf("This nuke has no output, but is good form to call when done\n");
    nuke (s1);
    printf("This assertion should succeed\n");
    assert (isEmpty (s1));
    printf("Illegal direction should cause error message\n");
    print (s1, 'k');
    addBack (s1, "alpha");
    addBack (s1, "beta");
    addBack (s1, "gamma");
    reverse(s1);
    printf("This prints \"gamma beta alpha\" across two lines with a tab before each element, and preceded by \"stack is:\" on its own line:\n");
    print(s1, 'f');
    destroySqueue(&s1); //we will always call this for any squeue we test with so make sure it is implemented correctly to free any allocated memory    
    
    return 0;
}