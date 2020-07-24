#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "closest.h"

struct duration {
    int minutes;
    schedule* flight;
};

schedule flights[] = {
    {"8:00am", "10:16am"},
    {"9:43am", "11:52am"},
    {"11:19am", "1:31pm"},
    {"12:47pm", "3:00pm"}
};

int sincemidnight(char* time) {
    int hoursin24hour = 0;
    char hoursin12hour[3] = {'\0', '\0', '\0'};
    int minutes;
    char minutesintime[3] = "";
    int len;
    char midday[3] = "";
    char *pos;
    
    pos = strchr(time, ':'); 
    strncpy(hoursin12hour, time, pos - time);
    printf("%s\t", hoursin12hour);
    
    len = strlen(pos+1);
    if (len > 2) {
        strncpy(minutesintime, pos+1, len-2);
        printf("%s\t", minutesintime);
        
        strcpy(midday, pos+1+strlen(minutesintime));
        printf("%s\n", midday);
        
        hoursin24hour = atoi(hoursin12hour);
        if (strcmp("am", midday) == 0 || strcmp("AM", midday) == 0)
            if (hoursin24hour == 12) hoursin24hour = 0;
        if (strcmp("pm", midday) == 0 || strcmp("PM", midday) == 0)
            if (hoursin24hour != 12) hoursin24hour += 12;
    } else {
        strcpy(minutesintime, pos+1);
        printf("%s\n", minutesintime);
        hoursin24hour = atoi(hoursin12hour);
    }
    
    minutes = atoi(minutesintime);
    
    return hoursin24hour * 60 + minutes;
}

void convert(int size, schedule src[], struct duration since[]) {
    
    for (int i = 0; i < size; i++) {
        since[i].minutes = sincemidnight(src[i].departure);
        since[i].flight = &src[i];
    }
    
}

int cmpfunc(const void *a, const void *b) {
    return ((struct duration*)a)->minutes - ((struct duration*)b)->minutes;
}

schedule discover(char* travel) {
    int s = sizeof(flights)/sizeof(schedule);
    struct duration *sincedeparture = (struct duration *)malloc(s * sizeof(struct duration));
    
    convert(s, flights, sincedeparture);
    printf("---\n");

    int m = sincemidnight(travel);
    printf("---\n");
    
    for (int i = 0; i < s; i++) {
        sincedeparture[i].minutes -= m;
        printf("%d\t", sincedeparture[i].minutes);
    }
    printf("\n");
    
    qsort(sincedeparture, s, sizeof(struct duration), cmpfunc);
    
    schedule result;
    result.departure = NULL;
    result.arrival = NULL;
    int l;
    for (int i = 0; i < s; i++) {
        if (sincedeparture[i].minutes > 0) {
            printf("%d d->%s a<-%s\n", sincedeparture[i].minutes,  sincedeparture[i].flight->departure, sincedeparture[i].flight->arrival);
            l = strlen(sincedeparture[i].flight->departure);
            result.departure = (char *)malloc(l+1);
            strcpy(result.departure, sincedeparture[i].flight->departure);
            result.departure[l] = '\0';
            l = strlen(sincedeparture[i].flight->arrival);
            result.arrival = (char *)malloc(l+1);
            strcpy(result.arrival, sincedeparture[i].flight->arrival);
            result.arrival[l] = '\0';
            printf("d->%s a<-%s\n", result.departure, result.arrival);
            break;
        } 
    }
    
    return result;
}

