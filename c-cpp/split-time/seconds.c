
#include <stdio.h>
#include <stdlib.h>

#include "simpletime.h"

struct dtseconds {
	int days;
	int hours;
	int minutes;
	int seconds;
};

time secondstohms(int totalseconds) {
    time t;
    
    t.minutes = totalseconds / 60;
    t.seconds = totalseconds % 60;
    t.hours = t.minutes / 60;
    t.minutes %= 60;
    
    return t;
}

int secondstotime(int totalseconds, int* days, int* hours, int* minutes, int* seconds) {
	struct dtseconds dts;
	int ds, hs, ms, ss;
	
	if (days == NULL || hours == NULL || minutes == NULL || seconds == NULL)
	    return 1;
	
	dts.seconds = totalseconds;
	
	ss = dts.seconds % 60;
	dts.minutes = (dts.seconds - ss) / 60;
	ms = dts.minutes % 60;
	dts.hours = (dts.minutes - ms) / 60;
	hs = dts.hours % 24;
	ds = (dts.hours - hs) / 24;
	dts.days = ds;
	
	*days = dts.days;
	*hours = hs;
	*minutes = ms;
	*seconds = ss;
	
	return 0;
}