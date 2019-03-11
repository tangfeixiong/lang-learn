#include <stdio.h>
#include <stdlib.h>

#include <closest.h>

int main(void) {
    char travel[6];
    
    printf("Enter a 24-hour (hh:mm, where hh between 0 and 23) time: ");
    scanf("%s", travel);
    
    for (int i = 0; i < 6; i++) {
        if (!(travel[i] > 32 && travel[i] < 127)) {
            travel[i] = '\0';
            break;
        }
    }
    
    schedule flight = discover(travel);
    
    if (flight.departure == NULL || flight.arrival == NULL)
        printf("No appropriate flight\n");
    else
        printf("Closest departure time is %s, arriving at %s.\n", flight.departure, flight.arrival);
        
    return 0;
}